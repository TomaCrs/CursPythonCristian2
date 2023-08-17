nr = input("Te rog introdu un numar intreg: ")
while nr.isdecimal() is False:
    nr = input(f"Numarul {nr} introdus nu este valid. Te rog introdu un numar intreg: ")
nr = int(nr)
if nr % 3 == 0 and nr % 5 == 0:
    print("FizzBuzz")
elif nr % 3 == 0:
    print('Fizz')
elif nr % 5 == 0:
    print('Buzz')
else: print(nr)