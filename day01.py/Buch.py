class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten


    def info(self):
        print(f"'{self.titel}' von {self.autor}, {self.seiten} Seiten")


    def lesezeit_schaetzen(self, seiten_pro_stunde = 30):
        if seiten_pro_stunde <= 0:
            return "Ungültige lesegeschwindigkeit"
        lesezeit = self.seiten / seiten_pro_stunde
        return round(lesezeit, 1)
    

buch1 = Buch("Der kleine Prinz", "Antoine de Saint-Exupery", 96)
buch1.info()
print(f"Geschätze lesezeit: {buch1.lesezeit_schaetzen()} Stunden")