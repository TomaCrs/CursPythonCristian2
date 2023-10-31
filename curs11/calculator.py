class Calculator:

    def __init__(self):
        self.nr1 = self.nr_check(input("Insert first number: "), 1)
        self.nr2 = self.nr_check(input("Insert second number: "), 2)
        self.op = self.op_check(input("Insert operation sign: "))

    def nr_check(self, number, counter):
        while True:
            try:
                float(number)
                break
            except ValueError:
                number = input(f"Numarul {number} este incorect. Aduaga din nou numarul {counter}: ")
        return float(number)

    def op_check(self, operator):
        while operator not in '+-*/' or len(operator) != 1:
            operator = input("Insert operation sign: ")
        return operator

    def adunare(self):
        return self.nr1 + self.nr2

    def scadere(self):
        return self.nr1 - self.nr2

    def inmultire(self):
        return self.nr1 * self.nr2

    def impartire(self):
        if int(self.nr2) != 0:
            return self.nr1 / self.nr2
        return "Eroare"

    def calcul(self):
        if self.op == '+':
            return self.adunare()
        elif self.op == '-':
            return self.scadere()
        elif self.op == '*':
            return self.inmultire()
        return self.impartire()

    def __str__(self):
        return f"{self.nr1} {self.op} {self.nr2} = {self.calcul()}"


while True:
    obiect_1 = Calculator()
    print(obiect_1)
    quit_q = input('Press Q to quit: ').lower()
    if quit_q == 'q':
        break
# obiect_2 = Calculator(1, 2, '-')
# obiect_3 = Calculator(1, 2, '*')
# obiect_4 = Calculator(3, 7, '/')
# print(obiect_2)
# print(obiect_3)
# print(obiect_4)
