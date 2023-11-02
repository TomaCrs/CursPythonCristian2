class Clasa1:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip
        self.culoare = None

    def colour(self, culoare):
        self.culoare = culoare

    def afisare_culoare(self):
        return f"Culoarea este {self.culoare}"


class Clasa2(Clasa1):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = None

    def scaune(self, scaune_incalzite=False):
        self.scaune_incalzite = scaune_incalzite


class Clasa3(Clasa1):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.bloc_optic_led = None

    def lumini(self, led=False):
        self.bloc_optic_led = led


masina1 = Clasa2("Aro", "M461")
masina1.scaune(True)
masina1.colour("rosu")
masina2 = Clasa3("Dacia", "Logan")
masina2.lumini()
masina2.colour("negru")
print(masina1.afisare_culoare(), masina1.scaune_incalzite, masina1.marca, masina1.tip)
print(masina2.afisare_culoare(), masina2.bloc_optic_led, masina2.marca, masina2.tip)
