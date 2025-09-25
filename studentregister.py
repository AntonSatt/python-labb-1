#Python Labb 1 - Studentregister

menu_start = True

student_list = [
    {"namn": "Ada", "ålder": 36}, 
    {"namn": "Johan", "ålder": 25}, 
    {"namn": "Maria", "ålder": 31}
]

while menu_start:
    menu_selection = input("Välkommen till Studentregistret huvudmenu, väl ett val.\n1. för att lägga till en student.\n2. för att visa alla studenter\n3. för att avsluta programmet.\nVälj ovan: ")
    print()
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
    elif menu_selection == '2':
        for student in student_list:
            print(student["namn"], student["ålder"])
        input("")
        continue
    elif menu_selection == '3':
        break
    else:
        continue










