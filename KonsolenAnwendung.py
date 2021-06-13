from termcolor import colored
from Controller import Controller
from NeuronalesNetz import NeuronalesNetz
from Regelwerk import Regelwerk
from Dataset import Dataset
from Layer import Layer

class KonsolenAnwendung(object):
    
    def __init__(self):    
        self.optionen = ["erstellen", "laden", "speichern", "trainieren", "testen mit Testdaten", "testen mit Input", "beenden"]
        self.controller = Controller()
        self.netz = -1
        
        
    def start(self):
        while True:
            option = self.getOption()
            if option == "beenden":
                print("Das Programm wird beendet")
                break;
            if option == "erstellen":
                self.erstelleNetzwerk()
                
            if option == "laden":
                self.netz = self.controller.lade(self.netz,self.getPfad())
                
            if option == "speichern":
                if self.istNetzAngelegt():
                    self.controller.speichere(self.netz,self.getPfad())
                    
            if option == "trainieren":
                if self.istNetzAngelegt():
                    self.controller.trainieren(self.netz)
                    
            if option == "testen mit Testdaten":
                if self.istNetzAngelegt():
                    self.controller.testen(self.netz)
                    
            if option == "testen mit Input":
                if self.istNetzAngelegt():
                    ##TODO hier fehlt noch die Funktion, die auf die MiniGui zugreift und die Funktion zum Controller
                    self.controller.test(self.netz)
                
    
    def getOption(self):
        x = 1
        print("Die folgenden Optionen sind möglich: (1-{})".format(len(self.optionen)))
        for option in self.optionen:
            print("{} {}".format(x,option))
            x=x+1
        i = -1
        try:
            i = int(input()) -1
        except ValueError:
            print(colored("Die Eingabe muss zwischen 1 und {} liegen".format(len(self.optionen)),"red"))
        if i < len(self.optionen) and i >= 0:
            return self.optionen[i]
        else:
            print(colored("Die Eingabe muss zwischen 1 und {} liegen".format(len(self.optionen)),"red"))
            return -1
        
    def erstelleNetzwerk(self):
        aktOption = -1
        layers = []
        while aktOption != 0 and aktOption != 2:
            optionen = ["abbrechen","Layer anlegen", "Netzwerkerstellung abschließen"]
            x = 1
            print("Die folgenden Optionen sind möglich: (1-{})".format(len(optionen)))
            for option in optionen:
                print("{} {}".format(x,option))
                x=x+1
            try:
                aktOption = int(input()) -1
            except ValueError:
                print(colored("Die Eingabe muss zwischen 1 und {} liegen".format(len(optionen)),"red"))
            inputLayerAngelegt = False
            outputLayerAngelegt = False
            
            if aktOption == 1: ##Layer anlegen
                layer = self.erstelleLayer()
                if layer.getLayerType() == 1:
                    inputLayerAngelegt = True
                if layer.getLayerType() == 3:
                    outputLayerAngelegt = True
                layers.append(layer)
                print("Layer wurde angelegt")
            if aktOption == 2: ##Netzwerkerstellung abschließen
                if inputLayerAngelegt != True:
                    print(colored("Erstellung des Netzwerks konnte nicht abgeschlossen werden","red"))
                    print(colored("Ein Inputlayer fehlt","red"))
                    aktOption = -1
                if outputLayerAngelegt != True:
                    print(colored("Erstellung des Netzwerks konnte nicht abgeschlossen werden","red"))
                    print(colored("Ein Outputlayer fehlt","red"))
                    aktOption = -1
                if aktOption != 2:
                    dataset = Dataset()
                    dataset.loadMNIST()
                    self.netz = NeuronalesNetz(layers,Regelwerk(),dataset)
                    print(colored("Erstellung des Netzwerks wurde abgeschlossen","green"))
            
            
            
            
        
    def erstelleLayer():
        neuronenAnzahl = -1
        layerTyp = -1
        print("Bitte gibt die Anzahl der Neuronen für das Layer ein:")
        while(neuronenAnzahl == -1):
            try:
                i = int(input()) -1
            except ValueError:
                print(colored("Die Eingabe muss eine Ganzzahl sein größer als 0!","red"))
            if i >0:
                print(colored("Die Eingabe muss eine Ganzzahl sein größer als 0","red"))
            else:
                neuronenAnzahl = i
        print("Bitte gibt den Typ für das Layer an:")
        print("1 --> Inputlayer")
        print("2 --> Hiddenlayer")
        print("3 --> Outputlayer")
        while(neuronenAnzahl == -1):
            try:
                i = int(input()) -1
            except ValueError:
                print(colored("Die Eingabe muss eine Ganzzahl muss zwischen 1 und 3 sein","red"))
            if i >0 and i < 4:
                print(colored("Die Eingabe muss eine Ganzzahl muss zwischen 1 und 3 sein","red"))
            else:
                layerTyp = i
        return Layer(neuronenAnzahl,layerTyp)
        
    def istNetzAngelegt(self):
        if(self.netz != -1):
            return True
        else:
            print("Es ist kein Netz vorhanden, dass gespeichert werden könnte")
            return False
        
    ##Hier fehlt noch eine Funktion um einen Pfad einzulesen
    def getPfad(self):
        1
    
KonsolenAnwendung().start()