# 3. Scrieti un program care sa faca split dupa al n-lea element intr-o lista:
# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3
# result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

def functie_split(input_list, n):
    result = []
    for i in range(n):
        result.append([])
    for i, x in enumerate(input_list):
        result_index = i % n
        result[result_index].append(x)
    return result

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = functie_split(lista_start, n)
print(result)
