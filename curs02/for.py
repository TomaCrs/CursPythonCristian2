for i in range(0, 10, 2):
    print(f"Set instructiuni {i}")

lista = [45, 62, 73]
for index, value in enumerate(lista):
    print(index, value)

dict_1 = {"key_1": 45,
          "key_2": 62,
          "key_3": 73}
# for i in dict_1:
# for i in dict_1.keys():
# for i in dict_1.values():
for i, v in dict_1.items():
    print(i, v)
