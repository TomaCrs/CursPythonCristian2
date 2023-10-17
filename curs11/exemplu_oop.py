"""
Rudolph este o pisica mare care doarme toata ziua.
clasa -> pisica
obiect -> Rudolph
proprietatea -> mare
activitatea -> doarme
"""


# class Pisica:
#     pass
#
#
# Felix = Pisica()
# Tom = Pisica()
# Max = Pisica()


stiva = []


def push(val):
    stiva.append(val)


def pop():
    value = stiva[-1]
    stiva.pop()
    return value


push(3)
push(2)
push(1)
print(stiva)
print(pop())
print(pop())
print(pop())
