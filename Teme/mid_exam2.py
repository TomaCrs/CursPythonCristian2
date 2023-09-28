# ex1
nr_chei = input("Introduceti nr chei(maxim 20): ")
while nr_chei.isdigit() is False or int(nr_chei) not in range(21):
    nr_chei = input("Introduceti nr chei(maxim 20): ")
dictionar = {}
for index in range(1, int(nr_chei) + 1):
    dictionar.update({f'{index}': index * index})
print(dictionar)


# ex2
def suma_tuplu(tuplu: tuple) -> int:
    suma = 0
    for x_tuple in tuplu:
        suma += x_tuple
    return suma


tuple_example = (8, 2, 3, 0, 7)
print(suma_tuplu(tuple_example))


# ex3
def separere_lista(lista: list, numar: int) -> list:
    result = [lista[0:numar], lista[numar:]]
    return result


list_example = [1, 1, 2, 3, 4, 4, 5, 1]
nr = input("Introduceti numarul: ")
while nr.isdigit() is False or int(nr) > len(list_example):
    nr = input("Introduceti numarul: ")
print(separere_lista(list_example, int(nr)))

# ex4
sir = "cristian"
counter = 0
for x in sir:
    if x in "aeiou":
        counter += 1
print(f"{counter} vocale")

# ex5
print("Introduceti 3 numere: ")
x = int(input())
y = int(input())
z = int(input())
if x == 0 or y == 0 or z == 0:
    print(0)
elif x == y == z:
    print(3 * x / y / z)
else:
    print(x / y / z)

# ex6
n = [1, 2, 3, 4, 5, 6, 7]
i = 0
while i < len(n):
    x = n[i]
    if x % 2 == 0:
        n.insert(i + 1, x * 2)
        i += 1
    i += 1
print(n)
