class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = dict()
        self.absente = 0

    def __str__(self):
        return str(self.absente)

    def incrementare_abs(self):
        self.absente += 1

    def stergere_abs(self, scutire):
        if type(scutire) is int:
            if self.absente >= scutire:
                self.absente -= int(scutire)
        else:
            return "Invalid Input"


class Extensie1(Catalog):
    # def __init__(self, nume, prenume):
    #     super().__init__(nume, prenume)

    def adaugare_materie(self, materie, note):
        self.materii[materie] = note

    def afisare_materii(self):
        return list(self.materii.keys())

    def situatie_scolare(self):
        medii = {}
        for mt, nt in self.materii.items():
            medie = 0
            for x in nt:
                if type(x) is int:
                    medie += x
            medii[mt] = round(medie / len(nt),2)
        return medii


student1 = Extensie1("Roata", "Ion")
student1.incrementare_abs()
student1.incrementare_abs()
student1.incrementare_abs()
student1.stergere_abs(2)
student2 = Extensie1("Cerc", "George")
student2.incrementare_abs()
student2.incrementare_abs()
student2.incrementare_abs()
student2.incrementare_abs()
student2.stergere_abs(2)
print(student1)
print(student2)
student1.adaugare_materie("Python", [10,7,9])
student2.adaugare_materie("Python", [8,5,9])
student2.adaugare_materie("Matematica", [10,9,9])
student1.adaugare_materie("Romana", [6,9,9])
print(student1.afisare_materii())
print(student2.afisare_materii())
print(student1.situatie_scolare())
print(student2.situatie_scolare())