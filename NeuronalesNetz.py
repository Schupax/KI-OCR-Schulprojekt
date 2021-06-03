import numpy as np
import Dataset
import Regelwerk

"""
    Diese Modellklasse fasst die Eigenschaften und Funktionen/Methoden eines neuronalen Netzes zusammen.
"""

class NeuronalesNetz(object):
    
    def __init__(self,pLayers, pRegelwerk, pDataset = 0):
        self.layers = pLayers
        self.wurdeTrainiert = False
        self.regelwerk = pRegelwerk
        if pDataset == 0:
            self.dataset = Dataset()
            self.dataset.loadMNIST()
        else:
            self.dataset = pDataset
        
        
    def train(self):
        self.__initLayers()
        (x_train, y_train) = self.dataset.getTrainingData()
        x_train = self.dataset.normalize(x_train)
        for train in range(len(x_train)):
            for row in range(28):
                for x in range(28):
                    if x_train[train][row][x] != 0:
                        x_train[train][row][x] = 1
        self.regelwerk.fit()
        self.wurdeTrainiert = True
    
    def save(self, pPfad):
        if self.wurdeTrainiert:
            self.regelwerk.speicherNetzwerk(pPfad)
        #else:   
            #Message/ Exception ´´ 
            

    """
     TODO: die Messages müssen umgeschrieben werden. 
     Die Ergebnisse des Tests sollten zurückgegeben werden als Array und über den 
     Controller in Consolen bzw. GUI umgeleitet werden
    """
    def test(self):
        (x_test, y_test) = self.dataset.getTestData()
        x_test = self.dataset.normalize(x_test)
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
                count+=1
        print("The program got", count, 'wrong, out of', len(x_test))
        print(str(100 - ((count/len(x_test))*100)) + '% correct')
    
    def load(self, pPfad):
        self.regelwerk.ladeNetzwerk(pPfad)