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
    #in testNetwork fehlt Funktion zum testen      
    def testen(self,pNeuronalesNetz):
        pNeuronalesNetz.testen()
    #in createModel fehlt Funktion zum trainieren
    def trainieren(self,pNeuronalesNetz):  
        pNeuronalesNetz.trainieren()
        
    
    