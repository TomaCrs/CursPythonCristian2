# 3. Scrieti un program care sa faca split dupa al n-lea element intr-o lista:
# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
# result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
list_init = input("Elementele listei sunt separate prin virgula: ")
lista_start = list_init.split(',')

n = input("Introduceti un nr intreg si pozitiv: ")
while n.isnumeric() is False:
    n = input("Introduceti un nr intreg si pozitiv: ")
n = int(n)


def functie_split(input_list: list, nr: int) ->list:
    result = []
    for i in range(nr):
        result.append([])
    for i, x in enumerate(input_list):
        result_index = i % nr
        result[result_index].append(x)
    return result


print(functie_split(lista_start, n))
