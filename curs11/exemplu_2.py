class Exemplu:

    counter = 0

    def __init__(self, val):
        self.first = val
        Exemplu.counter += 1


"""
proprietatea -> first
clasa -> Exemplu
obiect -> obiect_1,obiect_2,obiect_3
activitate -> 
"""

obiect_1 = Exemplu('bmw')
obiect_2 = Exemplu('audi')
obiect_3 = Exemplu('mercedes')
# print(obiect_1.first)
# print(obiect_2.first)
# print(obiect_3.first)
# print(Exemplu.counter)
# print(obiect_1.counter)


class Pisica:

    nr_picioare = 4
    nr_pisici = 0
    nr_vieti = 9

    def __init__(self, size='mare'):
        # self.__marime = size
        self.marime = size
        Pisica.nr_pisici += 1

    def set_second(self, val):
        self.second = val

    def mananca(self, tip_mancare):
        self.mancare = tip_mancare

    def accidentare(self):
        self.nr_vieti -= 1


Felix = Pisica()
# print(Felix._Pisica__marime)
Max = Pisica('mic')
# print(Max._Pisica__marime)
Felix.set_second("tarcat")
# print(Felix.second)
# print(Felix.__dict__)
# print(Max.__dict__)
Felix.varsta = 3.2
# print(Felix.varsta)
Max.mananca('bobite')
# print(Max.mancare)
# print(Max.__dict__)
# print(Felix.__dict__)

print(Max.nr_picioare)
print(Pisica.nr_picioare)
print(Max.nr_pisici)

Max.accidentare()
Max.accidentare()
print(Max.nr_vieti)
print(Felix.nr_vieti)
