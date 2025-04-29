### 2. 🛒 **Lagerverwaltung**

#**Aufgabenstellung:**
#Erstelle eine Klasse **Lager**, die:

# - **Bestand anzeigen**: Zeigt den aktuellen Lagerbestand eines Artikels.
# - **Ware einlagern**: Erhöht den Bestand.
# - **Ware auslagern**: Verringert den Bestand.

class Lager:
    def __init__(self, artikel_name, bestand = 0 ):
        self.artikel_name = artikel_name
        self.bestand = bestand

    def bestand_anzeigen(self):
        print(f"Artikel: {self.artikel_name}, Bestand: {self.bestand} Stück")


    def ware_einlagern(self, menge):
        if menge <= 0:
            print("Ungültige Menge zum Einlagern.")
            return
        self.bestand += menge
        print(f"{menge} Stück von {self.artikel_name} wurden eingelagert.")

    def ware_auslagern(self, menge):
        if menge <= 0:
            print("Ungültige Menge zum Auslagern")
            return
        if menge > self.bestand:
            print(f"Nicht genug Bestand! Nur {self.bestand} Stück verfügbar")
        else:
            self.bestand -= menge
            print(f"{menge} Stück von {self.artikel_name} wurde ausgelagert.")


Lager1 = Lager("Tastatur", 20)
Lager1.bestand_anzeigen()
Lager1.ware_einlagern(10)
Lager1.bestand_anzeigen()
Lager1.ware_auslagern(5)
Lager1.bestand_anzeigen()

        