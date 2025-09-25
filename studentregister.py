#Python Labb 1 - Studentregister

import os

#importerad från Mika's GitHub (MikaSamba88)
#funktion som rensar konsolen
def clear_console():
    if os.name == 'nt':
        os.system('cls') #för windows
    else:
        os.system('clear') #för Linux & Mac

MENU_START = True

student_list = [
    {"namn": "Ada", "ålder": 36},
    {"namn": "Johan", "ålder": 25},
    {"namn": "Maria", "ålder": 31}
]

while MENU_START:
    menu_selection = input(("Välkommen till Studentregistret huvudmenu, väl ett val.\n"
                           "1 - för att lägga till en student.\n"
                           "2 - för att ta bort en student.\n"
                           "3 - för att visa alla studenter.\n"
                           "4 - för att söka efter en student.\n"
                           "5 - för att räkna ut genomsnittsåldern.\n"
                           "6 - för att avsluta programmet.\nVälj ovan: "))
    print()
    #Lägg till student.
    if menu_selection == '1':
        new_student = {}
        new_student["namn"] = input("Var vänlig att lägg till en studentens namn: ")
        new_student["ålder"] = int(input("Ålder?: "))
        student_list.append(new_student)
        print("Tack, jag har lagt in studenten nu. Här är den nya listan:\n")
        for student in student_list:
            print(student["namn"], student["ålder"])
        print()
        input("Tryck enter för att komma tillbaka till Huvudmenun.\n")
        clear_console()
    #Ta bort student.
    elif menu_selection == '2':
        for student in student_list:
            print(student["namn"])
        name_to_remove = input("Vem vill du ta bort?: ")
        for student in student_list:
            if student["namn"] == name_to_remove:
                student_list.remove(student)
                break
        print(f"\n{name_to_remove} har tagits bort.")
        input("\nTryck enter för att komma tillbaka till Huvudmenun.")
        clear_console()
    #Listar alla studenter.
    elif menu_selection == '3':
        for student in student_list:
            print(student["namn"], student["ålder"])
        input("\nTryck enter för att komma tillbaka till Huvudmenun.")
        clear_console()
        continue
    #Sök student.
    elif menu_selection == '4':
        namn = input("Vilken namn letar du efter? ")
        for namn_sok in student_list:
            if namn == namn_sok["namn"]:
                print(f"{namn} finns med!")
                input("\nTryck enter för att komma tillbaka till Huvudmenun.")
                break
            else:
                continue
        clear_console()
    #Räkna ut genomsnittsåldern.
    elif menu_selection == '5':
        ålder_total = 0
        for ålder in student_list:
            ålder_total += ålder["ålder"]
        genomsnitt_ålder = ålder_total / len(student_list)
        print(f'Genomsnittsåldern för alla studenter är {round(genomsnitt_ålder)} år.')
        input("\nTryck enter för att komma tillbaka till Huvudmenun.")   
        continue     
    #Avsluta program.
    elif menu_selection == '6':
        break
    #Starta om huvudmenu.
    else:
        clear_console()
        continue
