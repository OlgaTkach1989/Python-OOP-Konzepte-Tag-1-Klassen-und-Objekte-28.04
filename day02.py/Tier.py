class Art:
    def __init__(self, name):
        self.name = name

class Tier:
    def __init__(self, name, art_name):
        self.name = name
        self.art = Art(art_name)

class Pfleger:
    def __init__(self, name):
        self.name = name
        self.tiere = []  

    def tiere_hinzufügen(self, tier):
        self.tiere.append(tier)

class Fuetturung:
    def __init__(self, pfleger, tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self):
        print(f"Pfleger {self.pfleger.name} füttert das Tier {self.tier.name} (Art: {self.tier.art.name}).")


simba = Tier("Simba", "Löwe")
tom = Pfleger("Tom")
tom.tiere_hinzufügen(simba)
f = Fuetturung(tom, simba)
f.starten()
        
       