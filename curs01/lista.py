my_list = [1, '3', 0, 4, 1, True, None, [1,2,4]]
# print(my_list[0])
# print(my_list[8]) eroare out of range
# print(my_list[-1]) ultima valoare
# print(my_list[0:3:2]) range de la 0 la 2 (fara val specificata) si pasul
# print(my_list[6:8])
# print(len(my_list)) lungimea listei
# print(my_list[6][1]) accesarea sublistei din lista
# print(my_list[-3:])
# print(my_list.index(1))
my_list.append(56)
my_list.insert(2, 22)
my_list.remove('3')
my_list.pop(0)
print(my_list)