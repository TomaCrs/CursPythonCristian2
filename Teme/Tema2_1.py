# 1Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
# caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
# preluat automat de la tastatura.

nume = input("Introduceti-va numele: ")
while nume.isalpha() is False:
    nume = input("Nume invalid. Introduceti-va numele: ")
text = input("Introduceti un text: ")
if text.isalpha() is True:
    print(f"Sirul de caractere a fost gasit de {nume}.")
elif text.isnumeric() is True:
    print(f"Sirul de numere a fost gasit de {nume}.")
else:
    print("Sirul introdus este alfanumeric")
