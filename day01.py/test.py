class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe


    def fahren(self):
        print(f"{self.farbe} es {self.marke} färt")

    def hupen(self):
        print(f"{self.marke} hupt: Huuuup!")
# Objekte erstellen
mein_auto = Auto("BMW", "Gelb")
dein_auto = Auto("Mercedes", "Schwarz")

mein_auto.fahren()
dein_auto.fahren()
mein_auto.hupen()


        