from termcolor import colored
from Controller import Controller
from NeuronalesNetz import NeuronalesNetz

class KonsolenAnwendung(object):
    
    def __init__(self):    
        self.optionen = ["erstellen", "laden", "speichern", "trainieren", "testen mit Testdaten", "testen mit Input", "beenden"]
        self.controller = Controller()
        self.netz = 0
    def start(self):
        while True:
            option = self.getOption()
            if option == "beenden":
                print("Das Programm wird beendet")
                break;
            if option == "erstellen":
                self.erstelleNetzwerk()
            if option == "laden":
                self.netz = self.controller.lade()
            if option == "speichern":
                if self.istNetzAngelegt():
                    self.controller.speichere(self.netz,self.getPfad())
            if option == "trainieren":
                if self.istNetzAngelegt():
                    self.controller.train(self.netz)
            if option == "testen mit Testdaten":
                if self.istNetzAngelegt():
                    self.controller.test(self.netz)
            if option == "testen mit Input":
                if self.istNetzAngelegt():
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
        1
    def istNetzAngelegt(self):
        if(self.netz != 0):
            return True
        else:
            print("Es ist kein Netz vorhanden, dass gespeichert werden könnte")
            return False
        
    ##Hier fehlt noch eine Funktion um einen Pfad einzulesen
    def getPfad(self):
        1
    
KonsolenAnwendung().start()