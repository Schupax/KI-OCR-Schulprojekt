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
        
    def getNeuronenAnzahl(self):
        return self.neuronAnzahl
    
    def setNeuronenAnzahl(self, pNeuronenAnzahl):
        self.neuronAnzahl = pNeuronenAnzahl
        
    def getLayerType(self):
        return self.layerType
    
    def setLayerType(self, pLayerType):
        self.layerType = pLayerType