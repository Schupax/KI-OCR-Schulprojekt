class Layer(object):
    
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