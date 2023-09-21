def element_majoritar(x: list) -> str:
    elemente = []
    aparitie_maxima = 0
    for value in x:
        if x.count(value) > aparitie_maxima:
            aparitie_maxima = x.count(value)
    for value in x:
        if x.count(value) == aparitie_maxima and str(value) not in elemente:
            elemente.append(str(value))
    if elemente:
        return ','.join(elemente)
    else:
        return "Elementele majoritare nu au fost gasite."


lista = input("Introduceti o lista de numere: ")
lista = lista.split()
while any(not x.isdigit() for x in lista) or len(lista) == 0:
    lista = input("Introduceti o lista de numere: ")
    lista = lista.split()
print(element_majoritar(lista))
