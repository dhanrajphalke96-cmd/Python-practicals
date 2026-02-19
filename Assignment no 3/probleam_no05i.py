student ={}

while True:

    print("--------Student Information----------")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for Student")
    print("D - Display all Student Marks")
    print("E - Exit Program")

    user = input("Enter a option :").lower()

    if user == 'a':
        name = input("Enter name of student :")
        marks = int(input("Enter marks :"))
        student[name]= marks
        print("Student added succesfully ")

    elif user == 'b':
        name = input("Enter name of Student :")
        if name in student :
            marks = int(input("Enter marks :"))
            student[name]=marks
            print("Marks updated")
        else :
            print("Name is not found in student")

    elif user == 'c':
        name = input("Enter name of student :")
        if name in student :
            print("Name is found in Student")
            print("Marks:", student[name])   
        else :
            print("Name is not in student")

    elif user == 'd' :
        if student :
            print("\nstudent marks :")
            for name,marks in student.items() :
                print(f"{name}:{marks}")
        else :
            print("Student not found")
    elif user == 'e' :
        print("Existing Program")
        break

    else :
        print("Enter a vaild option")                               