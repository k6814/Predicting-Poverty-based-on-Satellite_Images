import os
import sys
import tensorflow as tf
from PIL import Image


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Unpersists graph from file
with tf.gfile.FastGFile("output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile("output_labels.txt")]
path = sys.argv[1]
outpath = sys.argv[2]

#Creating directory for each of label

os.mkdir(outpath+label_lines[0])
os.mkdir(outpath+label_lines[1])
#os.mkdir(outpath+label_lines[2])

#Reading all the images in the directory
for subdirs, dirs, files in os.walk(path):
    for pic in files:
        image_path = os.path.join(subdirs,pic)
        img = Image.open(image_path)         
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()




        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            
            predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})
            
            # Sort to show labels of first prediction in order of confidence
            top_one = predictions[0].argsort()[-len(predictions[0]):][::-1][0]
            score = predictions[0][top_one]
            pred_class = label_lines[top_one]
            img.save(outpath+'/'+pred_class+'/'+str(pic),quality=100) #Save the image
            
            #Uncomment below line to print the label for each of the image
            '''
            score = predictions[0][top_one]
            print(' %s  (score = %.2f)' % (pred_class, score))'''
