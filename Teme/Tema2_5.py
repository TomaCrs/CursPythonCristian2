# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

while True:
    alegere = input("Va rugam alegeti una din optiunile de mai jos: \n"
                    "1 – Afisare lista de cumparaturi\n"
                    "2 – Adaugare element\n"
                    "3 – Stergere element\n"
                    "4 – Stergere lista de cumparaturi\n"
                    "5 - Cautare in lista de cumparaturi\n")
    if alegere == '1':
        print("Afisare lista de cumparaturi.")
        break
    elif alegere == '2':
        print("Adugare element.")
        break
    elif alegere == '3':
        print("Stergere element.")
        break
    elif alegere == '4':
        print("Stergere lista de cumparaturi.")
        break
    elif alegere == '5':
        print("Cautare in lista de cumparaturi")
        break
    else:
        print("Alegerea nu exista. Reincercati.")
