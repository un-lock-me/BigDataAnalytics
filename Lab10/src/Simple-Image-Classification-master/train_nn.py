from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.metrics import confusion_matrix
import numpy as np

"""
Returns a sorted list of all the classes contained in 'features_file'
"""
def get_classes(features_file):
	classes = set()

	with open(features_file, 'r') as f:
		line = f.readline()

		while len(line) > 0:
			class_label = line.split(',')[0]
			classes.add(class_label)

			line = f.readline()

	return sorted(list(classes))

"""
Returns the feature vectors and the corresponding labels contained in 'features_file'
"""
def get_data(classes, features_file):
	x = []
	y = []

	with open(features_file, 'r') as f:
		for line in f:
			parts = line.split(',')

			class_index = classes.index(parts[0])

			y_val = np.zeros(len(classes))
			y_val[class_index] = 1

			# One-hot feature vector represting the corresponding class label
			y.append(y_val)

			x.append([float(v) for v in parts[1:]])

	return np.array(x), np.array(y)

"""
Trains a one-layer neural network to classify the features generated from the 
Inception model.
"""
def train_nn(features_file, model_file, val_split=0.8, nb_epochs=50, optimizer='rmsprop'):
	classes = get_classes(features_file)

	print "Classes are: %s" % str(classes)

	print "Loading training data..."

	num_classes = len(classes)

	x,y = get_data(classes, features_file)

	# Shuffle data
	randomize = np.arange(len(x))
	np.random.shuffle(randomize)
	x = x[randomize]
	y = y[randomize]

	# Split data into training and validation data
	cutoff = int(len(x) * val_split)

	train_x = x[:cutoff]
	train_y = y[:cutoff]

	val_x = x[cutoff:]
	val_y = y[cutoff:]

	print "Finished loading training data"

	print "Compiling model"

	# Build model
	model = Sequential()

	model.add(Dense(num_classes, input_dim=2048))
	model.add(Activation('softmax'))

	# Compile model
	model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

	print "Finished compiling model"

	print "Training classifier..."

	# Start training model
	model.fit(train_x, train_y, nb_epoch=nb_epochs, verbose=1)

	print "Finished training classifier."

	# Save model
	model.save(model_file)

	# Generate predictions for validation data
	pred_y = [np.argmax(y) for y in model.predict(val_x)]
	true_y = [np.argmax(y) for y in val_y]

	# Create a confusion matrix
	cm = confusion_matrix(true_y, pred_y)

	num_correct = sum([v for j,row in enumerate(cm) for i,v in enumerate(row) if i==j])
	total = sum([v for j,row in enumerate(cm) for i,v in enumerate(row)])

	print "Confusion Matrix:"
	print cm

	print "Accuracy: %.2f" % (float(num_correct) / float(total))

