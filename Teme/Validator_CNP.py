cnp = list('5011210460011')
cnp_validare = list()
for i,x in enumerate(cnp):
    cnp_validare.append(int(x))
nr = list('279146358279')
nr_validare = list()
for i,x in enumerate(nr):
    nr_validare.append(int(x))
c_cal = 0
c = cnp_validare[-1]
cnp_validare.pop()
for i,x in enumerate(cnp_validare):
    c_cal += x * nr_validare[i]
c_control = c_cal % 11
if c_control == 10:
    c_control =1
if c_control == c:
    print(f"CNP-ul {''.join(cnp)} este valid.")