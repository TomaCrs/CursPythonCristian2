# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

nr = input("Te rog introdu un numar intreg (pozitiv sau negativ): ")
ok = nr.isnumeric()
while ok is False:
    if nr[0] == '-' and nr[1:].isnumeric():
        ok = True
    elif nr.isnumeric():
        ok = True
    if ok is False:
        nr = input("Te rog introdu un numar intreg (pozitiv sau negativ): ")
if nr[0] == '-':
    nr_nou = nr[1:]
    nr_nou = int(nr_nou)
    print("Numarul transformat este: ", nr_nou)
elif nr == '0':
    print("Numarul este 0.")
elif 0 < int(nr) < 10:
    print(f"Numarul {nr} este mai mic decat 10. ")
else:
    print(f"Numarul {nr} este pozitiv.")
