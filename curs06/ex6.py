"""Se da un cuvant de la tastatura. Sa se indice cate vocale si cate consoane contine."""

cuvant = input("Adauga un cuvant : ")
def counter_litere(word: str) -> (int, int):
    nr_vocale = 0
    nr_consoane = 0
    for i in word:
        if i in 'aeiou':
            nr_vocale += 1
        elif i.isalpha():
            nr_consoane += 1
    return nr_vocale, nr_consoane
print(f"Cuvantul {cuvant} are {counter_litere(cuvant)}")
