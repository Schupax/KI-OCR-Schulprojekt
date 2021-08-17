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
     
    
    """
        Diese Methode soll nach dem Struktogramm implementiert werden.
    """
    def erstelleNetzwerk(self):
        print("Die Erstellung eines neuronalen Netzs wurde noch nicht implementiert!")
            
            
            
            
    """
        Diese Methode soll nach dem Struktogramm implementiert werden.
    """
    def erstelleLayer(self):
        print("Die Erstellung eines Layers wurde noch nicht implementiert!")
        
        
    def istNetzAngelegt(self):
        if(self.netz != -1):
            return True
        else:
            print("Es ist kein Netz vorhanden, das genutzt werden könnte")
            return False
    
KonsolenAnwendung().start()