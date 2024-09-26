# This is a machine learning model to classify articles 
# change training datasets will lead to different labeling
import numpy as np
from datetime import date
from datetime import datetime
import math
from datetime import timedelta
from dateutil.relativedelta import relativedelta, MO
from pandas import DataFrame
import pandas as pd
import os


#################convert the train and test into dictionaries##########
#trainkr.json is a the training set that include both the text that fall into the event category and the event that do not fall into the category.

train = pd.read_json('trainkr.json')
dicos1 = 'Dictionarykr/kr/'
dicos2 = 'Dictionarykr/nonkr/'
os.makedirs(os.path.dirname(dicos1), exist_ok=True) 
os.makedirs(os.path.dirname(dicos2), exist_ok=True) 
for index, row in train.iterrows():
    if row['predict50_kr'] ==1:  
        f = open(dicos1+str(index)+'.txt', 'w')
        f.write(row[0])
        f.close()
    else:
        f = open(dicos2+str(index)+'.txt', 'w')
        f.write(row[0])
        f.close()

#https://www.tensorflow.org/text/tutorials/classify_text_with_bert
import os
import shutil

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization  # to create AdamW optimizer

import matplotlib.pyplot as plt

tf.get_logger().setLevel('ERROR')

# Preprocessing
tfhub_handle_preprocess= 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'

# Bert encoder
tfhub_handle_encoder = 'https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-2_H-128_A-2/2'

bert_preprocess_model = hub.KerasLayer(tfhub_handle_preprocess)
def build_classifier_model():
  text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
  preprocessing_layer = hub.KerasLayer(tfhub_handle_preprocess, name='preprocessing')
  encoder_inputs = preprocessing_layer(text_input)
  encoder = hub.KerasLayer(tfhub_handle_encoder, trainable=True, name='BERT_encoder')
  outputs = encoder(encoder_inputs)
  net = outputs['pooled_output']
  net = tf.keras.layers.Dropout(0.1)(net)
  net = tf.keras.layers.Dense(1, activation=None, name='classifier')(net)
  return tf.keras.Model(text_input, net)

loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)
metrics = tf.metrics.BinaryAccuracy()

AUTOTUNE = tf.data.AUTOTUNE
batch_size = 32
seed = 42
raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'Dictionarykr',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

class_names = raw_train_ds.class_names
train_ds = raw_train_ds.cache().prefetch(buffer_size=AUTOTUNE)

val_ds = tf.keras.utils.text_dataset_from_directory(
    'Dictionarykr',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)

val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
###########test the label##############

for text_batch, label_batch in train_ds.take(1):
  for i in range(3):
    print(f'Review: {text_batch.numpy()[i]}')
    label = label_batch.numpy()[i]
    print(f'Label : {label} ({class_names[label]})')

##########################
epochs = 5
steps_per_epoch = tf.data.experimental.cardinality(train_ds).numpy()
num_train_steps = steps_per_epoch * epochs
num_warmup_steps = int(0.1*num_train_steps)

init_lr = 3e-5
optimizer = optimization.create_optimizer(init_lr=init_lr,
                                          num_train_steps=num_train_steps,
                                          num_warmup_steps=num_warmup_steps,
                                          optimizer_type='adamw')
classifier_model = build_classifier_model()
classifier_model.compile(optimizer=optimizer,
                         loss=loss,
                         metrics=metrics)

history = classifier_model.fit(x=train_ds,
                               validation_data=val_ds,
                               epochs=epochs)


loss, accuracy = classifier_model.evaluate(val_ds)

print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')
classifier_model.save('BERT_kr', include_optimizer=False)

