import random

situatie_joc = [None, None, None, None, None, None, None, None, None]
pozitii_calculator = [5, 1, 3, 7, 9, 2, 4, 6, 8]


# afisare pe 3 coloane
def afisare(lista):
    for i in range(3):
        print(lista[i * 3:(i + 1) * 3])
    print("=======================")


def check(lista, simbol, name):
    # verificam randurile
    if ((all(lista[i] == simbol for i in range(3)) or
         all(lista[i + 3] == simbol for i in range(3)) or
         all(lista[i + 6] == simbol for i in range(3))) or
            # verificam coloanele
            (all(lista[i] == simbol for i in range(0, 7, 3)) or
             all(lista[i] == simbol for i in range(1, 8, 3)) or
             all(lista[i] == simbol for i in range(2, 9, 3))) or
            # verificam diagonalele
            all(lista[i] == simbol for i in range(0, 9, 4)) or
            all(lista[i] == simbol for i in range(2, 7, 2))):
        print(f"{name} a castigat")
        return True
    # verificam daca toate pozitiile sunt ocupate
    if None not in lista:
        print("Nu a castigat nimeni!")
        return True
    return False


# returneaza o lista pt fiecare pozitie: 1 pt pc, 0 pt none si -1 pt user
def suma_partiala(lista, simbol_pc, simbol_usr):
    simboluri = list()
    for i in range(9):
        if lista[i] == simbol_pc:
            simboluri.append(1)
        elif lista[i] == simbol_usr:
            simboluri.append(-1)
        else:
            simboluri.append(0)
    return simboluri


# verifica situatia jocului in cazul in care ar fi 2 elemente pe fiecare linie, coloana, diagonala si o pozitie libera
def alegere_partiala(lista, valoare):
    # decizie linii
    for j in [3, 6, 9]:
        s = 0
        for i in range(j - 3, j):
            s += lista[i]
        if s == valoare:
            for i in range(j - 3, j):
                if lista[i] == 0:
                    return i
    # decizie coloana
    for j in range(3):
        s = 0
        for i in [0, 3, 6]:
            s += lista[i + j]
        if s == valoare:
            for i in [0, 3, 6]:
                if lista[i + j] == 0:
                    return i + j
    # decizie diagonala principala
    s = 0
    s += lista[0] + lista[4] + lista[8]
    if s == valoare:
        for i in [0, 4, 8]:
            if lista[i] == 0:
                return i
    # decizie diagonala secundara
    s = 0
    s += lista[2] + lista[4] + lista[6]
    if s == valoare:
        for i in [2, 4, 6]:
            if lista[i] == 0:
                return i


def alegere_calculator(lista, pozitii_pc, simbol_pc, simbol_usr):
    simboluri = suma_partiala(lista, simbol_pc, simbol_usr)
    # verifica daca exista posibilitatea ca pc sa castige la urmatoarea mutare
    i = alegere_partiala(simboluri, 2)
    if i is not None:
        return i
    # verifica daca exista posibilitatea ca userul sa castige la urmatoarea mutare
    i = alegere_partiala(simboluri, -2)
    if i is not None:
        return i
    # alegem din pozitii preferentiale sau random daca e prima alegere a calculatorului
    if len(pozitii_pc) > 7:
        i = pozitii_pc[random.randrange(len(pozitii_pc))]
    else:
        i = pozitii_pc[0]
    return i - 1


# verifica daca pozitia introdusa este corecta si plaseaza simbolul in casuta corecta
def alegere_user(lista_pozitii, sit_joc, simb_user):
    poz_aleasa = input(f"Alege pozitia {sorted(lista_pozitii)} ")
    while (not poz_aleasa.isnumeric() or
           int(poz_aleasa) not in lista_pozitii):
        poz_aleasa = input(f"Optiune incorecta, te rog alege una din variantele: {sorted(lista_pozitii)} ")
    poz_aleasa = int(poz_aleasa)
    sit_joc[poz_aleasa - 1] = simb_user
    lista_pozitii.remove(poz_aleasa)
    return poz_aleasa


# jucatorul introduce simbolul cu care vrea sa joace
simbol_user = input("Alege optiune X sau 0 ").upper()
# verificam daca inputul de la jucator este corect
while simbol_user != 'X' and simbol_user != '0':
    simbol_user = input("Optiunea aleasa este gresita, Te rog alege X sau 0 ").upper()
simbol_calculator = "0" if simbol_user == "X" else "X"

# plasam pozitia calculatorului
while not check(situatie_joc, simbol_user, "Jucatorul"):
    # se executa doar daca jucatorul are x la prima alegere
    if simbol_user == 'X' and len(pozitii_calculator) == 9:
        alegere_user(pozitii_calculator, situatie_joc, simbol_user)
        afisare(situatie_joc)

    optiune_calculator = alegere_calculator(situatie_joc, pozitii_calculator, simbol_calculator, simbol_user)
    situatie_joc[optiune_calculator] = simbol_calculator
    pozitii_calculator.remove(optiune_calculator + 1)
    afisare(situatie_joc)

    if check(situatie_joc, simbol_calculator, "Calculatorul"):
        break
    # plasam 0 pe pozitia aleasa de jucator daca este valida
    alegere_user(pozitii_calculator, situatie_joc, simbol_user)
    afisare(situatie_joc)
