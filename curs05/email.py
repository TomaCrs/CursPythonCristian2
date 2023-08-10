"""Creati un program in care utilizatorul sa introduca o adresa de email de formatul
litere_sau_cifre@litere_sau_cifre.litere
Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa existe o singura data
in sirul de caractere."""
email_adress = input("Adauga adresa de email: ")
# if email_adress.split('@')[0] .isalnum() is False:
#     email_adress = input(f"Adresa de email {email_adress} nu este valida. Adauga din nou adresa de email: ")
while email_adress.count('@') != 1 or \
        email_adress.count('.') != 1 or \
        email_adress.index('@') > email_adress.index('.') or \
        email_adress.split('@')[0] .isalnum() is False or\
        email_adress.split('@')[1].split('.')[0].isalnum() is False or \
        email_adress.split('@')[1].split('.')[1].isalpha() is False:
    email_adress = input(f"Adresa de email {email_adress} nu este valida. Adauga din nou adresa de email: ")
print(f"Adresa de email {email_adress} este valida.")

