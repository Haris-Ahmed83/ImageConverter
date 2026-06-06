def convert(input_path, source_fmt, target_fmt, quality=85):
    try:
        # Try Pillow EPS reader or use intermediate via ImageMagick/Ghostscript
        from PIL import Image
        import tempfile, os, subprocess

        # First try to use ImageMagick for vector to raster
        if subprocess.run(['which', 'magick'], capture_output=True).returncode == 0:
            temp_out = tempfile.NamedTemporaryFile(
                dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
                suffix=f'.{target_fmt}', delete=False
            )
            temp_out.close()
            result = subprocess.run(
                ['magick', input_path, '-density', '300', temp_out.name],
                capture_output=True, timeout=30
            )
            if result.returncode == 0:
                return {'success': True, 'output_path': temp_out.name}

        # Try direct Pillow open (works for EPS if ghostscript is available)
        img = Image.open(input_path)
        if target_fmt in ('jpg', 'jpeg'):
            img = img.convert('RGB')
        elif img.mode != 'RGBA' and target_fmt == 'png':
            img = img.convert('RGBA')

        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix=f'.{target_fmt}', delete=False
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
        return {'format': 'JPEG', 'quality': quality}
    elif fmt == 'png':
        return {'format': 'PNG'}
    elif fmt == 'webp':
        return {'format': 'WebP', 'quality': quality}
    elif fmt in ('tiff', 'tif'):
        return {'format': 'TIFF'}
    elif fmt == 'bmp':
        return {'format': 'BMP'}
    elif fmt == 'gif':
        return {'format': 'GIF'}
    elif fmt == 'ico':
        return {'format': 'ICO'}
    else:
        return {'format': fmt.upper()}
