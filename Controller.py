import install_requirements
from Layer import Layer
from Regelwerk import Regelwerk
from Dataset import Dataset
from NeuronalesNetz import NeuronalesNetz






class Controller(object):
    
    def lade(self,pPfad):
        regelwerk = Regelwerk()
        netz = NeuronalesNetz(0,regelwerk,-1)
        netz.laden(pPfad)
        return netz
        
    def speichere(self, pNeuronalesNetz, pPfad):   
        pNeuronalesNetz.save(pPfad)
    #in testNetwork fehlt Funktion zum testen      
    def test(self,pNeuronalesNetz):
        pNeuronalesNetz.test()
    #in createModel fehlt Funktion zum trainieren
    def train(self,pNeuronalesNetz):  
        pNeuronalesNetz.train()
        
        
def testCase():
    inputLayer = Layer(128,1)
    hiddenLayer = Layer(128,2)
    outputLayer = Layer(10,3)
    layers = [inputLayer,hiddenLayer,outputLayer]
    regelwerk = Regelwerk()
    dataset = Dataset()
    dataset.loadMNIST()
    netz = NeuronalesNetz(layers,regelwerk,dataset)
    
    