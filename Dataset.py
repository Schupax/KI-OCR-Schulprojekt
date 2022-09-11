import keras
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.utils.data_utils import get_file

class Dataset(object):
    
    
    
    def loadMNIST(self):
        mnist = tf.keras.datasets.mnist
        (x_train, y_train),(x_test, y_test) = self.load_data('Datasets/mnist.npz')
        self.__trainingData = (x_train, y_train)
        self.__testData = (x_test, y_test)
    def load_data(self,path="mnist.npz"):
        #origin_folder = "Datasets/"
        #path = get_file(
              #path,
              #origin=origin_folder + "mnist.npz",
              #file_hash=
              #'731c5ac602752760c8e48fbffcf8c3b850d9dc2a2aedcf2cc48468fc17b673d1')
        with np.load(path, allow_pickle=True) as f:
            x_train, y_train = f['x_train'], f['y_train']
            x_test, y_test = f['x_test'], f['y_test']
        
            return (x_train, y_train), (x_test, y_test)
        
    def getTrainingData(self):
        return self.__trainingData
    
    def getTestData(self):
        return self.__testData
    
    def normalisiere(self, pXtrain):
        return tf.keras.utils.normalize(pXtrain, axis=1)