from termcolor import colored
from NeuronalesNetz import NeuronalesNetz
from Regelwerk import Regelwerk
from Dataset import Dataset
from Layer import Layer
from View import View
##import pygame

class KonsolenAnwendung(View):
    
    def __init__(self):
        super().__init__()
        self.optionen = ["erstellen", "laden", "speichern", "trainieren", "testen mit Testdaten", "testen mit Input", "beenden"]
        
        
    def start(self):
        while True:
            option = self.getOption()
            if option == "beenden":
                print("Das Programm wird beendet")
                break;
            if option == "erstellen":
                self.erstelleNetzwerk()
                
            if option == "laden":
                self.netz = self.controller.lade('my_model.tf')
                print(colored("Das Netz wurde erfolgreich geladen","green"))
                
            if option == "speichern":
                if self.istNetzAngelegt():
                    self.controller.speichere(self.netz,'my_model.tf')
                    print(colored("Das Netz wurde erfolgreich gespeichert","green"))
                    
            if option == "trainieren":
                if self.istNetzAngelegt():
                    print(colored("Dieser Prozess kann einige Minuten dauern bitte warten","yellow"))
                    self.controller.trainieren(self.netz)
                    
            if option == "testen mit Testdaten":
                if self.istNetzAngelegt():
                    print(colored("Dieser Prozess kann einige Minuten dauern bitte warten","yellow"))
                    self.controller.testen(self.netz)
                    print(colored("Der Test wurde erfolgreich abgeschlossen.","green"))
                    
            if option == "testen mit Input":
                if self.istNetzAngelegt():
                    vorhersage = self.controller.testeBild(self.netz,self.schreibeZahl())
                    print(colored("Ich denke das ist eine: {}".format(vorhersage),"yellow"))
                    
                
    
    def getOption(self):
        x = 1
        print("Die folgenden Optionen sind möglich: (1-{})".format(len(self.optionen)))
        print("Neuronales Netz")
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
        inputLayerAngelegt = False
        outputLayerAngelegt = False
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
            
            
            if aktOption == 1: ##Layer anlegen
                layer = self.erstelleLayer()
                if layer.getLayerType() == 1:
                    inputLayerAngelegt = True
                if layer.getLayerType() == 3:
                    outputLayerAngelegt = True
                layers.append(layer)
                print(colored("Layer wurde angelegt","green"))
            if aktOption == 2: ##Netzwerkerstellung abschließen
                if inputLayerAngelegt == False:
                    print(colored("Erstellung des Netzwerks konnte nicht abgeschlossen werden","red"))
                    print(colored("Ein Inputlayer fehlt","red"))
                    aktOption = -1
                if outputLayerAngelegt == False:
                    print(colored("Erstellung des Netzwerks konnte nicht abgeschlossen werden","red"))
                    print(colored("Ein Outputlayer fehlt","red"))
                    aktOption = -1
                if aktOption == 2:
                    dataset = Dataset()
                    dataset.loadMNIST()
                    self.netz = NeuronalesNetz(layers,Regelwerk(),dataset)
                    print(colored("Erstellung des Netzwerks wurde abgeschlossen","green"))
            
            
            
            
        
    def erstelleLayer(self):
        neuronenAnzahl = -1
        layerTyp = -1
        print("Bitte gibt die Anzahl der Neuronen für das Layer ein:")
        while(neuronenAnzahl == -1):
            try:
                i = int(input())
            except ValueError:
                print(colored("Die Eingabe muss eine Ganzzahl sein größer als 0!","red"))
            if i <0:
                print(colored("Die Eingabe muss eine Ganzzahl sein größer als 0","red"))
            else:
                neuronenAnzahl = i
        print("Bitte gibt den Typ für das Layer an:")
        print("1 --> Inputlayer")
        print("2 --> Hiddenlayer")
        print("3 --> Outputlayer")
        while(layerTyp == -1):
            try:
                i = int(input())
            except ValueError:
                print(colored("Die Eingabe muss eine Ganzzahl zwischen 1 und 3 sein","red"))
            if i < 0 and i > 4:
                print(colored("Die Eingabe muss eine Ganzzahl zwischen 1 und 3 sein","red"))
            else:
                layerTyp = i
        return Layer(neuronenAnzahl,layerTyp)
        
    def istNetzAngelegt(self):
        if(self.netz != -1):
            return True
        else:
            print("Es ist kein Netz vorhanden, dass genutzt werden könnte")
            return False
    
KonsolenAnwendung().start()