"""Se da un string de la tastatura. Sa se calculeza suma digitilor din acel string"""

cuvant = input("Adauga un cuvant : ")
def suma_cifre(word: str) ->str:
    suma_digit = 0
    var=''
    for i in word:
        if i.isdigit():
            suma_digit += int(i)
            var += i
    return f"{' + '.join(var)} = {suma_digit}"

print(suma_cifre(cuvant))
