from generate_inception_features import generate_features 
from train_nn import train_nn, get_classes
from run_classifier import predict

from keras.models import load_model

import os
from shutil import copy

"""
This is an example of how to use this tool.

Notice that since we are using a pre-trained model, only 42 images were used
for each category, with great results!

Look at the "demo_test_images_predictions" folder to see the results of this
classifier on unlabelled images.
"""


"""
images_dir should be a folder that is organized as such:

images_dir:
	class_0:
		img_0
		img_1
		...
	class_1:
		img_0
		img_1
		...
	...
"""
images_dir = 'demo_images/'
test_images_dir = 'unlabelLed_demo_images/'
test_images_predictions_dir = 'demo_test_images_predictions'
features_file = 'demo_features.txt'
model_file = 'demo_model.h5'

# Generates the features for all of the images using the
# Inception V3 model
generate_features(images_dir, features_file)

# Trains a one-layer neural network classifier for the features
train_nn(features_file, model_file, val_split=0.8, nb_epochs=40, optimizer='rmsprop')

# Ordered class labels
classes = get_classes(features_file)

# Load trained classifier

classifier = load_model(model_file)

for img in os.listdir(test_images_dir):
	if img[-3:].lower() != 'jpg' and img[-4:].lower() != 'jpeg':
		continue

	img_path = os.path.join(test_images_dir, img)

	# Generate the prediction for the unlabelled image
	prediction = predict(img_path, classifier)

	label = classes[prediction]

	dest = os.path.join(test_images_predictions_dir, label)

	if not os.path.isdir(dest):
		os.mkdir(dest)

	copy(img_path, dest)