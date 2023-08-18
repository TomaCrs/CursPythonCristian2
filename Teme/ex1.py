# 1.Realizati un program care sa gaseasca al doilea cel mai mic numar din lista.

list_1 = [-8, 1, 2, -2, 0]
list_2 = [1, 1, 0, 0, 2, -2, -2]
list_3 = [1, -1, 0, -9, 4, -5]
list_4 = [1, 4, 0, 23, 6, 34]
for i,x in enumerate(sorted(list_1)):
    if x != min(list_1):
        print(f"Minimul din lista {list_1} este {x}.")
        break
for i,x in enumerate(sorted(list_2)):
    if x != min(list_2):
        print(f"Minimul din lista {list_2} este {x}.")
        break
for i, x in enumerate(sorted(list_3)):
    if x != min(list_3):
        print(f"Minimul din lista {list_3} este {x}.")
        break
for i,x in enumerate(sorted(list_4)):
    if x != min(list_4):
        print(f"Minimul din lista {list_4} este {x}.")
        break
