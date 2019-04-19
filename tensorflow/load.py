import tensorflow.keras as keras 
import tensorflow as tf
from tensorflow.python.platform import gfile
"""
model = keras.models.load_model("mobilenet/saved_model/saved_model.pb")
model.load_weights("mobilenet/checkpoint")
print(" Model : "+str(model.summary()))
"""

import tensorflow as tf
from tensorflow.python.platform import gfile

GRAPH_PB_PATH = 'mobilenet/saved_model/saved_model.pb' #path to your .pb file

import tensorflow as tf
from tensorflow.python.platform import gfile
with tf.compat.v1.Session() as sess:
  print("load graph")
  with gfile.FastGFile(GRAPH_PB_PATH,'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
  sess.graph.as_default()
  tf.import_graph_def(graph_def, name='')
  graph_nodes=[n for n in graph_def.node]
  names = []
  for t in graph_nodes:
    names.append(t.name)
  print(names)