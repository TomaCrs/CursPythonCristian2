"""
utilizatorul cere de la tastatura 2 cifre si un operator (+, - *, /)
"""


def definire_operator(counter_parametru):
    operator = input(f"Aduaga {counter_parametru} numar: ")
    while operator.isdigit() is False:
        operator = input(f"Numarul {operator} este incorect. Aduaga din nou {counter_parametru} numar: ")
    return operator


operator_1 = definire_operator('primul')
operator_2 = definire_operator('al doilea')

operand = input("Adauga operandul (+, -, *, /): ")
while operand not in '+-*/' or len(operand) != 1:
    if len(operand) != 1:
        print("Ai introdus mai multe caractere.")
    operand = input("Adauga operandul (+, -, *, /): ")

if operand == '+':
    rezultat = int(operator_1) + int(operator_2)
elif operand == '-':
    rezultat = int(operator_1) - int(operator_2)
elif operand == '*':
    rezultat = int(operator_1) * int(operator_2)
else:
    while operator_2 == '0':
        operator_2 = input(f"Ai introdus valoarea {operator_2}. Aduaga al doilea numar: ")
    rezultat = int(operator_1) / int(operator_2)

print(f"{operator_1} {operand} {operator_2} = {rezultat}")
