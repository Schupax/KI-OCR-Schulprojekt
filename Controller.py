from Regelwerk import Regelwerk
from NeuronalesNetz import NeuronalesNetz






class Controller(object):
    
    def lade(self,pPfad):
        regelwerk = Regelwerk()
        netz = NeuronalesNetz(0,regelwerk,-1)
        netz.laden(pPfad)
        return netz
        
    def speichere(self, pNeuronalesNetz, pPfad):   
        pNeuronalesNetz.save(pPfad)
        
    def testen(self,pNeuronalesNetz):
        pNeuronalesNetz.testen()
        
    def testeBild(self,pNeuronalesNetz,pZahlenBild):
        pNeuronalesNetz.testeBild(pZahlenBild)
        
    def trainieren(self,pNeuronalesNetz):  
        pNeuronalesNetz.trainieren()
        
    
    