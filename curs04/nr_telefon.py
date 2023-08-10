"""Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
    +40725547895
-> incepe cu +40 (primele 3 caractere sunt +40)
-> are 12 caractere
-> sa aiba caracterele de la 3 la 12 sa fie doar cifre
"""
nr_telefon = input("Introdu un numar de telefon: ")
while nr_telefon[0:3] != '+40' or len(nr_telefon) != 12 or nr_telefon[3:].isdigit() is False:
    nr_telefon = input(f"Numarul introdus: {nr_telefon} este incorect. Introdu din nou un numar de telefon: ")
print(f"Numarul {nr_telefon} este valid.")