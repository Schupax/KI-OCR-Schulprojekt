from Regelwerk import Regelwerk
from Dataset import Dataset
from NeuronalesNetz import NeuronalesNetz






class Controller(object):
    
    def lade(self,pDateiname):
        regelwerk = Regelwerk()
        dataset = Dataset()
        dataset.loadMNIST()
        netz = NeuronalesNetz(0,regelwerk,dataset)
        netz.laden(pDateiname)
        return netz
        
    def speichere(self, pNeuronalesNetz, pDateiname):   
        pNeuronalesNetz.speichern(pDateiname)
        
    def testen(self,pNeuronalesNetz):
        return pNeuronalesNetz.testen()
        
    def testeBild(self,pNeuronalesNetz,pZahlenBild):
        return pNeuronalesNetz.testeBild(pZahlenBild)
        
    def trainieren(self,pNeuronalesNetz):  
        pNeuronalesNetz.trainieren()
        
    
    