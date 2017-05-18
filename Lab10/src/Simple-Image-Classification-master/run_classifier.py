from keras.models import load_model
import tensorflow as tf 
import numpy as np

"""
Setup the inception model
"""
def setup_inception():
	inception_model = 'inception_v3.pb'

	with tf.gfile.FastGFile(inception_model, 'rb') as f:
	    graph_def = tf.GraphDef()
	    graph_def.ParseFromString(f.read())
	    tf.import_graph_def(graph_def, name='')

setup_inception()

"""
Generate the class prediction for an image using the trained classifier.
"""
def predict(img_path, model):
	with tf.Session() as sess:
		pool_3_tensor = sess.graph.get_tensor_by_name('pool_3:0')

		# generate the features for the image
		try:
			image_data = tf.gfile.FastGFile(img_path).read()
			feature_vector = sess.run(pool_3_tensor, {'DecodeJpeg/contents:0': image_data}).flatten()
		except:
			raise Exception("Failed to load %s. Make sure this is a Jpeg image." % img_path)

		# generate the prediction using the trained classifier
		prediction = model.predict(np.array([feature_vector]))[0]

		return np.argmax(prediction)

