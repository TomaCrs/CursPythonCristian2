from curs06.ex1 import atribuire

"""Scrieti un program care sa extraga inversul dintr-un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""


def invers():
    value = str(atribuire("Adauga numarul: "))
    lista = []
    for i in value:
        lista.insert(0, i)
    return ' '.join(lista)


print(invers())
