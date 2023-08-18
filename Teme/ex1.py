# 1.Realizati un program care sa gaseasca al doilea cel mai mic numar din lista.

def sortare(lista):
    for i, x in enumerate(sorted(lista)):
        if x != min(lista):
            print(f"Minimul din lista {lista} este {x}.")
            break

list_1 = [-8, 1, 2, -2, 0]
list_2 = [1, 1, 0, 0, 2, -2, -2]
list_3 = [1, -1, 0, -9, 4, -5]
list_4 = [1, 4, 0, 23, 6, 34]
sortare(list_1)
sortare(list_2)
sortare(list_3)
sortare(list_4)
