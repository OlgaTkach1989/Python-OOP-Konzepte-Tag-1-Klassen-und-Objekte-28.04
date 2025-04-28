class Produkt:
    def __init__(self, name, preis, bestand):
        self.name = name
        self.preis = preis
        self.bestand = bestand
       


    def kaufen(self, menge):
        if menge <= 0:
            print("Ungültige Menge zum Kaufen.")
            return
        if menge > self.bestand:
            print(f"Nicht genug Bestand! Nur {self.bestand} Stück verfügbar")
        else:
            self.bestand -= menge
            gesamtpreis = menge * self.preis
            print(f"Du hast {menge} {self.name}(s) für {gesamtpreis:.2f} Euro gekauft.")
    def preis_aendern(self, neuer_preis):
        if neuer_preis <= 0:
            print("Ungültiger Preis")
            return
        self.preis = neuer_preis
        print(f"Neuer Preis für {self.name}: {self. preis:.2f} Euro.")


produkt1 = Produkt("Laptop", 999.99, 15)
produkt1.kaufen(2)
produkt1.preis_aendern(899.99)
produkt1.kaufen(2)

        