import os
import tempfile
import subprocess

def convert(input_path, source_fmt, target_fmt):
    conversion_map = {
        'ttf': {'otf': _font_to_otf, 'woff': _font_to_woff, 'woff2': _font_to_woff2, 'eot': _font_to_eot},
        'otf': {'ttf': _font_to_ttf, 'woff': _font_to_woff, 'woff2': _font_to_woff2, 'eot': _font_to_eot},
        'woff': {'ttf': _font_to_ttf, 'otf': _font_to_otf, 'woff2': _font_to_woff2, 'eot': _font_to_eot},
        'woff2': {'ttf': _font_to_ttf, 'otf': _font_to_otf, 'woff': _font_to_woff, 'eot': _font_to_eot},
        'eot': {'ttf': _font_to_ttf, 'otf': _font_to_otf, 'woff': _font_to_woff, 'woff2': _font_to_woff2},
    }

    if source_fmt in conversion_map and target_fmt in conversion_map[source_fmt]:
        return conversion_map[source_fmt][target_fmt](input_path)
    return {'success': False, 'error': f'Font conversion from {source_fmt} to {target_fmt} not supported'}

def _font_to_ttf(input_path):
    return _run_fonttools(input_path, 'ttf')

def _font_to_otf(input_path):
    return _run_fonttools(input_path, 'otf')

def _font_to_woff(input_path):
    return _run_fonttools(input_path, 'woff')

def _font_to_woff2(input_path):
    return _run_fonttools(input_path, 'woff2')

def _font_to_eot(input_path):
    return _run_fonttools(input_path, 'eot')

def _run_fonttools(input_path, target_fmt):
    try:
        import subprocess
        # Try using fonttools directly
        from fontTools.ttLib import TTFont

        font = TTFont(input_path)
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix=f'.{target_fmt}', delete=False
        )
        temp_out.close()
        font.save(temp_out.name)
        font.close()
        return {'success': True, 'output_path': temp_out.name}
    except ImportError:
        return {'success': False, 'error': 'fonttools library not installed'}
    except Exception as e:
        return {'success': False, 'error': str(e)}
