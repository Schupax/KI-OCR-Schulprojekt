"""
    Diese Modellklasse fasst die Eigenschaften und Funktionen/Methoden eines 
    einer Schicht in einem neuronalen Netz zusammen.
"""

class Layer(object):
    
    """
        mögliche Werte fur den "LayerType" und ihre Bedeutung
            1 --> Inputlayer
            2 --> Hiddenlayer
            3 --> Outputlayer 
    """
    def __init__(self,pNeuronAnzahl,pLayerType):
        self.neuronAnzahl = pNeuronAnzahl
        self.layerType = pLayerType
        
    def gibNeuronenAnzahl(self):
        return self.neuronAnzahl
    
    def setzeNeuronenAnzahl(self, pNeuronenAnzahl):
        if pNeuronenAnzahl > 0:
            self.neuronAnzahl = pNeuronenAnzahl
        else:
            print("Setzen der Neuronenanzahl ist fehlgeschlagen")
        
    def gibLayerType(self):
        return self.layerType
    
    def setzeLayerType(self, pLayerType):
        if pLayerType > 0 and pLayerType < 4:
            self.layerType = pLayerType
        else:
            print("Setzen des Layertpy ist fehlgeschlagen")