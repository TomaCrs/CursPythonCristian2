from curs06.ex1 import atribuire

"""Scrieti un program care itereaza prin primele 10 numere. La fiecare iteratie afiseaza suma dintre iteratorul curent
si urmatorul iterator din sir."""


def iterare():
    nr = atribuire("Alege iteratorul final: ")
    text = []
    for i in range(1, nr+1):
        if i < nr:
            suma = i + i + 1
            text.append(f"{i} + {i+1} = {suma}")
    return '\n'.join(text)


if __name__ == '__main__':
    print(iterare())


# """
#     suma din sirul: de exemplu [12, 25, 36, 78, 1, 23, 5, 41]
#     12 + 25
#     25 + 36
#     36 + 78
#     ...
# """
#
# sir = [12, 25, 36, 78, 1, 23, 5, 41]
# if len(sir) > 1:
#     for i,v in enumerate(sir):
#         if i < len(sir) - 1:
#             suma = v + sir[i+1]
#             print(f"{v} + {sir[i+1]} = {suma}")
