import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from detectors import dog_detector, face_detector, start_models
from detectors import allowed_file, remove_images

import io
import numpy as np

UPLOAD_FOLDER = './static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

allowed_ext = set(['png', 'jpg', 'jpeg', 'gif'])

resnet_model, face_model = start_models()


@app.route('/')
def upload_form():
	remove_images(app.config['UPLOAD_FOLDER'])
	return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
	remove_images(app.config['UPLOAD_FOLDER'])

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename,allowed_ext):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Image successfully uploaded and displayed below')
		img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		if face_detector(img_path,face_model):
			breed, sureness = dog_detector(img_path,resnet_model)
			message = "Human detected"
		else:
			breed, sureness = dog_detector(img_path,resnet_model)
			if sureness > 45:
				message = "Dog detected"
			else:
				message = "Neither human or dog detected"
				breed = ""
				sureness = 100 - sureness
		return render_template('index.html', filename=filename,message=message, breed=breed, sureness=sureness)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static',filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    app.run(debug=True)
