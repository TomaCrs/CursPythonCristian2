# 2.Realizati un program care sa creeze o lista, concatenand o lista data, cu nr. de la 1 la n
# exemplu:
# list-var = ['p', 's']
# n = 5
# result = ['p1', 's1', 'p2', 's2', 'p3', 's3', 'p4', 's4', 'p5', 's5']

# list_var = ['p', 's']
list_init = input("Elementele listei sunt separate prin virgula: ")
list_var = list_init.split(',')

n = input("Introduceti un nr intreg si pozitiv: ")
while n.isnumeric() is False:
    n = input("Introduceti un nr intreg si pozitiv: ")
n = int(n)


def concatenare(nr: int, lista: list) -> list:
    list_new =[]
    for i in range(int(nr)):
        for v in lista:
            list_new.append(v + str(i+1))
    return list_new


print(concatenare(n, list_var))
