# 212+ formats across 11 categories (CloudConvert-compatible)
# Each format: (name, full_name, mime, ext, category, color, engine)

FORMATS_DATA = {
    # ─── DOCUMENTS (23) ───
    'abw':   ('AbiWord', 'AbiWord Document', 'application/x-abiword', '.abw', 'documents', '#4a90d9', 'document'),
    'djvu':  ('DjVu', 'DjVu Document', 'image/vnd.djvu', '.djvu', 'documents', '#2d7f3a', 'document'),
    'doc':   ('DOC', 'Microsoft Word Document', 'application/msword', '.doc', 'documents', '#2b579a', 'document'),
    'docm':  ('DOCM', 'Word Macro-Enabled Document', 'application/vnd.ms-word.document.macroEnabled.12', '.docm', 'documents', '#2b579a', 'document'),
    'docx':  ('DOCX', 'Microsoft Word Open XML Document', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx', 'documents', '#2b579a', 'document'),
    'dot':   ('DOT', 'Word Document Template', 'application/msword', '.dot', 'documents', '#2b579a', 'document'),
    'dotx':  ('DOTX', 'Word Open XML Document Template', 'application/vnd.openxmlformats-officedocument.wordprocessingml.template', '.dotx', 'documents', '#2b579a', 'document'),
    'html':  ('HTML', 'Hypertext Markup Language', 'text/html', '.html', 'documents', '#e44d26', 'document'),
    'hwp':   ('HWP', 'Hancom Word Document', 'application/x-hwp', '.hwp', 'documents', '#007396', 'document'),
    'hwpx':  ('HWPX', 'Hancom Word Open XML Document', 'application/x-hwp', '.hwpx', 'documents', '#007396', 'document'),
    'lwp':   ('LWP', 'Lotus Word Pro Document', 'application/vnd.lotus-wordpro', '.lwp', 'documents', '#0066cc', 'document'),
    'md':    ('MD', 'Markdown', 'text/markdown', '.md', 'documents', '#083fa1', 'document'),
    'odt':   ('ODT', 'OpenDocument Text', 'application/vnd.oasis.opendocument.text', '.odt', 'documents', '#7fba00', 'document'),
    'pages': ('PAGES', 'Apple Pages Document', 'application/vnd.apple.pages', '.pages', 'documents', '#e68533', 'document'),
    'pdf':   ('PDF', 'Portable Document Format', 'application/pdf', '.pdf', 'documents', '#b30b00', 'document'),
    'rst':   ('RST', 'reStructuredText', 'text/x-rst', '.rst', 'documents', '#1a6fc4', 'document'),
    'rtf':   ('RTF', 'Rich Text Format', 'application/rtf', '.rtf', 'documents', '#4169e1', 'document'),
    'sdw':   ('SDW', 'StarWriter Document', 'application/vnd.stardivision.writer', '.sdw', 'documents', '#ff8000', 'document'),
    'tex':   ('TeX', 'LaTeX Source Document', 'text/x-tex', '.tex', 'documents', '#3d6117', 'document'),
    'txt':   ('TXT', 'Plain Text', 'text/plain', '.txt', 'documents', '#4d4d4d', 'document'),
    'wpd':   ('WPD', 'WordPerfect Document', 'application/vnd.wordperfect', '.wpd', 'documents', '#e57a22', 'document'),
    'wps':   ('WPS', 'WPS Writer Document', 'application/vnd.wps-writer', '.wps', 'documents', '#365e9c', 'document'),
    'zabw':  ('ZAbw', 'AbiWord Compressed Document', 'application/x-zabw', '.zabw', 'documents', '#4a90d9', 'document'),

    # ─── IMAGES (42) ───
    'jpg':   ('JPG', 'Joint Photographic Experts Group', 'image/jpeg', '.jpg', 'images', '#e86c00', 'image'),
    'png':   ('PNG', 'Portable Network Graphics', 'image/png', '.png', 'images', '#5fb236', 'image'),
    'gif':   ('GIF', 'Graphics Interchange Format', 'image/gif', '.gif', 'images', '#d4419c', 'image'),
    'bmp':   ('BMP', 'Bitmap Image File', 'image/bmp', '.bmp', 'images', '#6b5b9e', 'image'),
    'tiff':  ('TIFF', 'Tagged Image File Format', 'image/tiff', '.tiff', 'images', '#8b4513', 'image'),
    'webp':  ('WebP', 'Web Picture Format', 'image/webp', '.webp', 'images', '#34a7c1', 'image'),
    'heic':  ('HEIC', 'High Efficiency Image File Format', 'image/heic', '.heic', 'images', '#4a90d9', 'image'),
    'heif':  ('HEIF', 'High Efficiency Image File Format', 'image/heif', '.heif', 'images', '#4a90d9', 'image'),
    'avif':  ('AVIF', 'AV1 Image File Format', 'image/avif', '.avif', 'images', '#00a3e0', 'image'),
    'svg':   ('SVG', 'Scalable Vector Graphics', 'image/svg+xml', '.svg', 'images', '#ffb13b', 'vector'),
    'ico':   ('ICO', 'Icon File Format', 'image/x-icon', '.ico', 'images', '#0078d7', 'image'),
    'psd':   ('PSD', 'Photoshop Document', 'image/vnd.adobe.photoshop', '.psd', 'images', '#001e36', 'image'),
    'psb':   ('PSB', 'Photoshop Large Document', 'image/vnd.adobe.photoshop', '.psb', 'images', '#001e36', 'image'),
    'ai':    ('AI', 'Adobe Illustrator', 'application/postscript', '.ai', 'images', '#ff9a00', 'vector'),
    'eps':   ('EPS', 'Encapsulated PostScript', 'application/postscript', '.eps', 'images', '#ff6600', 'vector'),
    'indd':  ('INDD', 'Adobe InDesign Document', 'application/x-indesign', '.indd', 'images', '#ff3366', 'document'),
    'xcf':   ('XCF', 'GIMP Image', 'image/x-xcf', '.xcf', 'images', '#5c5c5c', 'image'),
    'cr2':   ('CR2', 'Canon Raw Image', 'image/x-canon-cr2', '.cr2', 'images', '#0099ff', 'raw'),
    'cr3':   ('CR3', 'Canon Raw Image v3', 'image/x-canon-cr3', '.cr3', 'images', '#0099ff', 'raw'),
    'nef':   ('NEF', 'Nikon Raw Image', 'image/x-nikon-nef', '.nef', 'images', '#ffe100', 'raw'),
    'nrw':   ('NRW', 'Nikon Coolpix Raw Image', 'image/x-nikon-nrw', '.nrw', 'images', '#ffe100', 'raw'),
    'arw':   ('ARW', 'Sony Raw Image', 'image/x-sony-arw', '.arw', 'images', '#e60012', 'raw'),
    'dng':   ('DNG', 'Digital Negative', 'image/x-adobe-dng', '.dng', 'images', '#333333', 'raw'),
    'raf':   ('RAF', 'Fujifilm Raw Image', 'image/x-fujifilm-raf', '.raf', 'images', '#0080c5', 'raw'),
    'orf':   ('ORF', 'Olympus Raw Image', 'image/x-olympus-orf', '.orf', 'images', '#006699', 'raw'),
    'rw2':   ('RW2', 'Panasonic Raw Image', 'image/x-panasonic-rw2', '.rw2', 'images', '#00519e', 'raw'),
    'srw':   ('SRW', 'Samsung Raw Image', 'image/x-samsung-srw', '.srw', 'images', '#1428a0', 'raw'),
    'pef':   ('PEF', 'Pentax Raw Image', 'image/x-pentax-pef', '.pef', 'images', '#003366', 'raw'),
    '3fr':   ('3FR', 'Hasselblad Raw Image', 'image/x-hasselblad-3fr', '.3fr', 'images', '#000000', 'raw'),
    'erf':   ('ERF', 'Epson Raw Image', 'image/x-epson-erf', '.erf', 'images', '#003399', 'raw'),
    'mef':   ('MEF', 'Mamiya Raw Image', 'image/x-mamiya-mef', '.mef', 'images', '#cc0000', 'raw'),
    'kdc':   ('KDC', 'Kodak Raw Image', 'image/x-kodak-kdc', '.kdc', 'images', '#ffcc00', 'raw'),
    'dcr':   ('DCR', 'Kodak Digital Camera Raw', 'image/x-kodak-dcr', '.dcr', 'images', '#ffcc00', 'raw'),
    'mrw':   ('MRW', 'Minolta Raw Image', 'image/x-minolta-mrw', '.mrw', 'images', '#0099cc', 'raw'),
    'x3f':   ('X3F', 'Sigma Raw Image', 'image/x-sigma-x3f', '.x3f', 'images', '#003366', 'raw'),
    'fff':   ('FFF', 'Phase One Raw Image', 'image/x-phase-one-fff', '.fff', 'images', '#666666', 'raw'),
    'tga':   ('TGA', 'Truevision TGA', 'image/x-tga', '.tga', 'images', '#f60', 'image'),
    'pcx':   ('PCX', 'Paintbrush Bitmap', 'image/x-pcx', '.pcx', 'images', '#4a4a4a', 'image'),
    'pnm':   ('PNM', 'Portable Anymap', 'image/x-portable-anymap', '.pnm', 'images', '#6b6b6b', 'image'),
    'ppm':   ('PPM', 'Portable Pixmap', 'image/x-portable-pixmap', '.ppm', 'images', '#6b6b6b', 'image'),
    'pgm':   ('PGM', 'Portable Graymap', 'image/x-portable-graymap', '.pgm', 'images', '#6b6b6b', 'image'),
    'pbm':   ('PBM', 'Portable Bitmap', 'image/x-portable-bitmap', '.pbm', 'images', '#6b6b6b', 'image'),
    'xbm':   ('XBM', 'X BitMap', 'image/x-xbitmap', '.xbm', 'images', '#4a4a4a', 'image'),
    'dds':   ('DDS', 'DirectDraw Surface', 'image/vnd.ms-dds', '.dds', 'images', '#e6194b', 'image'),
    'sgi':   ('SGI', 'SGI Image File', 'image/x-sgi', '.sgi', 'images', '#999999', 'image'),
    'jp2':   ('JP2', 'JPEG 2000', 'image/jp2', '.jp2', 'images', '#e86c00', 'image'),
    'j2k':   ('J2K', 'JPEG 2000 Code Stream', 'image/j2k', '.j2k', 'images', '#e86c00', 'image'),
    'jxr':   ('JXR', 'JPEG XR', 'image/jxr', '.jxr', 'images', '#0078d7', 'image'),
    'pct':   ('PCT', 'Macintosh PICT', 'image/x-pict', '.pct', 'images', '#333333', 'image'),
    'pcd':   ('PCD', 'Kodak Photo CD', 'image/x-photo-cd', '.pcd', 'images', '#cc0000', 'image'),

    # ─── VIDEO (28) ───
    'mp4':   ('MP4', 'MPEG-4 Video', 'video/mp4', '.mp4', 'video', '#0099ff', 'video'),
    'mov':   ('MOV', 'Apple QuickTime Movie', 'video/quicktime', '.mov', 'video', '#333333', 'video'),
    'avi':   ('AVI', 'Audio Video Interleave', 'video/x-msvideo', '.avi', 'video', '#6b8e23', 'video'),
    'mkv':   ('MKV', 'Matroska Video', 'video/x-matroska', '.mkv', 'video', '#2b5b84', 'video'),
    'webm':  ('WebM', 'WebM Video', 'video/webm', '.webm', 'video', '#34a7c1', 'video'),
    'wmv':   ('WMV', 'Windows Media Video', 'video/x-ms-wmv', '.wmv', 'video', '#0078d7', 'video'),
    'flv':   ('FLV', 'Flash Video', 'video/x-flv', '.flv', 'video', '#e60012', 'video'),
    'mpeg':  ('MPEG', 'MPEG Video', 'video/mpeg', '.mpeg', 'video', '#666666', 'video'),
    'mpg':   ('MPG', 'MPEG Video', 'video/mpeg', '.mpg', 'video', '#666666', 'video'),
    '3gp':   ('3GP', '3GPP Multimedia', 'video/3gpp', '.3gp', 'video', '#009688', 'video'),
    '3g2':   ('3G2', '3GPP2 Multimedia', 'video/3gpp2', '.3g2', 'video', '#009688', 'video'),
    'm4v':   ('M4V', 'MPEG-4 Video', 'video/x-m4v', '.m4v', 'video', '#0099ff', 'video'),
    'ogv':   ('OGV', 'Ogg Video', 'video/ogg', '.ogv', 'video', '#000000', 'video'),
    'ts':    ('TS', 'MPEG Transport Stream', 'video/mp2t', '.ts', 'video', '#555555', 'video'),
    'mts':   ('MTS', 'AVCHD Video', 'video/mp2t', '.mts', 'video', '#e60012', 'video'),
    'm2ts':  ('M2TS', 'Blu-ray BDAV Video', 'video/mp2t', '.m2ts', 'video', '#1a237e', 'video'),
    'vob':   ('VOB', 'DVD Video Object', 'video/dvd', '.vob', 'video', '#ff8c00', 'video'),
    'divx':  ('DIVX', 'DivX Video', 'video/x-divx', '.divx', 'video', '#00a651', 'video'),
    'asf':   ('ASF', 'Advanced Systems Format', 'video/x-ms-asf', '.asf', 'video', '#0078d7', 'video'),
    'f4v':   ('F4V', 'Flash MP4 Video', 'video/x-f4v', '.f4v', 'video', '#e60012', 'video'),
    'rm':    ('RM', 'RealMedia', 'application/vnd.rn-realmedia', '.rm', 'video', '#cc0000', 'video'),
    'rmvb':  ('RMVB', 'RealMedia Variable Bitrate', 'application/vnd.rn-realmedia-vbr', '.rmvb', 'video', '#cc0000', 'video'),
    'mxf':   ('MXF', 'Material Exchange Format', 'application/mxf', '.mxf', 'video', '#333333', 'video'),
    'dv':    ('DV', 'Digital Video', 'video/x-dv', '.dv', 'video', '#4a4a4a', 'video'),
    'mpgv':  ('MPGV', 'MPEG-1 Video', 'video/mpeg', '.mpgv', 'video', '#666666', 'video'),
    'mpe':   ('MPE', 'MPEG Video', 'video/mpeg', '.mpe', 'video', '#666666', 'video'),
    'swf':   ('SWF', 'Shockwave Flash', 'application/x-shockwave-flash', '.swf', 'video', '#cc0000', 'video'),
    'wtv':   ('WTV', 'Windows Recorded TV', 'video/wtv', '.wtv', 'video', '#0078d7', 'video'),

    # ─── AUDIO (21) ───
    'mp3':   ('MP3', 'MPEG Audio Layer III', 'audio/mpeg', '.mp3', 'audio', '#e86c00', 'video'),
    'wav':   ('WAV', 'Waveform Audio', 'audio/wav', '.wav', 'audio', '#0099ff', 'video'),
    'flac':  ('FLAC', 'Free Lossless Audio Codec', 'audio/flac', '.flac', 'audio', '#4a4a4a', 'video'),
    'aac':   ('AAC', 'Advanced Audio Coding', 'audio/aac', '.aac', 'audio', '#660099', 'video'),
    'wma':   ('WMA', 'Windows Media Audio', 'audio/x-ms-wma', '.wma', 'audio', '#0078d7', 'video'),
    'm4a':   ('M4A', 'MPEG-4 Audio', 'audio/mp4', '.m4a', 'audio', '#0099ff', 'video'),
    'ogg':   ('OGG', 'Ogg Vorbis', 'audio/ogg', '.ogg', 'audio', '#000000', 'video'),
    'opus':  ('OPUS', 'Opus Audio', 'audio/opus', '.opus', 'audio', '#e86c00', 'video'),
    'aiff':  ('AIFF', 'Audio Interchange File Format', 'audio/x-aiff', '.aiff', 'audio', '#333333', 'video'),
    'alac':  ('ALAC', 'Apple Lossless Audio Codec', 'audio/mp4', '.alac', 'audio', '#999999', 'video'),
    'amr':   ('AMR', 'Adaptive Multi-Rate', 'audio/amr', '.amr', 'audio', '#009688', 'video'),
    'ac3':   ('AC3', 'Dolby Digital Audio', 'audio/ac3', '.ac3', 'audio', '#e60012', 'video'),
    'au':    ('AU', 'Sun Audio', 'audio/basic', '.au', 'audio', '#4a4a4a', 'video'),
    'ra':    ('RA', 'RealAudio', 'audio/vnd.rn-realaudio', '.ra', 'video', '#cc0000', 'video'),
    'voc':   ('VOC', 'Creative Voice File', 'audio/x-voc', '.voc', 'audio', '#4a4a4a', 'video'),
    'wv':    ('WV', 'WavPack Audio', 'audio/x-wavpack', '.wv', 'audio', '#4a4a4a', 'video'),
    'mid':   ('MID', 'MIDI Audio', 'audio/midi', '.mid', 'audio', '#336699', 'video'),
    'midi':  ('MIDI', 'MIDI Audio', 'audio/midi', '.midi', 'audio', '#336699', 'video'),
    'caf':   ('CAF', 'Core Audio Format', 'audio/x-caf', '.caf', 'audio', '#999999', 'video'),
    'dts':   ('DTS', 'Digital Theater Systems', 'audio/vnd.dts', '.dts', 'audio', '#cc0000', 'video'),
    'aifc':  ('AIFC', 'Compressed AIFF', 'audio/x-aiff', '.aifc', 'audio', '#333333', 'video'),

    # ─── SPREADSHEETS (8) ───
    'xls':   ('XLS', 'Microsoft Excel', 'application/vnd.ms-excel', '.xls', 'spreadsheets', '#217346', 'document'),
    'xlsx':  ('XLSX', 'Microsoft Excel Open XML', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx', 'spreadsheets', '#217346', 'document'),
    'xlsm':  ('XLSM', 'Excel Macro-Enabled Workbook', 'application/vnd.ms-excel.sheet.macroEnabled.12', '.xlsm', 'spreadsheets', '#217346', 'document'),
    'xlsb':  ('XLSB', 'Excel Binary Workbook', 'application/vnd.ms-excel.sheet.binary.macroEnabled.12', '.xlsb', 'spreadsheets', '#217346', 'document'),
    'ods':   ('ODS', 'OpenDocument Spreadsheet', 'application/vnd.oasis.opendocument.spreadsheet', '.ods', 'spreadsheets', '#7fba00', 'document'),
    'csv':   ('CSV', 'Comma-Separated Values', 'text/csv', '.csv', 'spreadsheets', '#4d4d4d', 'document'),
    'tsv':   ('TSV', 'Tab-Separated Values', 'text/tab-separated-values', '.tsv', 'spreadsheets', '#4d4d4d', 'document'),
    'numbers': ('NUMBERS', 'Apple Numbers', 'application/vnd.apple.numbers', '.numbers', 'spreadsheets', '#e68533', 'document'),

    # ─── SLIDES (11) ───
    'ppt':   ('PPT', 'Microsoft PowerPoint', 'application/vnd.ms-powerpoint', '.ppt', 'slides', '#d24726', 'document'),
    'pptx':  ('PPTX', 'PowerPoint Open XML', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx', 'slides', '#d24726', 'document'),
    'pptm':  ('PPTM', 'PowerPoint Macro-Enabled', 'application/vnd.ms-powerpoint.presentation.macroEnabled.12', '.pptm', 'slides', '#d24726', 'document'),
    'ppsx':  ('PPSX', 'PowerPoint Slideshow', 'application/vnd.openxmlformats-officedocument.presentationml.slideshow', '.ppsx', 'slides', '#d24726', 'document'),
    'pps':   ('PPS', 'PowerPoint Slideshow 97-2003', 'application/vnd.ms-powerpoint', '.pps', 'slides', '#d24726', 'document'),
    'odp':   ('ODP', 'OpenDocument Presentation', 'application/vnd.oasis.opendocument.presentation', '.odp', 'slides', '#7fba00', 'document'),
    'key':   ('KEY', 'Apple Keynote', 'application/vnd.apple.keynote', '.key', 'slides', '#e68533', 'document'),
    'potx':  ('POTX', 'PowerPoint Open XML Template', 'application/vnd.openxmlformats-officedocument.presentationml.template', '.potx', 'slides', '#d24726', 'document'),
    'pot':   ('POT', 'PowerPoint Template', 'application/vnd.ms-powerpoint', '.pot', 'slides', '#d24726', 'document'),
    'potm':  ('POTM', 'PowerPoint Macro-Enabled Template', 'application/vnd.ms-powerpoint.template.macroEnabled.12', '.potm', 'slides', '#d24726', 'document'),
    'fdf':   ('FDF', 'Forms Data Format', 'application/vnd.fdf', '.fdf', 'slides', '#b30b00', 'document'),

    # ─── E-BOOKS (22) ───
    'epub':  ('EPUB', 'Electronic Publication', 'application/epub+zip', '.epub', 'ebooks', '#6fb300', 'ebook'),
    'mobi':  ('MOBI', 'Mobipocket eBook', 'application/x-mobipocket-ebook', '.mobi', 'ebooks', '#e57a22', 'ebook'),
    'azw3':  ('AZW3', 'Kindle Format 8', 'application/vnd.amazon.mobi8-ebook', '.azw3', 'ebooks', '#ff9900', 'ebook'),
    'azw':   ('AZW', 'Kindle eBook', 'application/vnd.amazon.ebook', '.azw', 'ebooks', '#ff9900', 'ebook'),
    'fb2':   ('FB2', 'FictionBook', 'application/x-fictionbook+xml', '.fb2', 'ebooks', '#4a4a4a', 'ebook'),
    'lit':   ('LIT', 'Microsoft Reader eBook', 'application/x-ms-reader', '.lit', 'ebooks', '#0078d7', 'ebook'),
    'lrf':   ('LRF', 'Sony Portable Reader', 'application/x-sony-bbeb', '.lrf', 'ebooks', '#006699', 'ebook'),
    'pdb':   ('PDB', 'Palm Database eBook', 'application/vnd.palm', '.pdb', 'ebooks', '#333333', 'ebook'),
    'prc':   ('PRC', 'Palm Resource eBook', 'application/x-mobipocket-ebook', '.prc', 'ebooks', '#333333', 'ebook'),
    'snb':   ('SNB', 'Samsung Notebook', 'application/x-samsung-snb', '.snb', 'ebooks', '#1428a0', 'ebook'),
    'tcr':   ('TCR', 'TCR eBook', 'application/x-tcr', '.tcr', 'ebooks', '#555555', 'ebook'),
    'tpz':   ('TPZ', 'Kindle Topaz eBook', 'application/vnd.amazon.ebook', '.tpz', 'ebooks', '#ff9900', 'ebook'),
    'cbr':   ('CBR', 'Comic Book Archive (RAR)', 'application/vnd.comicbook-rar', '.cbr', 'ebooks', '#e60012', 'archive'),
    'cbz':   ('CBZ', 'Comic Book Archive (ZIP)', 'application/vnd.comicbook+zip', '.cbz', 'ebooks', '#0099ff', 'archive'),
    'cb7':   ('CB7', 'Comic Book Archive (7z)', 'application/x-cb7', '.cb7', 'ebooks', '#009900', 'archive'),
    'cbt':   ('CBT', 'Comic Book Archive (TAR)', 'application/x-cbt', '.cbt', 'ebooks', '#663300', 'archive'),
    'chm':   ('CHM', 'Microsoft Compiled HTML Help', 'application/vnd.ms-htmlhelp', '.chm', 'ebooks', '#0078d7', 'ebook'),
    'pml':   ('PML', 'Palm Markup Language', 'application/x-palm-pml', '.pml', 'ebooks', '#333333', 'ebook'),
    'djvu':  ('DJVU', 'DjVu eBook', 'image/vnd.djvu', '.djvu', 'ebooks', '#2d7f3a', 'document'),
    'htmlz': ('HTMLZ', 'Compressed HTML eBook', 'application/x-htmlz', '.htmlz', 'ebooks', '#e44d26', 'ebook'),
    'pdf':   ('PDFE', 'PDF eBook', 'application/pdf', '.pdf', 'ebooks', '#b30b00', 'document'),
    'txt':   ('TXTE', 'Text eBook', 'text/plain', '.txt', 'ebooks', '#4d4d4d', 'document'),
    # Note: some formats overlap with other categories. The engine handles it.

    # ─── ARCHIVES (39) ───
    'zip':   ('ZIP', 'ZIP Archive', 'application/zip', '.zip', 'archives', '#4a90d9', 'archive'),
    'tar':   ('TAR', 'Tape Archive', 'application/x-tar', '.tar', 'archives', '#333333', 'archive'),
    'gz':    ('GZ', 'GZIP Compressed', 'application/gzip', '.gz', 'archives', '#e44d26', 'archive'),
    'bz2':   ('BZ2', 'BZIP2 Compressed', 'application/x-bzip2', '.bz2', 'archives', '#6b8e23', 'archive'),
    'xz':    ('XZ', 'XZ Compressed', 'application/x-xz', '.xz', 'archives', '#2b5b84', 'archive'),
    '7z':    ('7Z', '7-Zip Archive', 'application/x-7z-compressed', '.7z', 'archives', '#009900', 'archive'),
    'rar':   ('RAR', 'RAR Archive', 'application/vnd.rar', '.rar', 'archives', '#006699', 'archive'),
    'z':     ('Z', 'Unix Compressed', 'application/x-compress', '.Z', 'archives', '#555555', 'archive'),
    'lz':    ('LZ', 'LZIP Compressed', 'application/x-lzip', '.lz', 'archives', '#555555', 'archive'),
    'lzma':  ('LZMA', 'LZMA Compressed', 'application/x-lzma', '.lzma', 'archives', '#555555', 'archive'),
    'cab':   ('CAB', 'Cabinet Archive', 'application/vnd.ms-cab-compressed', '.cab', 'archives', '#0078d7', 'archive'),
    'arj':   ('ARJ', 'ARJ Archive', 'application/x-arj', '.arj', 'archives', '#4a4a4a', 'archive'),
    'iso':   ('ISO', 'ISO Disk Image', 'application/x-iso9660-image', '.iso', 'archives', '#555555', 'archive'),
    'ace':   ('ACE', 'ACE Archive', 'application/x-ace-compressed', '.ace', 'archives', '#666666', 'archive'),
    'uue':   ('UUE', 'UUEncoded Archive', 'application/x-uuencoded', '.uue', 'archives', '#777777', 'archive'),
    'bhx':   ('BHX', 'BinHex Archive', 'application/x-binhex', '.bhx', 'archives', '#777777', 'archive'),
    'hqx':   ('HQX', 'MacBinHex Archive', 'application/mac-binhex40', '.hqx', 'archives', '#777777', 'archive'),
    'sit':   ('SIT', 'StuffIt Archive', 'application/x-stuffit', '.sit', 'archives', '#cc0000', 'archive'),
    'sitx':  ('SITX', 'StuffIt X Archive', 'application/x-stuffitx', '.sitx', 'archives', '#cc0000', 'archive'),
    'dmg':   ('DMG', 'Apple Disk Image', 'application/x-apple-diskimage', '.dmg', 'archives', '#999999', 'archive'),
    'mdf':   ('MDF', 'Media Descriptor File', 'application/x-iso9660-image', '.mdf', 'archives', '#555555', 'archive'),
    'isz':   ('ISZ', 'Compressed ISO Image', 'application/x-isz', '.isz', 'archives', '#555555', 'archive'),
    'nrg':   ('NRG', 'Nero Disc Image', 'application/x-nrg', '.nrg', 'archives', '#e60012', 'archive'),
    'img':   ('IMG', 'Raw Disk Image', 'application/x-raw-disk-image', '.img', 'archives', '#555555', 'archive'),
    'cso':   ('CSO', 'Compressed ISO', 'application/x-cso', '.cso', 'archives', '#555555', 'archive'),
    'dax':   ('DAX', 'DAX Compressed ISO', 'application/x-dax', '.dax', 'archives', '#555555', 'archive'),
    'vhd':   ('VHD', 'Virtual Hard Disk', 'application/x-vhd', '.vhd', 'archives', '#0078d7', 'archive'),
    'vmdk':  ('VMDK', 'Virtual Machine Disk', 'application/x-vmdk', '.vmdk', 'archives', '#ff6600', 'archive'),
    'vdi':   ('VDI', 'VirtualBox Disk Image', 'application/x-vdi', '.vdi', 'archives', '#006699', 'archive'),
    'qcow':  ('QCOW', 'QEMU Copy-On-Write', 'application/x-qcow', '.qcow', 'archives', '#333333', 'archive'),
    'qcow2': ('QCOW2', 'QEMU Copy-On-Write v2', 'application/x-qcow2', '.qcow2', 'archives', '#333333', 'archive'),
    'cpt':   ('CPT', 'Compact Pro Archive', 'application/x-cpt', '.cpt', 'archives', '#666666', 'archive'),
    'sea':   ('SEA', 'Self-Extracting Archive', 'application/x-sea', '.sea', 'archives', '#666666', 'archive'),
    'lha':   ('LHA', 'LHA Compressed Archive', 'application/x-lha', '.lha', 'archives', '#555555', 'archive'),
    'lzh':   ('LZH', 'LZH Compressed Archive', 'application/x-lzh', '.lzh', 'archives', '#555555', 'archive'),
    'bh':    ('BH', 'BlakHole Archive', 'application/x-blakhole', '.bh', 'archives', '#444444', 'archive'),
    'zst':   ('ZST', 'Zstandard Compressed', 'application/zstd', '.zst', 'archives', '#e44d26', 'archive'),
    'br':    ('BR', 'Brotli Compressed', 'application/x-brotli', '.br', 'archives', '#333333', 'archive'),
    'lz4':   ('LZ4', 'LZ4 Compressed', 'application/x-lz4', '.lz4', 'archives', '#555555', 'archive'),

    # ─── VECTOR (10) ───
    'svg':   ('SVGV', 'Scalable Vector Graphics', 'image/svg+xml', '.svg', 'vector', '#ffb13b', 'vector'),
    'ai':    ('AIV', 'Adobe Illustrator', 'application/postscript', '.ai', 'vector', '#ff9a00', 'vector'),
    'eps':   ('EPSV', 'Encapsulated PostScript', 'application/postscript', '.eps', 'vector', '#ff6600', 'vector'),
    'emf':   ('EMF', 'Enhanced Metafile', 'image/x-emf', '.emf', 'vector', '#0078d7', 'vector'),
    'wmf':   ('WMF', 'Windows Metafile', 'image/x-wmf', '.wmf', 'vector', '#0078d7', 'vector'),
    'cdr':   ('CDR', 'CorelDRAW', 'image/x-coreldraw', '.cdr', 'vector', '#2b5b84', 'vector'),
    'cgm':   ('CGM', 'Computer Graphics Metafile', 'image/cgm', '.cgm', 'vector', '#666666', 'vector'),
    'dxf':   ('DXF', 'Drawing Exchange Format', 'image/vnd.dxf', '.dxf', 'vector', '#cc0000', 'cad'),
    'hpgl':  ('HPGL', 'Hewlett-Packard Graphics Language', 'application/x-hpgl', '.hpgl', 'vector', '#009688', 'vector'),
    'plt':   ('PLT', 'HPGL Plot File', 'application/x-plotter', '.plt', 'vector', '#009688', 'vector'),

    # ─── CAD (3) ───
    'dwg':   ('DWG', 'AutoCAD Drawing', 'image/vnd.dwg', '.dwg', 'cad', '#cc0000', 'cad'),
    'dxf':   ('DXF', 'Drawing Exchange Format', 'image/vnd.dxf', '.dxf', 'cad', '#cc0000', 'cad'),
    'dwf':   ('DWF', 'Design Web Format', 'application/vnd.autodesk.dwf', '.dwf', 'cad', '#0099cc', 'cad'),

    # ─── FONTS (5) ───
    'ttf':   ('TTF', 'TrueType Font', 'font/ttf', '.ttf', 'fonts', '#4a4a4a', 'font'),
    'otf':   ('OTF', 'OpenType Font', 'font/otf', '.otf', 'fonts', '#4a4a4a', 'font'),
    'woff':  ('WOFF', 'Web Open Font Format', 'font/woff', '.woff', 'fonts', '#4a90d9', 'font'),
    'woff2': ('WOFF2', 'Web Open Font Format 2', 'font/woff2', '.woff2', 'fonts', '#4a90d9', 'font'),
    'eot':   ('EOT', 'Embedded OpenType', 'application/vnd.ms-fontobject', '.eot', 'fonts', '#0078d7', 'font'),
}

# Build FORMATS dict with full metadata (for backward compatibility)
FORMATS = {}
for key, (name, full, mime, ext, cat, color, engine) in FORMATS_DATA.items():
    FORMATS[key] = {
        'name': name,
        'full_name': full,
        'description': '',
        'mime': mime,
        'extensions': [ext],
        'category': cat,
        'color': color,
        'engine': engine,
    }

# Category display info
CATEGORIES = [
    {'id': 'documents', 'name': 'Documents', 'icon': '📄', 'count': 23},
    {'id': 'images', 'name': 'Images', 'icon': '🖼️', 'count': 42},
    {'id': 'video', 'name': 'Video', 'icon': '🎬', 'count': 28},
    {'id': 'audio', 'name': 'Audio', 'icon': '🎵', 'count': 21},
    {'id': 'spreadsheets', 'name': 'Spreadsheets', 'icon': '📊', 'count': 8},
    {'id': 'slides', 'name': 'Slides', 'icon': '📽️', 'count': 11},
    {'id': 'ebooks', 'name': 'E-books', 'icon': '📚', 'count': 22},
    {'id': 'archives', 'name': 'Archives', 'icon': '🗜️', 'count': 39},
    {'id': 'vector', 'name': 'Vector', 'icon': '📐', 'count': 10},
    {'id': 'cad', 'name': 'CAD', 'icon': '🏗️', 'count': 3},
    {'id': 'fonts', 'name': 'Fonts', 'icon': '🔤', 'count': 5},
]

def get_formats_by_category(cat_id):
    return {k: v for k, v in FORMATS.items() if v['category'] == cat_id}

def get_format_info(fmt):
    fmt = fmt.lower().replace('jpeg', 'jpg').replace('tif', 'tiff').replace('heif', 'heic')
    if fmt == 'svgv': fmt = 'svg'
    if fmt == 'aiv' or fmt == 'eps': pass  # handled by key
    if fmt == 'txte': fmt = 'txt'
    if fmt == 'pdfe': fmt = 'pdf'
    # Handle 'raw' as generic camera raw
    if fmt == 'raw':
        return FORMATS.get('dng', FORMATS.get('cr2'))
    return FORMATS.get(fmt)

def get_extension(fmt):
    info = get_format_info(fmt)
    if info:
        return info['extensions'][0]
    return f'.{fmt}'

def get_slug(src, dst):
    src = src.replace('jpg', 'jpeg') if src == 'jpg' else src
    dst = dst.replace('jpg', 'jpeg') if dst == 'jpg' else dst
    return f"{src}-to-{dst}"

OUTPUT_FORMATS = sorted(FORMATS.keys())
INPUT_FORMATS = sorted(FORMATS.keys())
