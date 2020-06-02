import base64
import re
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
	image_filename = './storage/faces/face_' + datetime.now().strftime('%H%M%S%f') + '.jpg'
	image_b64 = request.values['image_data']
	img_str = re.search(r'data:image/png;base64,(.*)', image_b64).group(1)
	output = open(image_filename, 'wb')
	decoded = base64.b64decode(img_str)
	output.write(decoded)
	output.close()
	return image_filename


if __name__ == '__main__':
	app.run()
