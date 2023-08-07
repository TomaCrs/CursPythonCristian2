cnp = input(f"Introduceti CNP-ul :")                        #putem testa un cnp random valid 6150508456911 sau invalide 123, 61505afd56321 etc
ok = True
if len(cnp) != 13:                                          #verificam daca cnp-ul introdus are 13 caractere
    ok = False
ok = cnp.isdigit()                                          #verificam daca cnp-ul introdus este format doar din cifre
if ok == True:
    #verificam sexul și secolul în care s-a născut persoana
    if not (cnp[0] >='1' and cnp[0] <= '9'):
        ok = False
    #verificam luna nașterii persoanei
    luna = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    luna_cnp = cnp[3]+cnp[4]
    if ok == True and not luna_cnp in luna:
        ok = False
    # verificam ziua nasterii persoane
    if ok == True and cnp[5] == '0' and cnp[6] == '0':
            ok = False
    elif ok == True  and cnp[5] != '0':
        zi_cnp=cnp[5]+cnp[6]
        if luna_cnp in ['04', '06', '09', '11'] and zi_cnp == 31:
            ok = False
        if luna_cnp == '02' and (zi_cnp == 31 or zi_cnp == 30):
            ok = False
        if int(zi_cnp) not in range(10,31):
            ok = False
    #verificam codul judetului unde s-a nascut persoana
    if ok == True and cnp[7] == '0' and cnp[8] == '0':
        ok = False
    elif ok == True and cnp[7] != '0':
        judet_cnp = cnp[7] + cnp[8]
        if int(judet_cnp) not in range(10,47) and int(judet_cnp) != 51 and int(judet_cnp) != 52:
            ok = False
    #verificam numarul unic
    nnn = cnp[9] + cnp[10] + cnp[11]
    if ok == True and nnn == '000':
        ok = False
    #verificam cifra de control
    if ok == True:
        cnp_validare = list()
        for i, x in enumerate(cnp):
            cnp_validare.append(int(x))
        nr_validare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        c_cal = 0
        c = cnp_validare[-1]
        cnp_validare.pop()
        for i,x in enumerate(cnp_validare):
            c_cal += x * nr_validare[i]
        c_control = c_cal % 11
        if c_control == 10:
            c_control = 1
        if not c_control == c:
            ok = False
if ok == True :
    print(f"CNP-ul {''.join(cnp)} este valid.")
else :
    print(f"CNP-ul {''.join(cnp)} nu este valid.")