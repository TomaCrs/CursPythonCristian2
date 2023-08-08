"""Scrieti un program ce va numara cate caractere are un sir de caractere date de utilizator. Aceasta numarare sa se
realizeze cu ajutorul unui for fara a utiliza len(). La final afisati rezultatul"""

sir = input("Adauga un sir de caractere: ")
count = 0
for i in sir:
    count += 1
# print(f"Utilizatorul a introdus de la tastatura sirul '{sir}' care are lungimea {count}")
# print(f"Utilizatorul a introdus de la tastatura sirul \"{sir}\" care are lungimea {count}")
print("Utilizatorul a introdus de la tastatura sirul \"" + sir + "\" care are lungimea " + str(count))