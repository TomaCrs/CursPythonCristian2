"""Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2 numere este
mai mic sau egal cu 1000, altfel, sa se returneze suma acestora."""


def atribuire(mesaj: str) -> int:
    nr = input(mesaj)
    while not nr.isnumeric():
        nr = input(mesaj)
    return int(nr)


def product_or_sum() -> str:
    input_1 = atribuire("Alege primul nr:")
    input_2 = atribuire("Alege al doilea nr:")
    rezultat = input_1 + input_2
    text = f"Suma este: {rezultat}"
    if (rezultat := input_1 * input_2) and rezultat <= 1000:
        text = f"Produsul este: {rezultat}"
    return text

if __name__ == '__main__':
    print(product_or_sum())
