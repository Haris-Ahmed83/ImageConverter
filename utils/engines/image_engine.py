import os
import tempfile
from PIL import Image

def convert(input_path, source_fmt, target_fmt, quality=85):
    try:
        img = Image.open(input_path)
        img = img.convert('RGB') if target_fmt in ('jpg', 'jpeg') else img

        target_ext = target_fmt.replace('jpg', 'jpeg')
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix=f'.{target_ext}', delete=False
        )

        save_kwargs = _get_save_kwargs(target_fmt, quality, img)
        img.save(temp_out.name, **save_kwargs)
        temp_out.close()

        return {'success': True, 'output_path': temp_out.name}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def _get_save_kwargs(fmt, quality, img):
    fmt = fmt.lower()
    if fmt in ('jpg', 'jpeg'):
        return {'format': 'JPEG', 'quality': quality, 'optimize': True}
    elif fmt == 'png':
        return {'format': 'PNG', 'optimize': True}
    elif fmt == 'webp':
        return {'format': 'WebP', 'quality': quality}
    elif fmt == 'gif':
        return {'format': 'GIF', 'optimize': True}
    elif fmt == 'bmp':
        return {'format': 'BMP'}
    elif fmt in ('tiff', 'tif'):
        return {'format': 'TIFF', 'compression': 'tiff_lzw'}
    elif fmt == 'ico':
        sizes = [(16, 16), (32, 32), (48, 48)]
        img = img.copy()
        img.save = lambda fp, **kw: _save_ico(fp, img, sizes, **kw)
        return {'format': 'ICO'}
    elif fmt == 'avif':
        return {'format': 'AVIF', 'quality': quality}
    elif fmt in ('heic', 'heif'):
        return {'format': 'HEIF', 'quality': quality}
    elif fmt == 'tga':
        return {'format': 'TGA'}
    elif fmt == 'pcx':
        return {'format': 'PCX'}
    elif fmt in ('pnm', 'ppm', 'pgm', 'pbm'):
        return {'format': fmt.upper()}
    elif fmt == 'dds':
        return {'format': 'DDS'}
    elif fmt == 'sgi':
        return {'format': 'SGI'}
    elif fmt in ('jp2', 'j2k', 'jpc'):
        return {'format': 'JPEG2000', 'quality_mode': 'lossy', 'quality': quality}
    elif fmt == 'xbm':
        return {'format': 'XBM'}
    elif fmt == 'psd':
        return {'format': 'PSD'}
    elif fmt == 'tiff_lzw':
        return {'format': 'TIFF', 'compression': 'tiff_lzw'}
    else:
        return {'format': fmt.upper()}

def _save_ico(fp, img, sizes, **kw):
    import struct
    from PIL import Image as PILImage
    import io
    ico_data = b''
    header = struct.pack('<HHH', 0, 1, len(sizes))
    ico_data += header
    offset = 6 + 16 * len(sizes)
    for s in sizes:
        tmp = img.resize(s, PILImage.LANCZOS)
        buf = io.BytesIO()
        tmp.save(buf, format='PNG')
        data = buf.getvalue()
        ico_data += struct.pack('<BBBBHHII', s[0], s[1], 0, 0, 1, 32, len(data), offset)
        offset += len(data)
    for s in sizes:
        tmp = img.resize(s, PILImage.LANCZOS)
        buf = io.BytesIO()
        tmp.save(buf, format='PNG')
        ico_data += buf.getvalue()
    with open(fp, 'wb') as f:
        f.write(ico_data)

def convert_pdf_page(input_path, page_num, target_fmt, quality=85):
    try:
        img = Image.open(input_path)
        if hasattr(img, 'seek'):
            img.seek(page_num)
        return convert(input_path, 'pdf', target_fmt, quality)
    except Exception as e:
        return {'success': False, 'error': str(e)}
