import keras
import tensorflow as tf

class Dataset(object):
    
    
    
    def loadMNIST(self):
        (x_train, y_train),(x_test, y_test) = self.dataset.load_data()
        self.__trainingData = (x_train, y_train)
        self.__testData = (x_test, y_test)
        
    def getTrainingData(self):
        return self.__trainingData
    
    def getTestData(self):
        return self.__testData
    
    def normalize(self, pXtrain):
        return tf.keras.utils.normalize(pXtrain, axis=1)
    
    