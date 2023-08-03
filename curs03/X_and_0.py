pozitii = [1, 2, 3,
           4, 5, 6,
           7, 8, 9]

situatie_joc = [None, None, None, None, None, None, None, None, None]

pozitii_calculator = [5, 2,4,1, 3, 7, 9,  6, 8]

optiune = input("Alege optiune X sau 0 ").upper()

def joc_castigat(situatie_joc, optiune):
        # verificam randurile
        if all(situatie_joc[i] == optiune for i in range(3)) or all(situatie_joc[i+3] == optiune for i in range(3)) or all(situatie_joc[i+6] == optiune for i in range(3)):
            return True
        # verificam coloanele
        col = [0, 3, 6]
        if all(situatie_joc[v] == optiune for i,v in enumerate(col)) or all(situatie_joc[v + 1] == optiune for i,v in enumerate(col)) or all(situatie_joc[v + 2] == optiune for i,v in enumerate(col)):
            return True
        #verificam diagonalele
        if all(situatie_joc[i] == optiune for i in range(0,9,4)):
            return True
        if all(situatie_joc[i] == optiune for i in range(2,7,2)):
            return True
        return False
def Stopjoc(situatie_joc):
    if None in situatie_joc:
        return False
    else:
        return True


while optiune != 'X' and optiune != '0':
    optiune = input("Optiunea aleasa este gresita, Te rog alege X sau 0 ").upper()

if optiune == 'X':
    pozitia_aleasa = int(input(f"Alege pozitia {pozitii} "))

while not Stopjoc(situatie_joc):

    if pozitia_aleasa in pozitii:
        situatie_joc[pozitia_aleasa - 1] = optiune
        pozitii.remove(pozitia_aleasa)
        pozitii_calculator.remove(pozitia_aleasa)

        if Stopjoc(situatie_joc):
            print("sfarsit")
            break

        else:
            optiune_calculator = pozitii_calculator[0]
            situatie_joc[optiune_calculator - 1] = "0"
            pozitii.remove(optiune_calculator)
            pozitii_calculator.remove(optiune_calculator)

            if Stopjoc(situatie_joc):
                print("sfarsit")
                break

    # introduce jucatorul

    else:
        if joc_castigat(situatie_joc, optiune):
            print("Ai castigat")
            break
        pozitia_aleasa = int(input(f"pozitie ocupata, alege alta {pozitii} "))
        continue

    print(situatie_joc)
