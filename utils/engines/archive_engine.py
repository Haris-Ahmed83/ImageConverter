import os
import tempfile
import zipfile
import tarfile
import gzip
import bz2
import lzma
import shutil

def convert(input_path, source_fmt, target_fmt):
    if target_fmt == 'zip':
        return _to_zip(input_path, source_fmt)
    elif target_fmt in ('tar', 'gz', 'bz2', 'xz', '7z'):
        return _repackage(input_path, source_fmt, target_fmt)
    return _extract_all(input_path, source_fmt)

def _to_zip(input_path, source_fmt):
    extract_dir = _extract_to_dir(input_path, source_fmt)
    if not extract_dir:
        return {'success': False, 'error': 'Failed to extract archive'}

    temp_out = tempfile.NamedTemporaryFile(
        dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
        suffix='.zip', delete=False
    )
    temp_out.close()

    with zipfile.ZipFile(temp_out.name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(extract_dir):
            for f in files:
                fp = os.path.join(root, f)
                arcname = os.path.relpath(fp, extract_dir)
                zf.write(fp, arcname)

    shutil.rmtree(extract_dir, ignore_errors=True)
    return {'success': True, 'output_path': temp_out.name}

def _repackage(input_path, source_fmt, target_fmt):
    extract_dir = _extract_to_dir(input_path, source_fmt)
    if not extract_dir:
        return {'success': False, 'error': 'Failed to extract archive'}

    temp_out = tempfile.NamedTemporaryFile(
        dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
        suffix=f'.{target_fmt}', delete=False
    )
    temp_out.close()

    if target_fmt == 'tar':
        with tarfile.open(temp_out.name, 'w') as tf:
            tf.add(extract_dir, arcname='.')
    elif target_fmt == 'gz':
        with tarfile.open(temp_out.name, 'w:gz') as tf:
            tf.add(extract_dir, arcname='.')
    elif target_fmt == 'bz2':
        with tarfile.open(temp_out.name, 'w:bz2') as tf:
            tf.add(extract_dir, arcname='.')
    elif target_fmt == 'xz':
        with tarfile.open(temp_out.name, 'w:xz') as tf:
            tf.add(extract_dir, arcname='.')
    else:
        shutil.rmtree(extract_dir, ignore_errors=True)
        return {'success': False, 'error': f'Repackaging to {target_fmt} not supported'}

    shutil.rmtree(extract_dir, ignore_errors=True)
    return {'success': True, 'output_path': temp_out.name}

def _extract_all(input_path, source_fmt):
    extract_dir = _extract_to_dir(input_path, source_fmt)

    if source_fmt in ('zip', 'cbz'):
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix='.zip', delete=False
        )
    elif source_fmt in ('tar',):
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix='.tar', delete=False
        )
    elif source_fmt in ('gz', 'bz2', 'xz'):
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix=f'.{source_fmt}', delete=False
        )
    else:
        temp_out = tempfile.NamedTemporaryFile(
            dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
            suffix='.zip', delete=False
        )

    temp_out.close()
    shutil.rmtree(temp_out.name, ignore_errors=True)
    if extract_dir:
        shutil.move(extract_dir, temp_out.name)
    return {'success': True, 'output_path': temp_out.name}

def _extract_to_dir(input_path, source_fmt):
    extract_dir = tempfile.mkdtemp(dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'))

    try:
        if source_fmt in ('zip', 'cbz'):
            with zipfile.ZipFile(input_path, 'r') as zf:
                zf.extractall(extract_dir)
        elif source_fmt in ('tar',):
            with tarfile.open(input_path, 'r') as tf:
                tf.extractall(extract_dir)
        elif source_fmt in ('gz',):
            out = os.path.join(extract_dir, 'extracted')
            with gzip.open(input_path, 'rb') as f_in:
                with open(out, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        elif source_fmt in ('bz2',):
            out = os.path.join(extract_dir, 'extracted')
            with bz2.open(input_path, 'rb') as f_in:
                with open(out, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        elif source_fmt in ('xz', 'lzma'):
            out = os.path.join(extract_dir, 'extracted')
            with lzma.open(input_path, 'rb') as f_in:
                with open(out, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        else:
            shutil.rmtree(extract_dir, ignore_errors=True)
            return None
        return extract_dir
    except Exception:
        shutil.rmtree(extract_dir, ignore_errors=True)
        return None
