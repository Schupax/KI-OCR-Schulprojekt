import install_requirements

import keras
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

class NeuronalesNetz(object):
    
    def __init__(self,pLayers,pDataset = 0):
        self.layers = pLayers
        self.__initLayers()
        if pDataset == 0:
            self.dataset = tf.keras.datasets.mnist
        else:
            self.dataset = pDataset
        self.model = tf.keras.models.Sequential()
        
    def train(self):
        (x_train, y_train),(x_test, y_test) = self.dataset.load_data()
        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)
        
        for train in range(len(x_train)):
            for row in range(28):
                for x in range(28):
                    if x_train[train][row][x] != 0:
                        x_train[train][row][x] = 1
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        
        self.model.fit(x_train, y_train, epochs=3)
               
    def __initLayers(self):
        self.model.add(tf.keras.layers.Flatten())
        for layer in self.layers:
            if layer.getLayerType() == 1 or layer.getLayerType() == 2:
                self.model.add(tf.keras.layers.Dense(layer.getNeuronenAnzahl(), activation=tf.nn.relu))
            else:
                self.model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
                
    def getModel(self):
        return self.model
    
    def test(self):
        (x_train, y_train),(x_test, y_test) = self.dataset.load_data()
        x_test = tf.keras.utils.normalize(x_test, axis=1)
        for test in range(len(x_test)):
            for row in range(28):
                for x in range(28):
                    if x_test[test][row][x] != 0:
                        x_test[test][row][x] = 1
        predictions = self.model.predict(x_test[:10])
        actual = y_test[x]
        count = 0
        for x in range(len(predictions)):
            guess = (np.argmax(predictions[x]))
            actual = y_test[x]
            print("I predict this number is a:", guess)
            print("Number Actually Is a:", actual)
            if guess != actual:
                #print("--------------")
                #print('WRONG')
                #print('---------------')
                count+=1
            plt.imshow(x_test[x], cmap=plt.cm.binary)
            plt.show()
        print("The program got", count, 'wrong, out of', len(x_test))
        print(str(100 - ((count/len(x_test))*100)) + '% correct')
    
    def load(self, pPfad):
        self.model = tf.keras.models.load_model(pPfad)