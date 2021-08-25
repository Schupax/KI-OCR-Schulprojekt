from Regelwerk import Regelwerk
from Dataset import Dataset
from NeuronalesNetz import NeuronalesNetz






class Controller(object):
    
    def lade(self,pPfad):
        regelwerk = Regelwerk()
        dataset = Dataset()
        dataset.loadMNIST()
        netz = NeuronalesNetz(0,regelwerk,dataset)
        netz.laden(pPfad)
        return netz
        
    def speichere(self, pNeuronalesNetz, pPfad):   
        pNeuronalesNetz.save(pPfad)
        
    def testen(self,pNeuronalesNetz):
        return pNeuronalesNetz.testen()
        
    def testeBild(self,pNeuronalesNetz,pZahlenBild):
        return pNeuronalesNetz.testeBild(pZahlenBild)
        
    def trainieren(self,pNeuronalesNetz):  
        pNeuronalesNetz.trainieren()
        
    
    