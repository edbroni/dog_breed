import cv2
import torch
import io
import os
import torch
import numpy as np
from fastai.vision.all import load_learner

def start_models():
	'''
	Initialize the models
	Inputs:
	Outputs: model - fastai model
	         face_cacasde - OpenCV model 
	'''
	
	# Initialize the ResNet50 model
	saved_model = './saved_models/fastai_ResNet50_dog_breed.pkl'
	model = load_learner(saved_model)

	# Initialize the opencv model
	face_cascade = cv2.CascadeClassifier('./saved_models/haarcascade_frontalface_alt.xml')

	return model, face_cascade


def dog_detector(img_path, model):
	'''
	Function to detect if an image contains a dog face, using the ResNet50
	Input: img_path - the image filename with path to analyze, string
	       model - fastai trained model
	Output: predict - label predicted - string
	        certainty - how good is the prediction in %- np float
	'''
	# method predict return the class, index of prediction and probabilities
	predict, predict_idx, outputs = model.predict(img_path)
	# Calculation in % of prediction of the class
	certainty = np.round(100*outputs[predict_idx].item(),2)

	return predict, certainty

def face_detector(img_path, face_model):
	'''
	Function to detect faces
	Input: img_path - the image filename with path to analyze, string
	       face_model - OpenCV trained model
	Output: True or false of detected faces - boolean
	'''
	# Open the image
	img = cv2.imread(img_path)
	# Preprocessing the image to gray scale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#Identify the faces
	faces = face_model.detectMultiScale(gray)
	return len(faces) > 0

def remove_images(folder):
	'''
	Remove old images from upload folder
	Input: folder - path to remove files - string
	Output:
	'''
	try:
		for file_delete in os.listdir(folder):
			os.remove(os.path.join(folder, file_delete))
	except:
		pass


def allowed_file(filename,allowed):
	'''
	Function to return true or false according file extension.
	Input: filename - filename to check extension - string
	       allowed - extension allowed - list of strings
	Output: True or false - boolean
	'''

	return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed
