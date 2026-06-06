const API_BASE = 'https://image-converter-lake.vercel.app';

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: 'convert-to-jpg',
    title: 'Convert to JPG',
    contexts: ['image']
  });
  chrome.contextMenus.create({
    id: 'convert-to-png',
    title: 'Convert to PNG',
    contexts: ['image']
  });
  chrome.contextMenus.create({
    id: 'convert-to-webp',
    title: 'Convert to WebP',
    contexts: ['image']
  });
  chrome.contextMenus.create({
    id: 'separator-1',
    type: 'separator',
    contexts: ['image']
  });
  chrome.contextMenus.create({
    id: 'compress-image',
    title: 'Compress Image',
    contexts: ['image']
  });
  chrome.contextMenus.create({
    id: 'remove-background',
    title: 'Remove Background',
    contexts: ['image']
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  const imageUrl = info.srcUrl;
  if (!imageUrl) return;

  switch (info.menuItemId) {
    case 'convert-to-jpg':
      processImage(imageUrl, 'jpg');
      break;
    case 'convert-to-png':
      processImage(imageUrl, 'png');
      break;
    case 'convert-to-webp':
      processImage(imageUrl, 'webp');
      break;
    case 'compress-image':
      compressImage(imageUrl);
      break;
    case 'remove-background':
      removeBg(imageUrl);
      break;
  }
});

async function processImage(imageUrl, targetFormat) {
  try {
    const blob = await fetch(imageUrl).then(r => r.blob());
    const formData = new FormData();
    formData.append('file', blob, 'image.' + (targetFormat === 'jpg' ? 'jpg' : targetFormat));
    formData.append('target_format', targetFormat);
    formData.append('quality', '85');

    const resp = await fetch(API_BASE + '/convert', {
      method: 'POST',
      body: formData
    });
    const data = await resp.json();

    if (data.success) {
      const downloadUrl = API_BASE + data.download_url;
      chrome.downloads.download({ url: downloadUrl, filename: 'converted.' + targetFormat });
    } else {
      alert('Conversion failed: ' + (data.error || 'Unknown error'));
    }
  } catch (err) {
    alert('Error: ' + err.message);
  }
}

async function compressImage(imageUrl) {
  try {
    const blob = await fetch(imageUrl).then(r => r.blob());
    const formData = new FormData();
    formData.append('file', blob, 'image.jpg');
    formData.append('quality', '60');

    const resp = await fetch(API_BASE + '/compress', {
      method: 'POST',
      body: formData
    });
    const data = await resp.json();

    if (data.success) {
      const downloadUrl = API_BASE + data.download_url;
      const savings = data.savings ? ' (' + data.savings.toFixed(1) + '% smaller)' : '';
      chrome.downloads.download({ url: downloadUrl, filename: 'compressed' + savings + '.jpg' });
    } else {
      alert('Compression failed: ' + (data.error || 'Unknown error'));
    }
  } catch (err) {
    alert('Error: ' + err.message);
  }
}

async function removeBg(imageUrl) {
  try {
    const blob = await fetch(imageUrl).then(r => r.blob());
    const formData = new FormData();
    formData.append('file', blob, 'image.png');
    formData.append('format', 'png');

    const resp = await fetch(API_BASE + '/remove-bg', {
      method: 'POST',
      body: formData
    });
    const data = await resp.json();

    if (data.success) {
      const downloadUrl = API_BASE + data.download_url;
      chrome.downloads.download({ url: downloadUrl, filename: 'no-background.png' });
    } else {
      alert('Background removal failed: ' + (data.error || 'Unknown error'));
    }
  } catch (err) {
    alert('Error: ' + err.message);
  }
}
