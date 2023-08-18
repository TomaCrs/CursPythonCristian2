# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest)

an = input("Introduceti un an: ")
while an.isnumeric() is False:
    an = input(f"Anul {an} este invalid. Introduceti un an: ")
an = int(an)
if an % 400 == 0 or (an % 4 == 0 and an % 100 != 0):
    print(f"Anul {an} este an bisect.")
else:
    print(f"Anul {an} nu este an bisect.")
