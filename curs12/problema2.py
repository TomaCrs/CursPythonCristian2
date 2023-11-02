class CatalogPrajituri:
    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        # self.prajitura = {'nume': nume, 'pret': pret, 'gramaj': gramaj}
        # CatalogPrajituri.lista_prajituri.append(self.prajitura)
        CatalogPrajituri.lista_prajituri.append([self.nume, self.pret, self.gramaj])
    def __str__(self):
        return str(CatalogPrajituri.lista_prajituri)

    def sortare(self):
        camp = input("Alege din optiunile: nume, pret sau gramaj: ").lower()
        while camp not in ['nume', 'pret', 'gramaj']:
            camp = input("Alege din optiunile: nume, pret sau gramaj: ").lower()
        if camp == 'nume':
            return sorted(CatalogPrajituri.lista_prajituri, key=lambda atribut: atribut[0])
        elif camp == 'pret':
            return sorted(CatalogPrajituri.lista_prajituri, key=lambda atribut: atribut[1])
        return sorted(CatalogPrajituri.lista_prajituri, key=lambda atribut: atribut[2])

class Tort(CatalogPrajituri):
    def optiuni(self, etajat = False, glazura = 'ciocolata'):
        self.etajat = etajat
        self.glazura = glazura
    def afisare(self):
        return f"{self.etajat}, {self.glazura}"

class Fursec(CatalogPrajituri):
    pass


pr1 = Tort('red velvet', 150, 1250)
pr2 = Tort('white velvet', 250, 1150)
pr3 = Tort('blue velvet', 175, 1650)
pr4 = Fursec('red macaroon', 5, 24)
pr5 = Fursec('white macaroon', 4, 26)
pr6 = Fursec('blue macaroon', 5, 25)
print(pr6.sortare())
pr2.optiuni(True, 'cacao')
print(pr2.afisare())
pr3.optiuni(True, 'blueberries')
print(pr3.afisare())
