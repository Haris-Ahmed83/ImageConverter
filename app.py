import os
import uuid
import zipfile
from flask import Flask, render_template, request, send_file, jsonify, abort
from utils.formats import FORMATS, get_format_info, get_extension, CATEGORIES
import utils.converter as converter_mod
import utils.bgremover as bgremover_mod

ON_VERCEL = os.environ.get('VERCEL', '') == '1' or os.environ.get('VERCEL_ENV', '')
BASE_DIR = '/tmp' if ON_VERCEL else os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
CONVERSION_FOLDER = os.path.join(BASE_DIR, 'conversions')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERSION_FOLDER, exist_ok=True)

converter_mod.init_paths(UPLOAD_FOLDER, CONVERSION_FOLDER)
bgremover_mod.set_conversion_dir(CONVERSION_FOLDER)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

MIME_MAP = {
    '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
    '.webp': 'image/webp', '.gif': 'image/gif', '.bmp': 'image/bmp',
    '.tiff': 'image/tiff', '.tif': 'image/tiff', '.ico': 'image/x-icon',
    '.avif': 'image/avif', '.heic': 'image/heic', '.heif': 'image/heic',
    '.svg': 'image/svg+xml', '.pdf': 'application/pdf', '.zip': 'application/zip',
    '.mp4': 'video/mp4', '.webm': 'video/webm', '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav', '.flac': 'audio/flac', '.ogg': 'audio/ogg',
    '.epub': 'application/epub+zip', '.mobi': 'application/x-mobipocket-ebook',
    '.ttf': 'font/ttf', '.otf': 'font/otf', '.woff': 'font/woff', '.woff2': 'font/woff2',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.7z': 'application/x-7z-compressed', '.tar': 'application/x-tar',
}

def cleanup_file(path):
    try:
        if os.path.exists(path):
            os.unlink(path)
    except:
        pass

@app.route('/')
def index():
    import json
    def _serialize(fmts):
        return {k: {'name': v['name'], 'full_name': v['full_name'], 'category': v['category'],
                     'color': v['color'], 'engine': v.get('engine', ''),
                     'mime': v['mime'], 'extensions': v['extensions']}
                for k, v in fmts.items()}
    return render_template('index.html', categories=CATEGORIES, formats=FORMATS,
                           formats_json=json.dumps(_serialize(FORMATS)),
                           categories_json=json.dumps(CATEGORIES))

