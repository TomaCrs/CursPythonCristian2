# 2.Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

nr = input("Te rog introdu un numar intreg: ")
while nr.isdecimal() is False:
    nr = input(f"Numarul {nr} introdus nu este valid. Te rog introdu un numar intreg: ")
nr = int(nr)
if nr % 2 == 0:
    print(f"Numarul {nr} este par.")
else:
    print(f"Numarul {nr} este impar.")
