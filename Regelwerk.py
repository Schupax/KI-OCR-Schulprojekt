"""
    Diese Klasse soll für die SchülerInnen eine Black Box sein
"""
import keras
import numpy as np
import tensorflow as tf

class Regelwerk(object):
    def __init__(self):
        self.model = tf.keras.models.Sequential()
        
    def fit(self, pTrainingData):
        (x_train, y_train) = pTrainingData
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=3)
        
    def initLayers(self,pLayers):
        self.model.add(tf.keras.layers.Flatten())
        for layer in pLayers:
            if layer.getLayerType() == 1 or layer.getLayerType() == 2:
                self.model.add(tf.keras.layers.Dense(layer.getNeuronenAnzahl(), activation=tf.nn.relu))
            else:
                self.model.add(tf.keras.layers.Dense(layer.getNeuronenAnzahl(), activation=tf.nn.softmax))
                
    def ladeNetzwerk(self, pPfad):
        self.model = tf.keras.models.load_model(pPfad)
    def speicherNetzwerk(self, pPfad):
        self.model.save(pPfad)
    def vorhersagen(self, pTestDaten):
        return self.model.predict(pTestDaten[:10])