import createModel
import drawNumber
import testNetwork


class IO(object):
    
    #in createModel fehlt Funktion zum laden
    def load(self,pNeuronalesNetz):
        pNeuronalesNetz.loadModel()
    #in craete fehlt Funktion zum speichern
    def save(self, pNeuronalesNetz, pPfad):   
        pNeuronalesNetz.save(pPfad)
    #in testNetwork fehlt Funktion zum testen      
    def test(self,pNeuronalesNetz):
        pNeuronalesNetz.test()
    #in createModel fehlt Funktion zum trainieren
    def train(self,pNeuronalesNetz):  
        pNeuronalesNetz.train()