pozitii = [1, 2, 3, 4, 5, 6, 7, 8, 9]
situatie_joc = [None, None, None, None, None, None, None, None, None]
pozitii_calculator = [5, 1, 3, 7, 9, 2, 4, 6, 8]

simbol_user = input("Alege optiune X sau 0 ").upper()


# afisare pe 3 coloane
def afisare(lista):
    for i in range(3):
        print(lista[i * 3:(i + 1) * 3])
    print("=======================")


def check(lista, simbol):
    # verificam randurile
    if all(lista[i] == simbol for i in range(3)) or all(
            lista[i + 3] == simbol for i in range(3)) or all(lista[i + 6] == simbol for i in range(3)):
        print(f"{simbol} a castigat")
        return True
    # verificam coloanele
    if all(lista[i] == simbol for i in range(0, 7, 3)) or all(
            lista[i] == simbol for i in range(1, 8, 3)) or all(
            lista[i] == simbol for i in range(2, 9, 3)):
        print(f"{simbol} a castigat")
        return True
    # verificam diagonalele
    if all(lista[i] == simbol for i in range(0, 9, 4)):
        print(f"{simbol} a castigat")
        return True
    if all(lista[i] == simbol for i in range(2, 7, 2)):
        print(f"{simbol} a castigat")
        return True
    if None not in lista:
        return True
    return False

def alegere_calculator(lista, simbol_pc, simbol_user):
    simboluri = list()
    for i in range(9):
        if lista[i] == simbol_pc:
            simboluri.append(1)
        elif lista[i] == simbol_user:
            simboluri.append(-1)
        else:
            simboluri.append(0)
    #decizie linii
    for j in [3,6,9]:
        s = 0
        for i in range(j-3,j):
            s += simboluri[i]
        if s == 2 or s == -2:
            for i in range(j-3,j):
                if simboluri[i] == 0:
                    return i
    #decizie coloana
    for j in range(3):
        s = 0
        for i in [0,3,6]:
            s += simboluri[i+j]
        if s == 2 or s == -2:
            for i in [0,3,6]:
                if simboluri[i+j] == 0:
                    return i+j
    #decizie coloana principala
    s = 0
    s += simboluri[0]+simboluri[4]+simboluri[8]
    if s == 2 or s ==-2:
        for i in [0,4,8]:
            if simboluri[i] == 0:
                return i
    # decizie coloana secundara
    s = 0
    s += simboluri[2] + simboluri[4] + simboluri[6]
    if s == 2 or s == -2:
        for i in [2, 4, 6]:
            if simboluri[i] == 0:
                return i
    #alegem din pozitii preferentiale
    i = pozitii_calculator[0]
    pozitii_calculator.remove(i)
    i -= 1
    return i



while simbol_user != 'X' and simbol_user != '0':
    simbol_user = input("Optiunea aleasa este gresita, Te rog alege X sau 0 ").upper

simbol_calculator = "0" if simbol_user == "X" else "X"
print(simbol_user + " " + simbol_calculator)

# Jucatorul are X
if simbol_user == 'X':
    pozitia_aleasa = int(input(f"Alege pozitia {pozitii} "))
    # plasam X pe pozitia aleasa de jucator daca este valida
    while not check(situatie_joc, simbol_user):
        if pozitia_aleasa in pozitii:
            situatie_joc[pozitia_aleasa - 1] = simbol_user
            pozitii.remove(pozitia_aleasa)
            pozitii_calculator.remove(pozitia_aleasa)
            afisare(situatie_joc)
            if check(situatie_joc, simbol_user):
                break
            # plasam pozitia calculatorului
            else:
                optiune_calculator = alegere_calculator(situatie_joc, simbol_calculator, simbol_user)
                situatie_joc[optiune_calculator] = simbol_calculator
                pozitii.remove(optiune_calculator+1)
                afisare(situatie_joc)
                if check(situatie_joc, simbol_calculator):
                    break
        # introduce jucatorul
        else:
            pozitia_aleasa = int(input(f"pozitie ocupata, alege alta {pozitii} "))
            continue
# Jucatorul are 0
else:
    # plasam pozitia calculatorului
    while not check(situatie_joc, simbol_calculator):
        optiune_calculator = alegere_calculator(situatie_joc, simbol_calculator, simbol_user)
        situatie_joc[optiune_calculator] = simbol_calculator
        pozitii.remove(optiune_calculator + 1)
        afisare(situatie_joc)
        if check(situatie_joc, simbol_calculator):
            break
        # plasam 0 pe pozitia aleasa de jucator daca este valida
        pozitia_aleasa = int(input(f"Alege pozitia {pozitii} "))
        if pozitia_aleasa in pozitii:
            situatie_joc[pozitia_aleasa - 1] = simbol_user
            pozitii.remove(pozitia_aleasa)
            pozitii_calculator.remove(pozitia_aleasa)
            afisare(situatie_joc)
            if check(situatie_joc, simbol_user):
                break
        else:
            pozitia_aleasa = int(input(f"pozitie ocupata, alege alta {pozitii} "))
            continue
        afisare(situatie_joc)