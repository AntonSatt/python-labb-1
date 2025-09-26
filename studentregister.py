#Python Labb 1 - Studentregister

import os

#imported from Mika's GitHub (MikaSamba88)
#function that clears the console.
def clear_console():
    if os.name == 'nt':
        os.system('cls') #for windows
    else:
        os.system('clear') #for Linux & Mac

def get_non_empty_string(input_text):
    name = ""
    #while is true while name is an empty string
    while not name:
        name = input(input_text)
    #controlling if name is an empty string
        if not name:
            print("Can't be left empty, please try again.")
    return name

MENU_START = True

student_list = [
    {"name": "Ada", "age": 36},
    {"name": "Johan", "age": 25},
    {"name": "Maria", "age": 31}
]

while MENU_START:
    menu_selection = input(("Welcome to the Studentregister main menu, please pick an option:\n"
                           "1 - to add a student.\n"
                           "2 - to delete a student.\n"
                           "3 - to show all students.\n"
                           "4 - to search for a student.\n"
                           "5 - to calculate the average age.\n"
                           "6 - to quit the program\nPick above: "))
    print()
    #Add student.
    if menu_selection == '1':
        new_student = {}
        new_student["name"] = get_non_empty_string("Please enter a name: ")
        new_student["age"] = int(input("Please enter age: "))
        student_list.append(new_student)
        print("Thank you, here's the new list:\n")
        for student in student_list:
            print(student["name"], student["age"])
        print()
        input("Press enter to get back to the main menu.\n")
        clear_console()
    #Remove student.
    elif menu_selection == '2':
        for student in student_list:
            print(student["name"])
        name_to_remove = input("Who do you want to remove?: ")
        for student in student_list:
            if student["name"] == name_to_remove:
                student_list.remove(student)
                break
        print(f"\n{name_to_remove} has been deleted.")
        input("Press enter to get back to the main menu.\n")
        clear_console()
    #List all students.
    elif menu_selection == '3':
        for student in student_list:
            print(student["name"], student["age"])
        input("Press enter to get back to the main menu.\n")
        clear_console()
    #Search for a student.
    elif menu_selection == '4':
        name = input("What are you searching for?: ")
        for name_search in student_list:
            if name == name_search["name"]:
                print(f"{name} is here!")
                input("Press enter to get back to the main menu.\n")
                break
            else:
                continue
        clear_console()
    #Calculate the average age.
    elif menu_selection == '5':
        total_age = 0
        for age in student_list:
            total_age += age["age"]
        average_age = total_age / len(student_list)
        print(f"The average age for all students is {round(average_age)} years.")
        input("Press enter to get back to the main menu.\n") 
        clear_console()  
    #Quit the program.
    elif menu_selection == '6':
        break
    #Restart back to main menu.
    else:
        clear_console()
        continue
