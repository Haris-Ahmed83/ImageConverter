import os
import tempfile
import zipfile
from werkzeug.utils import secure_filename
import utils.formats as formats_mod
from utils.engines import convert_file, set_conversion_folder, is_engine_available

UPLOAD_FOLDER = None
CONVERSION_FOLDER = None

def init_paths(upload, conversion):
    global UPLOAD_FOLDER, CONVERSION_FOLDER
    UPLOAD_FOLDER = upload
    CONVERSION_FOLDER = conversion
    os.makedirs(upload, exist_ok=True)
    os.makedirs(conversion, exist_ok=True)
    set_conversion_folder(conversion)

def detect_format(filename):
    ext = os.path.splitext(filename)[1].lower()
    for key, info in formats_mod.FORMATS.items():
        if ext in [ex.lower() for ex in info['extensions']]:
            return key
        if ext in ('.jpg', '.jpeg') and key == 'jpg':
            return 'jpg'
        if ext in ('.tiff', '.tif') and key == 'tiff':
            return 'tiff'
        if ext in ('.heic', '.heif') and key == 'heic':
            return 'heic'
    return None

def process_conversion(input_path, source_fmt, target_fmt, quality=85):
    return convert_file(input_path, source_fmt, target_fmt, quality)

def process_batch(file_list, target_fmt, quality=85):
    results = []
    for filepath, filename in file_list:
        src_fmt = detect_format(filename)
        if not src_fmt:
            results.append({'filename': filename, 'success': False, 'error': 'Unknown format'})
            continue

        result = process_conversion(filepath, src_fmt, target_fmt, quality)
        if result['success']:
            results.append({
                'filename': os.path.splitext(filename)[0] + f'.{target_fmt}',
                'output_path': result['output_path'],
                'success': True
            })
        else:
            results.append({'filename': filename, 'success': False, 'error': result.get('error', 'Conversion failed')})
    return results

def create_zip(output_path, file_list):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in file_list:
            if os.path.exists(f['output_path']):
                zf.write(f['output_path'], f['filename'])
    return output_path

_SAFE_FORMAT_NAMES = {
    'jpg': 'jpeg', 'tiff': 'tiff', 'heic': 'heic',
    'svg': 'svg', 'eps': 'eps', 'djvu': 'djvu',
    'pdf': 'pdf', 'psd': 'psd', 'indd': 'indd',
}
