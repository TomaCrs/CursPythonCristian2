import io

"""
r  -> read only
w  -> write only
a  -> write with append
r+ -> read/write
"""

# with open("data.txt", 'w') as file:
#     file.write("Hello\n")
#     file.write("World")

# file = open('data.txt' , 'r')
# try:
#     file.write("Hello")
# except io.UnsupportedOperation as error:
#     print(error)
#     file = open('data.txt', 'r+')
#     file.write("Hello dupa try except.")
# finally:
#     file.close()

# with open('data1.txt' , 'r') as item:
#     try:
#         item.write('Hei')
#     except io.UnsupportedOperation as error:
#         print(error)
#         file = open('data1.txt', 'r+')
#         file.write("Hei dupa try except.")

# with open("data1.txt", 'r') as file:
#     # print(file.readlines())
#     # x = file.readlines()
#     x = list(file)
#     print(x)
#     for line in x:
#         print(line)


with open("data1.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)