document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const convertBtn = document.getElementById('convertBtn');
    const conversionStatus = document.getElementById('conversionStatus');
    const progressFill = document.getElementById('progressFill');
    const statusText = document.getElementById('statusText');
    const downloadArea = document.getElementById('downloadArea');
    const downloadBtn = document.getElementById('downloadBtn');
    const downloadTitle = document.getElementById('downloadTitle');
    const downloadFilename = document.getElementById('downloadFilename');
    const newConvertBtn = document.getElementById('newConvertBtn');
    const errorMsg = document.getElementById('errorMsg');
    const qualitySelect = document.getElementById('qualitySelect');
    const batchQueue = document.getElementById('batchQueue');
    const batchFileList = document.getElementById('batchFileList');
    const zipCheckbox = document.getElementById('zipDownload');
    const modeType = document.getElementById('modeType');
    const pageTitle = document.getElementById('pageTitle');
    const pageSubtitle = document.getElementById('pageSubtitle');
    const convertMode = document.getElementById('convertMode');
    const compressMode = document.getElementById('compressMode');
    const qualityGroup = document.getElementById('qualityGroup');
    const compressQuality = document.getElementById('compressQuality');
    const compressQualityValue = document.getElementById('compressQualityValue');
    const sizeComparison = document.getElementById('sizeComparison');
    const originalSize = document.getElementById('originalSize');
    const compressedSize = document.getElementById('compressedSize');
    const sizeSavings = document.getElementById('sizeSavings');
    const removeBgMode = document.getElementById('removeBgMode');

    let currentFiles = [];
    let currentMode = 'convert';

    // ── Mode Tabs ──
    document.querySelectorAll('.mode-tab').forEach(function(tab) {
        tab.addEventListener('click', function() {
            document.querySelectorAll('.mode-tab').forEach(function(t) { t.classList.remove('active'); });
            tab.classList.add('active');
            currentMode = tab.dataset.mode;
            modeType.value = currentMode;

            if (currentMode === 'convert') {
                convertMode.style.display = 'block';
                compressMode.style.display = 'none';
                removeBgMode.style.display = 'none';
                qualityGroup.style.display = 'flex';
                pageTitle.textContent = 'Convert your images online';
                pageSubtitle.textContent = 'CloudConvert converts your image files online. Amongst many others, we support PNG, JPG, GIF, WEBP and HEIC. You can use the options to control image resolution, quality and file size.';
                convertBtn.textContent = 'Convert';
                sizeComparison.style.display = 'none';
            } else if (currentMode === 'compress') {
                convertMode.style.display = 'none';
                compressMode.style.display = 'block';
                removeBgMode.style.display = 'none';
                qualityGroup.style.display = 'none';
                pageTitle.textContent = 'Compress your images online';
                pageSubtitle.textContent = 'Reduce image file size while keeping quality. Compress JPG, PNG, WebP, GIF and more. Fast, secure, no signup required.';
                convertBtn.textContent = 'Compress';
                sizeComparison.style.display = 'none';
            } else {
                convertMode.style.display = 'none';
                compressMode.style.display = 'none';
                removeBgMode.style.display = 'block';
                qualityGroup.style.display = 'none';
                pageTitle.textContent = 'Remove Image Background';
                pageSubtitle.textContent = 'AI-powered background removal. Upload any image and get a transparent background instantly. Fast, secure, no signup required.';
                convertBtn.textContent = 'Remove Background';
                sizeComparison.style.display = 'none';
            }
            resetConverter();
        });
    });

    // ── Compress Quality Slider ──
    if (compressQuality) {
        compressQuality.addEventListener('input', function() {
            compressQualityValue.textContent = this.value + '%';
        });
    }

    // ── Format Dropdown ──
    document.querySelectorAll('.format-selector').forEach(function(sel) {
        var trigger = sel.querySelector('.format-selector-trigger');
        var dropdown = sel.querySelector('.fs-dropdown');
        var labelEl = trigger.querySelector('.fs-label');
        var iconEl = trigger.querySelector('.fs-icon');

        // Ensure hidden input exists
        var hiddenInput = sel.querySelector('input[type="hidden"]');
        if (!hiddenInput) {
            hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            if (sel.classList.contains('source')) { hiddenInput.id = 'sourceFmt'; hiddenInput.name = 'source_format'; }
            else { hiddenInput.id = 'targetFmt'; hiddenInput.name = 'target_format'; }
            sel.appendChild(hiddenInput);
        }

        trigger.addEventListener('click', function(e) {
            e.stopPropagation();
            var isOpen = dropdown.classList.contains('open');
            closeAllDropdowns();
            if (!isOpen) {
                dropdown.classList.add('open');
                trigger.classList.add('open');
            }
        });

        // Event delegation for dynamic options
        dropdown.addEventListener('click', function(e) {
            var opt = e.target.closest('.fs-option');
            if (!opt) return;
            var value = opt.dataset.value;
            var label = opt.dataset.label;
            var color = opt.dataset.color;
            if (hiddenInput) hiddenInput.value = value;
            if (labelEl) labelEl.textContent = label;
            if (iconEl) { iconEl.textContent = label.substring(0, 4); iconEl.style.background = color; }
            dropdown.querySelectorAll('.fs-option').forEach(function(o) { o.classList.remove('selected'); });
            opt.classList.add('selected');
            dropdown.classList.remove('open');
            trigger.classList.remove('open');
        });
    });

    function closeAllDropdowns() {
        document.querySelectorAll('.fs-dropdown.open').forEach(function(d) {
            d.classList.remove('open');
            if (d.closest('.format-selector')) {
                d.closest('.format-selector').querySelector('.format-selector-trigger').classList.remove('open');
            }
        });
    }

    document.addEventListener('click', function() { closeAllDropdowns(); });

    // ── Swap ──
    var swapBtn = document.getElementById('swapBtn');
    if (swapBtn) {
        swapBtn.addEventListener('click', function() {
            var srcInput = document.getElementById('sourceFmt');
            var dstInput = document.getElementById('targetFmt');
            var temp = srcInput.value;
            srcInput.value = dstInput.value;
            dstInput.value = temp;
            syncDropdownFromInput('source');
            syncDropdownFromInput('target');
        });
    }

    function syncDropdownFromInput(side) {
        var input = document.getElementById(side + 'Fmt');
        var sel = document.querySelector('.format-selector.' + side);
        if (!sel || !input) return;
        var val = input.value;
        var opt = sel.querySelector('.fs-option[data-value="' + val + '"]');
        if (opt) {
            sel.querySelector('.fs-label').textContent = opt.dataset.label;
            sel.querySelector('.fs-icon').textContent = opt.dataset.label.substring(0, 4);
            sel.querySelector('.fs-icon').style.background = opt.dataset.color;
            sel.querySelectorAll('.fs-option').forEach(function(o) { o.classList.remove('selected'); });
            opt.classList.add('selected');
        }
    }

    // ── Upload ──
    if (uploadArea) {
        uploadArea.addEventListener('click', function(e) {
            if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'INPUT') {
                fileInput.click();
            }
        });

        uploadArea.addEventListener('dragover', function(e) {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', function(e) {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', function(e) {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            if (e.dataTransfer.files.length > 0) {
                handleFiles(e.dataTransfer.files);
            }
        });

        fileInput.addEventListener('change', function(e) {
            if (fileInput.files.length > 0) {
                handleFiles(fileInput.files);
            }
        });
    }

    function handleFiles(files) {
        currentFiles = Array.from(files);
        var h3 = document.querySelector('.upload-area h3');
        var p = document.querySelector('.upload-area p');
        var batchOpt = document.getElementById('batchModeOption');

        if (currentFiles.length === 1) {
            if (batchOpt) batchOpt.style.display = 'none';
            h3.textContent = currentFiles[0].name;
            p.textContent = (currentFiles[0].size / 1024 / 1024).toFixed(2) + ' MB (' + formatBytes(currentFiles[0].size) + ')';
            if (batchQueue) batchQueue.classList.remove('active');
            if (currentMode === 'compress' && sizeComparison) {
                originalSize.textContent = formatBytes(currentFiles[0].size);
                compressedSize.textContent = '-';
                sizeSavings.textContent = '';
            }
        } else {
            if (batchOpt) batchOpt.style.display = 'flex';
            h3.textContent = currentFiles.length + ' files selected';
            p.textContent = 'Click "Convert" to convert all files';
            if (batchFileList) renderBatchList();
            if (batchQueue) batchQueue.classList.add('active');
        }
        if (errorMsg) errorMsg.classList.remove('active');
        if (sizeComparison && currentMode !== 'compress') sizeComparison.style.display = 'none';
    }

    function formatBytes(bytes) {
        if (bytes < 1024) return bytes + ' B';
        if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / 1048576).toFixed(2) + ' MB';
    }

    function renderBatchList() {
        batchFileList.innerHTML = '';
        currentFiles.forEach(function(file, index) {
            var item = document.createElement('div');
            item.className = 'batch-file-item';
            item.id = 'bf-' + index;
            item.innerHTML =
                '<span class="file-name">' + escapeHtml(file.name) + '</span>' +
                '<span class="file-status pending" id="bs-' + index + '">Pending</span>';
            batchFileList.appendChild(item);
        });
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // ── Convert / Compress ──
    if (convertBtn) {
        convertBtn.addEventListener('click', function() {
            if (currentFiles.length === 0) {
                if (errorMsg) { errorMsg.textContent = 'Please select a file first'; errorMsg.classList.add('active'); }
                return;
            }
            if (errorMsg) errorMsg.classList.remove('active');

            if (currentMode === 'compress') {
                compressFiles();
            } else if (currentMode === 'removebg') {
                removeBgFiles();
            } else if (currentFiles.length === 1) {
                convertSingle(currentFiles[0]);
            } else {
                convertBatch();
            }
        });
    }

    function getTargetFormat() {
        var input = document.getElementById('targetFmt');
        return input ? input.value : 'jpg';
    }

    function convertSingle(file) {
        var targetFormat = getTargetFormat();
        var quality = qualitySelect ? qualitySelect.value : 85;

        conversionStatus.classList.add('active');
        if (downloadArea) downloadArea.classList.remove('active');
        convertBtn.disabled = true;
        convertBtn.textContent = 'Converting...';

        var formData = new FormData();
        formData.append('file', file);
        formData.append('target_format', targetFormat);
        formData.append('quality', quality);

        sendRequest('/convert', formData, function(resp) {
            if (resp.success) {
                setTimeout(function() {
                    conversionStatus.classList.remove('active');
                    if (downloadArea) { downloadArea.classList.add('active'); downloadTitle.textContent = 'Conversion successful!'; downloadFilename.textContent = resp.filename; downloadBtn.href = resp.download_url; }
                }, 400);
            } else { showError(resp.error || 'Conversion failed'); }
            convertBtn.disabled = false; convertBtn.textContent = 'Convert';
        });
    }

    function convertBatch() {
        var targetFormat = getTargetFormat();
        var quality = qualitySelect ? qualitySelect.value : 85;
        var asZip = zipCheckbox ? zipCheckbox.checked : true;

        convertBtn.disabled = true;
        convertBtn.textContent = 'Converting...';
        conversionStatus.classList.add('active');
        if (downloadArea) downloadArea.classList.remove('active');

        var formData = new FormData();
        for (var i = 0; i < currentFiles.length; i++) formData.append('files', currentFiles[i]);
        formData.append('target_format', targetFormat);
        formData.append('quality', quality);
        formData.append('as_zip', asZip ? '1' : '0');

        for (var j = 0; j < currentFiles.length; j++) {
            var el = document.getElementById('bs-' + j);
            if (el) { el.textContent = 'Queued'; el.className = 'file-status queued'; }
        }

        sendRequest('/convert/batch', formData, function(resp) {
            if (resp.success) {
                for (var k = 0; k < resp.results.length; k++) {
                    var el2 = document.getElementById('bs-' + k);
                    if (el2) {
                        if (resp.results[k].success) { el2.textContent = '✓ Done'; el2.className = 'file-status done'; }
                        else { el2.textContent = '✗ ' + (resp.results[k].error || 'Failed'); el2.className = 'file-status error'; }
                    }
                }
                setTimeout(function() {
                    conversionStatus.classList.remove('active');
                    if (downloadArea) {
                        downloadArea.classList.add('active');
                        downloadTitle.textContent = 'Conversion successful!';
                        if (resp.zip_url) { downloadFilename.textContent = 'converted_images.zip (' + resp.results.length + ' files)'; downloadBtn.href = resp.zip_url; }
                        else if (resp.results.length === 1 && resp.results[0].success) { downloadFilename.textContent = resp.results[0].filename; downloadBtn.href = resp.results[0].download_url; }
                    }
                }, 500);
            } else { showError(resp.error || 'Batch conversion failed'); }
            convertBtn.disabled = false; convertBtn.textContent = 'Convert';
        });
    }

    function removeBgFiles() {
        if (currentFiles.length === 0) return;

        convertBtn.disabled = true;
        convertBtn.textContent = 'Removing background...';
        conversionStatus.classList.add('active');
        if (downloadArea) downloadArea.classList.remove('active');
        if (sizeComparison) sizeComparison.style.display = 'none';

        var bgFormat = 'png';
        document.querySelectorAll('input[name="bgFormat"]').forEach(function(r) {
            if (r.checked) bgFormat = r.value;
        });

        if (currentFiles.length === 1) {
            var formData = new FormData();
            formData.append('file', currentFiles[0]);
            formData.append('format', bgFormat);

            sendRequest('/remove-bg', formData, function(resp) {
                if (resp.success) {
                    setTimeout(function() {
                        conversionStatus.classList.remove('active');
                        if (downloadArea) {
                            downloadArea.classList.add('active');
                            downloadTitle.textContent = 'Background removed!';
                            downloadFilename.textContent = resp.filename;
                            downloadBtn.href = resp.download_url;
                        }
                    }, 400);
                } else { showError(resp.error || 'Background removal failed'); }
                convertBtn.disabled = false; convertBtn.textContent = 'Remove Background';
            });
        } else {
            showError('Please process one file at a time for background removal');
            convertBtn.disabled = false; convertBtn.textContent = 'Remove Background';
        }
    }

    function compressFiles() {
        if (currentFiles.length === 0) return;

        convertBtn.disabled = true;
        convertBtn.textContent = 'Compressing...';
        conversionStatus.classList.add('active');
        if (downloadArea) downloadArea.classList.remove('active');
        if (sizeComparison) sizeComparison.style.display = 'none';

        var quality = compressQuality ? compressQuality.value : 80;

        if (currentFiles.length === 1) {
            var formData = new FormData();
            formData.append('file', currentFiles[0]);
            formData.append('quality', quality);

            sendRequest('/compress', formData, function(resp) {
                if (resp.success) {
                    if (sizeComparison) {
                        sizeComparison.style.display = 'flex';
                        originalSize.textContent = formatBytes(resp.original_size);
                        compressedSize.textContent = formatBytes(resp.compressed_size);
                        var savingsEl = document.getElementById('sizeSavings');
                        if (savingsEl) {
                            var sv = resp.savings;
                            savingsEl.textContent = (sv > 0 ? '-' : '') + Math.abs(sv).toFixed(1) + '%';
                            savingsEl.className = 'size-savings ' + (sv > 0 ? 'positive' : 'negative');
                        }
                    }
                    setTimeout(function() {
                        conversionStatus.classList.remove('active');
                        if (downloadArea) { downloadArea.classList.add('active'); downloadTitle.textContent = 'Compression complete!'; downloadFilename.textContent = resp.filename + ' — ' + (resp.savings > 0 ? resp.savings.toFixed(1) + '% smaller' : 'same size'); downloadBtn.href = resp.download_url; }
                    }, 400);
                } else { showError(resp.error || 'Compression failed'); }
                convertBtn.disabled = false; convertBtn.textContent = 'Compress';
            });
        } else {
            // Batch compress: convert each to same format with lower quality
            var targetFormat = 'jpg';
            var asZip = zipCheckbox ? zipCheckbox.checked : true;
            var formData = new FormData();
            for (var i = 0; i < currentFiles.length; i++) formData.append('files', currentFiles[i]);
            formData.append('target_format', targetFormat);
            formData.append('quality', quality);
            formData.append('as_zip', asZip ? '1' : '0');

            sendRequest('/convert/batch', formData, function(resp) {
                if (resp.success) {
                    for (var k = 0; k < resp.results.length; k++) {
                        var el2 = document.getElementById('bs-' + k);
                        if (el2) {
                            if (resp.results[k].success) { el2.textContent = '✓ Done'; el2.className = 'file-status done'; }
                            else { el2.textContent = '✗ ' + (resp.results[k].error || 'Failed'); el2.className = 'file-status error'; }
                        }
                    }
                    setTimeout(function() {
                        conversionStatus.classList.remove('active');
                        if (downloadArea) {
                            downloadArea.classList.add('active');
                            downloadTitle.textContent = 'Compression complete!';
                            if (resp.zip_url) { downloadFilename.textContent = 'compressed_images.zip (' + resp.results.length + ' files)'; downloadBtn.href = resp.zip_url; }
                        }
                    }, 500);
                } else { showError(resp.error || 'Compression failed'); }
                convertBtn.disabled = false; convertBtn.textContent = 'Compress';
            });
        }
    }

    function sendRequest(url, formData, onSuccess) {
        var xhr = new XMLHttpRequest();

        xhr.upload.onprogress = function(e) {
            if (e.lengthComputable) {
                var pct = Math.round((e.loaded / e.total) * 50);
                progressFill.style.width = pct + '%';
                statusText.textContent = 'Uploading... ' + pct + '%';
            }
        };

        xhr.onload = function() {
            if (xhr.status === 200) {
                try { onSuccess(JSON.parse(xhr.responseText)); }
                catch (e) { showError('Invalid response'); }
            } else {
                handleErrorResponse(xhr);
            }
        };

        xhr.onerror = function() { showError('Network error occurred'); };

        var progress = 10;
        var interval = setInterval(function() {
            if (progress < 90) { progress += Math.random() * 8; progressFill.style.width = Math.min(progress, 90) + '%'; statusText.textContent = 'Processing... ' + Math.round(Math.min(progress, 90)) + '%'; }
        }, 600);

        xhr.addEventListener('loadend', function() { clearInterval(interval); });
        xhr.open('POST', url, true);
        xhr.send(formData);
    }

    function handleErrorResponse(xhr) {
        try { var resp = JSON.parse(xhr.responseText); showError(resp.error || 'Server error (' + xhr.status + ')'); }
        catch (e) { showError('Server error (' + xhr.status + ')'); }
    }

    function getBtnLabel() {
        if (currentMode === 'compress') return 'Compress';
        if (currentMode === 'removebg') return 'Remove Background';
        return 'Convert';
    }

    function showError(msg) {
        if (errorMsg) { errorMsg.textContent = msg; errorMsg.classList.add('active'); }
        if (conversionStatus) conversionStatus.classList.remove('active');
        if (convertBtn) { convertBtn.disabled = false; convertBtn.textContent = getBtnLabel(); }
    }

    if (newConvertBtn) {
        newConvertBtn.addEventListener('click', function() { resetConverter(); });
    }

    function resetConverter() {
        currentFiles = [];
        if (fileInput) fileInput.value = '';
        if (conversionStatus) conversionStatus.classList.remove('active');
        if (downloadArea) downloadArea.classList.remove('active');
        if (batchQueue) batchQueue.classList.remove('active');
        if (errorMsg) errorMsg.classList.remove('active');
        if (progressFill) progressFill.style.width = '0%';
        if (statusText) statusText.textContent = '';
        if (sizeComparison) sizeComparison.style.display = 'none';
        var h3 = document.querySelector('.upload-area h3');
        var p = document.querySelector('.upload-area p');
        if (h3) h3.textContent = 'Select your file here to get started';
        if (p) p.textContent = 'or drop your file here.';
        if (convertBtn) { convertBtn.disabled = false; convertBtn.textContent = getBtnLabel(); }
    }
});
