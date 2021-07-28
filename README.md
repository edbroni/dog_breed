# Dog Breed classification

## Table of contents
1. [Motivation](#motivation)
2. [Dependencies](#dependencies)
3. [Files description](#files)
4. [Installing](#install)
5. [Executing](#execute)
6. [Licensing](#license)


<a name="motivation"></a>
## 1 - Motivation

This is a project for Udacity NanoDegree to deploy an app performing the following
 tasks:
	-Identify human face, dog or none in an image;
	-If human face, predict a breed of dog;
	-If a dog, predict its breed;
	-Give an alert otherwise.

The final app is at: [Dog breed classification](frozen-plateau-36191.herokuapp.com)

<a name="dependencies"></a>
## 2 - Dependencies

The python notebook were tested with python3 an the main libraries are:<br>

	-Keras
	-TensorFlow
	-Pytorch
	-FastAi
	-Numpy

To complet list consult requirements.txt

<a name="files"></a>
## 3 - Files description

    * dog_breed.ipynb - Jupyter notebook
    * flask_app
        * app.py - file to start the flask app
        * detectors.py - file with python functions
        * Procfile - necessary to deploy with Heroku
        * requirements.txt - necessary libraries to run the app
            * saved_models
                * fastai_ResNet50_dog_breed.pkl - model to predict dog - transfer learning
                * weights.best.transfer_learning_Resnet50.hdf5 - model to predict dog - transfer learning
                * weights.best.from_scratch.hdf5 - model to detect dog - pre trained with imagenet dataset
                * weights.best.VGG16.hdf5 - model pre trained with imagenet dataset
                * haarcascade_frontalface_alt.xml - model to detect faces - from OpenCV
            * static
                * uploads - folder to save the images
            * templates - folder to store the html file
                * index.html - html file
    * haarcascades
        * haarcascade_frontalface_alt.xml - model to detect faces - from OpenCV
        * haarcascade_frontalface_alt2.xml - model to detect faces - from OpenCV
        * haarcascade_frontalface_default.xml - model to detect faces - from OpenCV
    * LICENSE licesing of this files, except OpenCV files
    * README.md this readme file
        

<a name="install"></a>
## 4 - Installing

Clone the repository<br>

	git clone https://github.com/edbroni/dog_breed

<a name="execute"></a>
## 5 - Executing

To execute the Jupyter notebook (command line):
    jupyter notebook dog_breed.ipynb

To execute online at [Google Colab](colab.research.google.com): 
Open a jupyter notebook session and open the file dog_breed.ipynb.

To execute the app (command line):
    cd flask_app
    python3 app.py

<a name="license"></a>
## 6 - Licensing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br>
This project is licensed under MIT License - see [License](LICENSE) for details

