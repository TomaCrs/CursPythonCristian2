from curs06.ex1 import atribuire

"""Se da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura"""

def split_value():
    string_input = input("Adauga un string: ")
    n = atribuire("Adauga indexul final de eliminat: ")
    while len(string_input) < n:
        n = atribuire("Index prea mare. Adauga indexul final de eliminat: ")
    return string_input[n:]
    
print(split_value())
