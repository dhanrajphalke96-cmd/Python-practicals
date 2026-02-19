print("A - Add a student")
print("B - Update marks")
print("C - Search for Student")
print("D - Display all Student Marks")

user = input(("Enter a option from the given manu : ")).lower()

student = {}

if user == 'a' :

    name = input("Enter Name of Student :")
    marks = int(input("Enter marks : "))

    student[name] = marks

    print("Student added succesfully ")

elif user == 'b':

    name = input("Enter name of student : ")
    if name in student :
        marks = int(input("Enter marks :"))
        student[name]=marks
        print("marks Updated")
    else:
        print("Student not found")

elif user == 'c':
    name = input("Enter name of student :")
    if name in student :
        print("Name is present")            
    else :
        print("No name found")

elif user == 'd':
    print(student.items())

else :
    print("Invaild option")    