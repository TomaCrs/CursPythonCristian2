class Animal:
    patruped = 2
    def __init__(self, varsta):
        self.varsta = varsta
class Patruped(Animal):
    # patruped = 1
    def __init__(self, name, varsta):
        super().__init__(varsta)
        self.name = name

class Carnivor:
    patruped = 3
    def __init__(self, tip_carne):
        self.carne = tip_carne

class Caine(Patruped, Carnivor):
    nr_picioare = 4
    def __init__(self, name, varsta,tip_carne):
        # super().__init__(name)
        Patruped.__init__(self,name, varsta)
        Animal.__init__(self, varsta)
        Carnivor.__init__(self,tip_carne)
        self.name = name

    def __str__(self):
        return self.name

    def botez(self, name):
        self.name = name
        return self.name

exemplu_caine = Caine("Rex", 2, "porc")
print(exemplu_caine.__dict__)
print(exemplu_caine.patruped)