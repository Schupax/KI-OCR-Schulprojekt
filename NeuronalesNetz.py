import numpy as np
from Dataset import Dataset
from Layer import Layer
from Regelwerk import Regelwerk

"""
    Diese Modellklasse fasst die Eigenschaften und Funktionen/Methoden eines 
    neuronalen Netzes zusammen.
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
        
        
    def trainieren(self):
        self.regelwerk.initialisiereLayers(self.layers)
        (x_train, y_train) = self.dataset.getTrainingData()
        x_train = self.dataset.normalisiere(x_train)
        for train in range(len(x_train)):
            for row in range(28):
                for x in range(28):
                    if x_train[train][row][x] != 0:
                        x_train[train][row][x] = 1
        ##TODO: nur normalisierte Trainingsdaten d�rfen hier eigentlich rein
        self.regelwerk.anpassen((x_train, y_train))
        self.wurdeTrainiert = True
    
    def save(self, pPfad):
        if self.wurdeTrainiert:
            self.regelwerk.speicherNetzwerk(pPfad)
        #else:   
            #Message/ Exception �� 
            

    """ TODO: die Messages mussen umgeschrieben werden. 
     Die Ergebnisse des Tests sollten zuruckgegeben werden als Array und uber den 
     Controller in Consolen bzw. GUI umgeleitet werden
    """
    def testen(self):
        (x_test, y_test) = self.dataset.getTestData()
        x_test = self.dataset.normalisiere(x_test)
        for test in range(len(x_test)):
            for row in range(28):
                for x in range(28):
                    if x_test[test][row][x] != 0:
                        x_test[test][row][x] = 1
        self.regelwerk.vorhersagen(x_test,10)
    
    def testeBild(self, pZahlenBild):
        vorhersagen = self.regelwerk.vorhersagen(pZahlenBild,1)
        vorhersage = (np.argmax(vorhersagen[0]))
        return vorhersage

        
    
    def laden(self, pPfad):
        self.regelwerk.ladeNetzwerk(pPfad)
        
    def getDataset(self):
        return self.dataset