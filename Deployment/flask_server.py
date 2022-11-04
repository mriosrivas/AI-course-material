from PIL import Image
import numpy as np
import tensorflow.lite as tflite
from io import BytesIO
from urllib import request as urllib_request

from flask import Flask
from flask import jsonify
from flask import request

app = Flask('image_classifier')

def download_image(url):
    with urllib_request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    img = img.resize((299, 299), Image.NEAREST)
    return img

#with Image.open('shorts.jpg') as img:
#    img = img.resize((299, 299), Image.NEAREST)

def preprocess_lite(X):
    return np.float32((X/127.5) - 1)


def load_model():
    # Load model to interpreter
    interpreter = tflite.Interpreter(model_path='xception.tflite')
    # Load weights
    interpreter.allocate_tensors()
    # Find input pointer
    input_index = interpreter.get_input_details()[0]['index']
    # Find output pointer
    output_index = interpreter.get_output_details()[0]['index']
    return interpreter, input_index, output_index

def run_model(interpreter, input_index, output_index, X):
    # Load data into input
    interpreter.set_tensor(input_index, X)
    # Run inference
    interpreter.invoke()
    # Load output into memory
    lite_pred = interpreter.get_tensor(output_index)
    return lite_pred

@app.route('/predict', methods=['POST'])
def predict():
    #url = 'https://i.postimg.cc/pX0LpQ4t/shorts.jpg'
    data = request.get_json()
    url = data['url']

    classes = ['dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']

    interpreter, input_index, output_index = load_model()

    img = download_image(url)

    X = preprocess_lite(np.array([np.array(img)]))

    lite_pred = run_model(interpreter, input_index, output_index, X)

    # print(dict(zip(classes, lite_pred[0])))

    strings = []
    for i in lite_pred[0]:
        strings.append(str(i))

    return jsonify(dict(zip(classes, strings)))


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9696)