"""
    Diese Modellklasse fasst die Eigenschaften und Funktionen/Methoden 
    einer Schicht in einem neuronalen Netz zusammen.
"""

class Layer(object):
    
    """
        1.  Implementiere die Eigenschaften und Methoden aus dem UML-Diagramm. 
        
        2.  Erweitere die Methoden setzeLayertyp und setzeNeuronenanzahl um eine Prüfung der Parameter.
        
            Tipp:
                1. mögliche Werte fur den "Layertyp" und ihre Bedeutung:
                    1 --> Inputlayer
                    2 --> Hiddenlayer
                    3 --> Outputlayer
                    
                2. Wie viele Neuronen sind Maximal/Minimal sinnvoll?
                
        3.  Nenne Vor- und Nachteile für die Implementierung des Layertyps als Vererbung. 
            Begründe die Entscheidung, den Layertyp als Ganzzahl darzustellen.
            
            Tipp:
                Mit der Vererbung ist gemeint, dass es eine Klasse Layer und dass es je eine Klasse pro Layertyp gibt
        
    """