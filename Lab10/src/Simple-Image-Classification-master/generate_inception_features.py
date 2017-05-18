import numpy as np
import tensorflow as tf
import os

"""
Generates the features for all the images in 'images_dir'. The 'images_dir' directory should be formatted as such:

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

All the features will be written to 'features_file'.
"""
def generate_features(images_dir, features_file):
	inception_model = 'inception_v3.pb'

	with tf.gfile.FastGFile(inception_model, 'rb') as f:
	    graph_def = tf.GraphDef()
	    graph_def.ParseFromString(f.read())
	    tf.import_graph_def(graph_def, name='')

	with tf.Session() as sess:
			pool_3_tensor = sess.graph.get_tensor_by_name('pool_3:0')

			with open(features_file, 'w') as f:
				for class_dir in os.listdir(images_dir):
					class_dir_path = os.path.join(images_dir, class_dir)

					if os.path.isdir(class_dir_path):
						for img in os.listdir(class_dir_path):
							img_path = os.path.join(class_dir_path, img)

							# generate the features for the image
							try:
								image_data = tf.gfile.FastGFile(img_path).read()
								feature_vector = sess.run(pool_3_tensor, {'DecodeJpeg/contents:0': image_data}).flatten()
							except:
								print "Failed to load %s. Make sure this is a Jpeg image." % img_path
								continue

							# write the feature vector (2048 dimensions) to 'features_file'
							# Each line is in the form "class_name,feature_0,feature_1,...,feature_2047"
							f.write(class_dir + ',' + ','.join([str(x) for x in feature_vector]) + '\n')