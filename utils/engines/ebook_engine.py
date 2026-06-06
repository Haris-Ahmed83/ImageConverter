import os
import tempfile
import zipfile
import xml.etree.ElementTree as ET

def convert(input_path, source_fmt, target_fmt):
    if source_fmt == 'epub' and target_fmt in ('txt', 'html', 'pdf', 'zip'):
        return _epub_to(input_path, target_fmt)
    elif target_fmt == 'epub':
        return _to_epub(input_path, source_fmt)
    return {'success': False, 'error': f'E-book conversion from {source_fmt} to {target_fmt} not supported'}

def _epub_to(input_path, target_fmt):
    import shutil

    extract_dir = tempfile.mkdtemp(dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'))
    try:
        with zipfile.ZipFile(input_path, 'r') as zf:
            zf.extractall(extract_dir)

        if target_fmt == 'txt':
            return _epub_to_txt(extract_dir)
        elif target_fmt == 'html':
            return _epub_to_html(extract_dir)
        elif target_fmt == 'zip':
            temp_out = tempfile.NamedTemporaryFile(
                dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
                suffix='.zip', delete=False
            )
            temp_out.close()
            shutil.make_archive(temp_out.name.replace('.zip', ''), 'zip', extract_dir)
            return {'success': True, 'output_path': temp_out.name + '.zip'}
        elif target_fmt == 'pdf':
            # Try using ebook-convert (calibre)
            import subprocess
            temp_out = tempfile.NamedTemporaryFile(
                dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
                suffix='.pdf', delete=False
            )
            temp_out.close()
            result = subprocess.run(
                ['ebook-convert', input_path, temp_out.name],
                capture_output=True, timeout=60
            )
            if result.returncode == 0:
                return {'success': True, 'output_path': temp_out.name}
    finally:
        shutil.rmtree(extract_dir, ignore_errors=True)
    return {'success': False, 'error': 'E-book conversion failed'}

def _epub_to_txt(extract_dir):
    import shutil
    # Find all XHTML/HTML files and extract text
    texts = []
    for root, dirs, files in os.walk(extract_dir):
        for f in files:
            if f.endswith(('.xhtml', '.html', '.htm')):
                fp = os.path.join(root, f)
                try:
                    tree = ET.parse(fp)
                    for elem in tree.iter():
                        if elem.text:
                            texts.append(elem.text.strip())
                        if elem.tail:
                            texts.append(elem.tail.strip())
                except:
                    pass

    temp_out = tempfile.NamedTemporaryFile(
        dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
        suffix='.txt', delete=False, mode='w', encoding='utf-8'
    )
    temp_out.write('\n\n'.join([t for t in texts if t]))
    temp_out.close()
    return {'success': True, 'output_path': temp_out.name}

def _epub_to_html(extract_dir):
    import shutil
    temp_out = tempfile.NamedTemporaryFile(
        dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
        suffix='.html', delete=False, mode='w', encoding='utf-8'
    )

    html_parts = ['<html><body>']
    for root, dirs, files in os.walk(extract_dir):
        for f in sorted(files):
            if f.endswith(('.xhtml', '.html', '.htm')):
                fp = os.path.join(root, f)
                try:
                    with open(fp, 'r', encoding='utf-8') as hf:
                        content = hf.read()
                    # Extract body content
                    import re
                    body = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    if body:
                        html_parts.append(body.group(1))
                except:
                    pass
    html_parts.append('</body></html>')

    temp_out.write('\n'.join(html_parts))
    temp_out.close()
    return {'success': True, 'output_path': temp_out.name}

def _to_epub(input_path, source_fmt):
    import shutil
    # For text/html to EPUB, create a minimal EPUB
    temp_out = tempfile.NamedTemporaryFile(
        dir=os.environ.get('CONVERSION_FOLDER', '/tmp/conversions'),
        suffix='.epub', delete=False
    )
    temp_out.close()

    # Try using calibre
    import subprocess
    result = subprocess.run(
        ['ebook-convert', input_path, temp_out.name],
        capture_output=True, timeout=60
    )
    if result.returncode == 0:
        return {'success': True, 'output_path': temp_out.name}

    # Fallback: create minimal EPUB manually
    try:
        _create_minimal_epub(input_path, source_fmt, temp_out.name)
        return {'success': True, 'output_path': temp_out.name}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def _create_minimal_epub(input_path, source_fmt, output_path):
    import shutil, uuid
    content = ''

    if source_fmt in ('txt',):
        with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        content = f'<p>{content.replace(chr(10), "</p><p>")}</p>'
    elif source_fmt in ('html', 'htm'):
        with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

    book_id = str(uuid.uuid4())
    work_dir = tempfile.mkdtemp()
    oebps = os.path.join(work_dir, 'OEBPS')
    meta_inf = os.path.join(work_dir, 'META-INF')
    os.makedirs(oebps)
    os.makedirs(meta_inf)

    with open(os.path.join(meta_inf, 'container.xml'), 'w') as f:
        f.write('<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')

    with open(os.path.join(oebps, 'content.opf'), 'w') as f:
        f.write(f'<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="2.0"><metadata><dc:identifier id="bookid">{book_id}</dc:identifier><dc:title>Converted Document</dc:title><dc:language>en</dc:language></metadata><manifest><item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/><item id="content" href="content.xhtml" media-type="application/xhtml+xml"/></manifest><spine toc="ncx"><itemref idref="content"/></spine></package>')

    with open(os.path.join(oebps, 'toc.ncx'), 'w') as f:
        f.write(f'<?xml version="1.0"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="{book_id}"/></head><docTitle><text>Converted Document</text></docTitle><navMap><navPoint id="p1"><navLabel><text>Page 1</text></navLabel><content src="content.xhtml"/></navPoint></navMap></ncx>')

    with open(os.path.join(oebps, 'content.xhtml'), 'w', encoding='utf-8') as f:
        f.write(f'<?xml version="1.0"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Converted Document</title></head><body>{content}</body></html>')

    shutil.make_archive(output_path.replace('.epub', ''), 'zip', work_dir)
    shutil.move(output_path.replace('.epub', '.zip'), output_path)
    shutil.rmtree(work_dir, ignore_errors=True)
