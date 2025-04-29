class Pflanze:
     def __init__(self, name, wasserstand = 0, max_wasserstand = 100):
        self.name = name
        self.wasserstand = wasserstand
        self.max_wasserstand = max_wasserstand


     def wasserstand_anzeigen(self):
        print(f"{self.name}: aktueller Wasserstand = {self.wasserstand} / {self. max_wasserstand}")

     def giessen(self, menge):
        if menge <= 0:
            print("Ungültige Gießmenge.")
            return
        self.wasserstand += menge
        if self.wasserstand > self.max_wasserstand:
            self.wasserstand = self.max_wasserstand
            print(f"{self.name} wurde gegossen. Der Wasserstand ist jetzt voll!")
        else:
            print(f"{self.name} wuede gegossen. Wasserstand: {self.wasserstand}")


     def wasser_verbrauchen(self, menge):
        if menge <= 0:
            print("Ungültige Verbrauch.")
            return
        self.wasserstand -= menge
        if self.wasserstand < 0:
            print(f"{self.name} hat kein Wasser mehr!")
        else:
            print(f"{self.name} hat Wasser verbraucht. Aktueller Wasserstand: {self.wasserstand}")
        
pflanze1 = Pflanze("Rose")
pflanze1.wasserstand_anzeigen()
pflanze1.giessen(30)
pflanze1.wasser_verbrauchen(10)
pflanze1.wasserstand_anzeigen()