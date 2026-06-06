import os
import tempfile
import logging
logging.disable(logging.CRITICAL)

os.environ['U2NET_HOME'] = os.environ.get('U2NET_HOME', '/tmp/.u2net')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

CONVERSION_DIR = '/tmp/conversions'

def set_conversion_dir(path):
    global CONVERSION_DIR
    CONVERSION_DIR = path
    os.makedirs(CONVERSION_DIR, exist_ok=True)

def remove_background(input_path, output_format='png', model=None):
    model_name = model or os.environ.get('U2NET_MODEL', 'u2netp')

    import onnxruntime
    import numpy as np
    from PIL import Image
    import io

    model_path = _get_model(model_name)
    ort_session = onnxruntime.InferenceSession(model_path)

    img = Image.open(input_path).convert('RGB')
    orig_w, orig_h = img.size

    input_size = 320
    img_resized = img.resize((input_size, input_size), Image.LANCZOS)

    input_array = np.array(img_resized).astype(np.float32) / 255.0
    input_array = input_array.transpose(2, 0, 1)
    input_array = np.expand_dims(input_array, axis=0)

    ort_inputs = {ort_session.get_inputs()[0].name: input_array}
    ort_outputs = ort_session.run(None, ort_inputs)

    mask = ort_outputs[0][0, 0, :, :]
    mask = (mask * 255).astype(np.uint8)
    mask_img = Image.fromarray(mask, mode='L').resize((orig_w, orig_h), Image.LANCZOS)

    img.putalpha(mask_img)

    output_ext = '.png' if output_format != 'jpg' else '.jpg'
    if output_format == 'webp':
        output_ext = '.webp'
    if output_format == 'jpeg':
        output_ext = '.jpg'

    os.makedirs(CONVERSION_DIR, exist_ok=True)
    temp_output = tempfile.NamedTemporaryFile(
        dir=CONVERSION_DIR,
        suffix=output_ext,
        delete=False
    )
    output_path = temp_output.name
    temp_output.close()

    if output_format in ('jpg', 'jpeg'):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        bg.save(output_path, 'JPEG', quality=95)
    elif output_format == 'webp':
        bg = Image.new('RGBA', img.size, (255, 255, 255, 0))
        bg.paste(img, mask=img.split()[3])
        bg.save(output_path, 'WebP', quality=95)
    else:
        img.save(output_path, 'PNG')

    return output_path

def _get_model(model_name):
    import urllib.request

    cache_dir = os.environ['U2NET_HOME']
    os.makedirs(cache_dir, exist_ok=True)

    model_map = {
        'u2net': 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx',
        'u2netp': 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx',
    }
    url = model_map.get(model_name, model_map['u2netp'])
    local_path = os.path.join(cache_dir, f'{model_name}.onnx')

    if not os.path.exists(local_path):
        urllib.request.urlretrieve(url, local_path)

    return local_path