@app.context_processor
def inject_globals():
    return dict(FORMATS=FORMATS, CATEGORIES=CATEGORIES)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400

    target_format = request.form.get('target_format', '').lower().replace('jpeg', 'jpg').replace('tif', 'tiff')
    quality = int(request.form.get('quality', 85))

    fmt_info = get_format_info(target_format)
    if not fmt_info:
        return jsonify({'success': False, 'error': f'Unsupported target format: {target_format}'}), 400

    unique_id = str(uuid.uuid4())
    input_filename = f"{unique_id}_input{os.path.splitext(file.filename)[1] or '.bin'}"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    file.save(input_path)

    try:
        src_fmt = converter_mod.detect_format(file.filename)
        if not src_fmt:
            return jsonify({'success': False, 'error': 'Could not detect source format'}), 400

        result = converter_mod.process_conversion(input_path, src_fmt, target_format, quality)
        if result['success']:
            ext = get_extension(target_format)
            return jsonify({
                'success': True,
                'download_url': f"/download/{os.path.basename(result['output_path'])}",
                'filename': f"converted{ext}"
            })
        else:
            return jsonify({'success': False, 'error': result.get('error', 'Conversion failed')}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        cleanup_file(input_path)

@app.route('/convert/batch', methods=['POST'])
def convert_batch():
    if 'files' not in request.files:
        return jsonify({'success': False, 'error': 'No files uploaded'}), 400

    files = request.files.getlist('files')
    if not files or len(files) == 0:
        return jsonify({'success': False, 'error': 'No files selected'}), 400

    target_format = request.form.get('target_format', '').lower().replace('jpeg', 'jpg').replace('tif', 'tiff')
    quality = int(request.form.get('quality', 85))

    fmt_info = get_format_info(target_format)
    if not fmt_info:
        return jsonify({'success': False, 'error': f'Unsupported target format: {target_format}'}), 400

    ext = get_extension(target_format)
    batch_id = str(uuid.uuid4())
    results = []
    output_paths = []

    for file in files:
        if file.filename == '':
            results.append({'filename': '', 'success': False, 'error': 'Empty filename'})
            continue

        src_fmt = converter_mod.detect_format(file.filename)
        if not src_fmt:
            results.append({'filename': file.filename, 'success': False, 'error': 'Unknown format'})
            continue

        input_filename = f"{batch_id}_{uuid.uuid4().hex}_input{os.path.splitext(file.filename)[1] or '.bin'}"
        input_path = os.path.join(UPLOAD_FOLDER, input_filename)
        file.save(input_path)

        try:
            result = converter_mod.process_conversion(input_path, src_fmt, target_format, quality)
            if result['success']:
                output_paths.append(result['output_path'])
                base = os.path.splitext(file.filename)[0]
                results.append({'filename': f"{base}{ext}", 'success': True,
                                'download_url': f"/download/{os.path.basename(result['output_path'])}"})
            else:
                results.append({'filename': file.filename, 'success': False, 'error': result.get('error', 'Failed')})
        except Exception as e:
            results.append({'filename': file.filename, 'success': False, 'error': str(e)})
        finally:
            cleanup_file(input_path)

    as_zip = request.form.get('as_zip', '1') == '1'
    if as_zip and len(output_paths) > 0:
        zip_filename = f"converted_{batch_id}.zip"
        zip_path = os.path.join(CONVERSION_FOLDER, zip_filename)
        converter_mod.create_zip(zip_path, [
            {'output_path': p, 'filename': r['filename']}
            for p, r in zip(output_paths, [r for r in results if r['success']])
        ])
        return jsonify({'success': True, 'results': results, 'zip_url': f"/download/{zip_filename}"})

    return jsonify({'success': True, 'results': results})

@app.route('/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400

    quality = int(request.form.get('quality', 80))
    quality = max(1, min(100, quality))

    ext = os.path.splitext(file.filename)[1].lower()
    unique_id = str(uuid.uuid4())
    input_filename = f"{unique_id}_input{ext or '.bin'}"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    file.save(input_path)

    original_size = os.path.getsize(input_path)

    try:
        src_fmt = converter_mod.detect_format(file.filename)
        if not src_fmt:
            return jsonify({'success': False, 'error': 'Unsupported format'}), 400

        result = converter_mod.process_conversion(input_path, src_fmt, src_fmt, quality)
        if result['success']:
            compressed_size = os.path.getsize(result['output_path'])
            savings = round((1 - compressed_size / original_size) * 100, 1) if original_size > 0 else 0
            return jsonify({
                'success': True,
                'download_url': f"/download/{os.path.basename(result['output_path'])}",
                'filename': f"compressed{ext}",
                'original_size': original_size,
                'compressed_size': compressed_size,
                'savings': savings
            })
        else:
            return jsonify({'success': False, 'error': result.get('error', 'Compression failed')}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        cleanup_file(input_path)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400

    output_format = request.form.get('format', 'png').lower()
    if output_format not in ('png', 'jpg', 'jpeg', 'webp'):
        output_format = 'png'

    ext = os.path.splitext(file.filename)[1].lower()
    unique_id = str(uuid.uuid4())
    input_filename = f"{unique_id}_input{ext or '.bin'}"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    file.save(input_path)

    try:
        output_path = bgremover_mod.remove_background(input_path, output_format=output_format)
        out_ext = output_format if output_format != 'jpeg' else 'jpg'
        return jsonify({
            'success': True,
            'download_url': f"/download/{os.path.basename(output_path)}",
            'filename': f"no-bg.{out_ext}"
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        cleanup_file(input_path)

@app.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(CONVERSION_FOLDER, filename)
    if not os.path.exists(filepath):
        abort(404)

    ext = os.path.splitext(filename)[1].lower()
    mime = MIME_MAP.get(ext, 'application/octet-stream')

    response = send_file(filepath, mimetype=mime, as_attachment=True, download_name=f"converted{ext}")

    @response.call_on_close
    def _cleanup():
        cleanup_file(filepath)

    return response

@app.route('/formats')
def formats_index():
    return render_template('formats_index.html', categories=CATEGORIES, formats=FORMATS)

@app.route('/api')
def api_docs():
    return render_template('api.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/<path:slug>')
def format_page(slug):
    slug = slug.lower()
    if '-' in slug:
        parts = slug.split('-to-')
        if len(parts) == 2:
            src_slug, dst_slug = parts
            src_info = get_format_info(src_slug)
            dst_info = get_format_info(dst_slug)
            if src_info and dst_info:
                import json
                def _serialize(fmts):
                    return {k: {'name': v['name'], 'full_name': v['full_name'], 'category': v['category'],
                                 'color': v['color'], 'engine': v.get('engine', ''),
                                 'mime': v['mime'], 'extensions': v['extensions']}
                            for k, v in fmts.items()}
                return render_template('convert.html',
                    src_info=src_info, dst_info=dst_info,
                    src_slug=src_slug.replace('jpeg', 'jpg') if 'jpeg' in src_slug else src_slug,
                    dst_slug=dst_slug.replace('jpeg', 'jpg') if 'jpeg' in dst_slug else dst_slug,
                    formats_json=json.dumps(_serialize(FORMATS)),
                    categories_json=json.dumps(CATEGORIES))
    abort(404)

@app.route('/sitemap.xml')
def sitemap():
    pages = ['/', '/formats']
    for src_key in FORMATS:
        for dst_key in FORMATS:
            if src_key != dst_key:
                pages.append(f'/{src_key}-to-{dst_key}')
                if len([p for p in pages if p.startswith(f'/{src_key}-to-')]) > 5:
                    break
        if len(pages) > 500:
            break

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml += f'  <url><loc>https://image-converter-lake.vercel.app{page}</loc></url>\n'
    xml += '</urlset>'
    return xml, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
