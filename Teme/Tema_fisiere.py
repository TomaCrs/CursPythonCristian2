from datetime import datetime
taskuri = []
categorii = []


def add_category():
    print("Introduceti categoriile de taskuri (introduceti \"stop\" pentru a va opri): ")
    while True:
        x = input()
        if x.lower() == "stop":
            break
        elif x not in categorii:
            categorii.append(x)
        else:
            print("Categoria exista deja.")
    return True


def add_task():
    while True:
        task = {'text': input("Introduceti taskul: "),
                'data': input("Introduceti data limita a taskului (format: YYYY-MM-DD HH:MM) : "),
                'persoana': input("Introduceti persoana responsabila pentru task: "),
                'categorie': input(f"Introduceti o categorie din care face parte taskul ({categorii}): ")}
        while task['categorie'] not in categorii:
            task['categorie'] = input(
                f"Categoria aleasa nu exista. Va rog introduceti o categorie din lista ({categorii}): ")
        check = False
        for value in taskuri:
            if value['text'] == task['text']:
                check = True
        while check:
            task['text'] = input("Taskul exista deja, va rog reformulati: ")
            check = False
            for value in taskuri:
                if value['text'] == task['text']:
                    check = True
        while True:
            try:
                datetime.strptime(task['data'], "%Y-%m-%d %H:%M")
                break
            except ValueError:
                task['data'] = input("Va rog introduceti o data valida, dupa formatul YYYY-MM-DD HH:MM: ")
        taskuri.append(task)
        choice = input("Doriti sa continuati sa introduceti taskuri ? (Da/Nu): ").lower()
        while choice != "da" and choice != "nu":
            choice = input("Va rog alegeti Da sau Nu: ")
        if choice == "nu":
            break
    return True


def create_files():
    with open("categorii.txt", 'w') as category_file:
        for value_category in categorii:
            category_file.write(value_category)
            category_file.write("\n")
    with open("taskuri.txt", 'w') as task_file:
        for value_dict in taskuri:
            for value in value_dict:
                task_file.write(value_dict[value])
                task_file.write(" ")
            task_file.write("\n")
    return True


def listare():
    taskuri_sorted = sorted(taskuri, key=lambda categorie: categorie['categorie'])
    for value in taskuri_sorted:
        print(' '.join(value_dict for value_dict in value.values()))
    return True


def sortare():
    print("Alegeti una din metodele de sortare: ")
    print("1. Sortare ascendentă task")
    print("2. Sortare descendentă task")
    print("3. Sortare ascendentă data")
    print("4. Sortare descendentă data")
    print("5. Sortare ascendentă persoana responsabilă")
    print("6. Sortare descendentă persoană responsabilă")
    print("7. Sortare ascendentă categorie")
    print("8. Sortare descendentă categorie")
    choice_sort = input()
    task_sortat = []
    if choice_sort == '1':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['text'])
    elif choice_sort == '2':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['text'], reverse=True)
    elif choice_sort == '3':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['data'])
    elif choice_sort == '4':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['data'], reverse=True)
    elif choice_sort == '5':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['persoana'])
    elif choice_sort == '6':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['persoana'], reverse=True)
    elif choice_sort == '7':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['categorie'])
    elif choice_sort == '8':
        task_sortat = sorted(taskuri, key=lambda alegere: alegere['categorie'], reverse=True)
    else:
        print("Alegerea nu exista.")
    for value in task_sortat:
        print(' '.join(value_dict for value_dict in value.values()))
    return True


def filtrare():
    pass


def editare():
    pass


def stergere():
    pass


def meniu():
    while True:
        print("Meniu taskuri. Alegeti operatiunea dorita: ")
        print("0.Inchidere meniu.")
        print("1.Listare date.")
        print("2.Listare date sortate.")
        print("3.Filtrare date.")
        print("4.Adauga un nou task.")
        print("5.Editeaza un task.")
        print("6.Sterge un task.")
        choice_menu = input()
        if choice_menu == '0':
            break
        elif choice_menu == '1':
            listare()
        elif choice_menu == '2':
            sortare()
        elif choice_menu == '3':
            filtrare()
        elif choice_menu == '4':
            add_task()
        elif choice_menu == '5':
            editare()
        elif choice_menu == '6':
            stergere()
        else:
            print("Alegerea nu exista.")


add_category()
add_task()
create_files()
meniu()
