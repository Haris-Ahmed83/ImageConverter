import os
import traceback
import logging
logging.disable(logging.CRITICAL)

ENGINE_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(ENGINE_DIR)

CONVERSION_FOLDER = None

def set_conversion_folder(path):
    global CONVERSION_FOLDER
    CONVERSION_FOLDER = path
    os.makedirs(path, exist_ok=True)

def convert_file(input_path, source_fmt, target_fmt, quality=85):
    from utils.formats import FORMATS

    src_info = FORMATS.get(source_fmt)
    dst_info = FORMATS.get(target_fmt)

    if not src_info:
        return {'success': False, 'error': f'Unsupported source format: {source_fmt}'}
    if not dst_info:
        return {'success': False, 'error': f'Unsupported target format: {target_fmt}'}

    src_engine = src_info['engine']
    dst_engine = dst_info['engine']

    try:
        if src_engine == 'image' and dst_engine == 'image':
            from utils.engines.image_engine import convert as img_conv
            return img_conv(input_path, source_fmt, target_fmt, quality)
        elif src_engine == 'raw' and dst_engine == 'image':
            from utils.engines.raw_engine import convert as raw_conv
            return raw_conv(input_path, source_fmt, target_fmt, quality)
        elif dst_engine == 'image' and src_engine in ('document', 'vector', 'video', 'cad'):
            # Use intermediate PDF then convert to image
            return _convert_via_intermediate(input_path, source_fmt, 'pdf', target_fmt, quality, 'ImageMagick' if dst_engine == 'video' else None)
        elif src_engine == 'document' and dst_engine == 'document':
            return _libreoffice_convert(input_path, source_fmt, target_fmt)
        elif src_engine == 'video' and dst_engine == 'video':
            return _ffmpeg_convert(input_path, source_fmt, target_fmt)
        elif src_engine == 'video' and dst_engine == 'audio':
            return _ffmpeg_convert(input_path, source_fmt, target_fmt)
        elif src_engine == 'video' and dst_engine == 'image':
            return _ffmpeg_extract_frame(input_path, source_fmt, target_fmt)
        elif src_engine == 'archive':
            from utils.engines.archive_engine import convert as arch_conv
            return arch_conv(input_path, source_fmt, target_fmt)
        elif src_engine == 'font':
            from utils.engines.font_engine import convert as font_conv
            return font_conv(input_path, source_fmt, target_fmt)
        elif src_engine == 'vector' and dst_engine == 'image':
            from utils.engines.vector_engine import convert as vec_conv
            return vec_conv(input_path, source_fmt, target_fmt, quality)
        elif src_engine == 'ebook':
            from utils.engines.ebook_engine import convert as ebook_conv
            return ebook_conv(input_path, source_fmt, target_fmt)
        elif src_engine == 'image' and dst_engine in ('document', 'vector', 'video', 'cad'):
            return {'success': False, 'error': f'Conversion from {source_fmt.upper()} to {target_fmt.upper()} not supported'}
        else:
            return {'success': False, 'error': f'Conversion from {source_fmt.upper()} to {target_fmt.upper()} not supported'}
    except Exception as e:
        return {'success': False, 'error': str(e), 'traceback': traceback.format_exc()}

def _convert_via_intermediate(input_path, source_fmt, inter_fmt, target_fmt, quality, engine_hint=None):
    import tempfile
    import subprocess
    from PIL import Image

    with tempfile.NamedTemporaryFile(suffix=f'.{inter_fmt}', delete=False) as tmp:
        inter_path = tmp.name

    if engine_hint == 'ImageMagick':
        subprocess.run(['magick', input_path, inter_path], capture_output=True)
    else:
        subprocess.run(['soffice', '--headless', '--convert-to', inter_fmt, '--outdir',
                        os.path.dirname(inter_path), input_path], capture_output=True)

    if not os.path.exists(inter_path):
        return {'success': False, 'error': f'Could not convert {source_fmt.upper()} to intermediate format'}

    try:
        from utils.engines.image_engine import convert as img_conv
        return img_conv(inter_path, inter_fmt, target_fmt, quality)
    finally:
        try: os.unlink(inter_path)
        except: pass

def _libreoffice_convert(input_path, source_fmt, target_fmt):
    import tempfile, subprocess
    with tempfile.NamedTemporaryFile(suffix=f'.{target_fmt}', delete=False) as tmp:
        out_path = tmp.name

    try:
        result = subprocess.run(
            ['soffice', '--headless', '--convert-to', target_fmt,
             '--outdir', os.path.dirname(out_path), input_path],
            capture_output=True, timeout=60
        )
        if result.returncode != 0:
            return {'success': False, 'error': f'LibreOffice conversion failed: {result.stderr.decode()}'}
        return {'success': True, 'output_path': out_path}
    except FileNotFoundError:
        return {'success': False, 'error': 'LibreOffice is not installed on this server'}
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Conversion timed out'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def _ffmpeg_convert(input_path, source_fmt, target_fmt):
    import tempfile, subprocess
    with tempfile.NamedTemporaryFile(suffix=f'.{target_fmt}', delete=False) as tmp:
        out_path = tmp.name

    try:
        result = subprocess.run(
            ['ffmpeg', '-i', input_path, '-y', out_path],
            capture_output=True, timeout=120
        )
        if result.returncode != 0:
            return {'success': False, 'error': f'FFmpeg conversion failed: {result.stderr.decode()}'}
        return {'success': True, 'output_path': out_path}
    except FileNotFoundError:
        return {'success': False, 'error': 'FFmpeg is not installed on this server'}
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Conversion timed out'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def _ffmpeg_extract_frame(input_path, source_fmt, target_fmt):
    import tempfile, subprocess
    with tempfile.NamedTemporaryFile(suffix=f'.{target_fmt}', delete=False) as tmp:
        out_path = tmp.name

    try:
        result = subprocess.run(
            ['ffmpeg', '-i', input_path, '-vframes', '1', '-y', out_path],
            capture_output=True, timeout=60
        )
        if result.returncode != 0:
            return {'success': False, 'error': f'FFmpeg frame extraction failed: {result.stderr.decode()}'}
        return {'success': True, 'output_path': out_path}
    except FileNotFoundError:
        return {'success': False, 'error': 'FFmpeg is not installed on this server'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def is_engine_available(engine_name):
    import shutil
    if engine_name in ('image', 'raw', 'archive', 'font'):
        return True
    if engine_name in ('video',):
        return shutil.which('ffmpeg') is not None
    if engine_name in ('document',):
        return shutil.which('soffice') is not None
    if engine_name in ('vector',):
        return shutil.which('magick') is not None or shutil.which('inkscape') is not None
    if engine_name in ('ebook',):
        return shutil.which('ebook-convert') is not None
    if engine_name in ('cad',):
        return shutil.which('magick') is not None
    return False
