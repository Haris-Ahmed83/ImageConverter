import os
import tempfile
import rawpy
from PIL import Image

def convert(input_path, source_fmt, target_fmt, quality=85):
    try:
        with rawpy.imread(input_path) as raw:
            rgb = raw.postprocess()

        img = Image.fromarray(rgb)

        target_ext = target_fmt.replace('jpg', 'jpeg')
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix=f'.{target_ext}', delete=False
        )

        save_kwargs = _get_save_kwargs(target_fmt, quality)
        img.save(temp_out.name, **save_kwargs)
        temp_out.close()

        return {'success': True, 'output_path': temp_out.name}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def _get_save_kwargs(fmt, quality):
    fmt = fmt.lower()
    if fmt in ('jpg', 'jpeg'):
        return {'format': 'JPEG', 'quality': quality, 'optimize': True}
    elif fmt == 'png':
        return {'format': 'PNG', 'optimize': True}
    elif fmt == 'webp':
        return {'format': 'WebP', 'quality': quality}
    elif fmt in ('tiff', 'tif'):
        return {'format': 'TIFF', 'compression': 'tiff_lzw'}
    elif fmt == 'dng':
        return {'format': 'TIFF'}
    elif fmt == 'bmp':
        return {'format': 'BMP'}
    else:
        return {'format': fmt.upper()}
