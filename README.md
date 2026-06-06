# ImageConverter

> Convert 200+ file formats — images, documents, video, audio, archives, fonts, and more. Free, fast, no signup.

![Python](https://img.shields.io/badge/python-3.12-blue) ![Flask](https://img.shields.io/badge/flask-3.1-green) ![License](https://img.shields.io/badge/license-MIT-lightgrey) ![Vercel](https://img.shields.io/badge/deployed%20on-Vercel-black)

ImageConverter is a full-featured file conversion web application inspired by CloudConvert. It supports **212 formats across 11 categories** — from everyday images to niche document, video, audio, archive, font, and CAD formats.

## Features

- **Convert** — Any format to any format (212 formats supported)
- **Compress** — Reduce file size while controlling quality
- **Remove Background** — AI-powered background removal (U²-Net ONNX)
- **Batch Processing** — Convert multiple files at once, download as ZIP
- **Browser Extension** — Right-click any image → convert, compress, or remove BG
- **SEO-Optimized Pages** — Individual `/format-to-format` pages for every pair

## Supported Formats (212 total)

| Category | Count | Examples |
|----------|-------|---------|
| Documents | 23 | PDF, DOCX, DOC, TXT, RTF, HTML, MD, ODT, TeX |
| Images | 42 | JPG, PNG, WebP, HEIC, AVIF, PSD, RAW (CR2, NEF, ARW, DNG...) |
| Video | 28 | MP4, MOV, AVI, MKV, WebM, WMV, FLV, 3GP, VOB |
| Audio | 21 | MP3, WAV, FLAC, AAC, OGG, OPUS, MIDI |
| Spreadsheets | 8 | XLS, XLSX, ODS, CSV, TSV |
| Slides | 11 | PPT, PPTX, ODP, KEY, PPSX |
| E-books | 22 | EPUB, MOBI, AZW3, FB2, CBR, CBZ |
| Archives | 39 | ZIP, TAR, GZ, BZ2, XZ, 7Z, RAR, ISO, DMG |
| Vector | 10 | SVG, AI, EPS, EMF, WMF, CDR |
| CAD | 3 | DWG, DXF, DWF |
| Fonts | 5 | TTF, OTF, WOFF, WOFF2, EOT |

## Tech Stack

- **Backend:** Python 3.12, Flask 3.1
- **Image Engine:** Pillow 12 + pillow-heif + rawpy
- **Document Engine:** LibreOffice (used server-side)
- **Media Engine:** FFmpeg (video/audio)
- **AI:** ONNX Runtime — U²-Net for background removal
- **Fonts:** fonttools
- **Frontend:** Vanilla JS, CSS (CloudConvert-style UI)
- **Deployment:** Vercel (serverless)

## Quick Start

```bash
# Clone
git clone https://github.com/yourusername/image-converter.git
cd image-converter

# Install dependencies
pip install -r requirements.txt

# Run
python app.py

# Open http://localhost:5000
```

### Production Dependencies

For full conversion support (video, audio, documents, CAD), install system packages:

```bash
# Ubuntu/Debian
sudo apt install ffmpeg libreoffice-core libreoffice-writer \
  libreoffice-calc libreoffice-impress ghostscript imagemagick

# macOS
brew install ffmpeg libreoffice ghostscript imagemagick
```

## Project Structure

```
.
├── app.py                    # Flask application (all routes)
├── requirements.txt          # Python dependencies
├── vercel.json               # Vercel deployment config
├── api/
│   └── index.py              # Vercel serverless entrypoint
├── utils/
│   ├── formatter.py          # 212 format definitions & metadata
│   ├── converter.py          # Conversion dispatcher
│   ├── bgremover.py          # ONNX background removal
│   └── engines/
│       ├── image_engine.py   # Pillow-based image conversion
│       ├── raw_engine.py     # Raw camera format processor
│       ├── archive_engine.py # ZIP/TAR/GZ/BZ2/XZ handler
│       ├── font_engine.py    # fonttools wrapper
│       ├── vector_engine.py  # Vector graphics rasterizer
│       ├── ebook_engine.py   # EPUB processor
│       └── __init__.py       # Engine dispatcher
├── templates/
│   ├── base.html             # Layout (CloudConvert-style header/footer)
│   ├── index.html            # Home page with all categories
│   ├── convert.html          # Individual format pair pages
│   ├── formats_index.html    # Full format catalog
│   ├── api.html              # API documentation
│   ├── pricing.html          # Pricing page
│   ├── login.html            # Sign in (UI placeholder)
│   └── register.html         # Sign up (UI placeholder)
├── static/
│   ├── css/style.css         # Complete CSS
│   └── js/main.js            # Client-side logic
└── extension/                # Chrome browser extension
    ├── manifest.json
    ├── background.js
    ├── popup.html
    └── icon*.png
```

## API

```bash
curl -X POST https://your-domain.com/convert \
  -F "file=@image.heic" \
  -F "target_format=jpg" \
  -F "quality=90"
```

Endpoints: `POST /convert`, `POST /convert/batch`, `POST /compress`, `POST /remove-bg`

## Browser Extension

Load `extension/` folder in `chrome://extensions` (Developer mode) to get right-click image conversion.

## License

MIT
