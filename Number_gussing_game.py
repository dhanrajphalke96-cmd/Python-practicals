import random

computer= random.randint(1,100)
count = 0

while True:
    user = int(input("Enter a no between 1 to 100 :" ))

    if user < 1 or user > 100:
        print("enter a vailed no between 1 to 100")
        continue
    count +=1
    if user == computer:
        print("correct guess",user)
        print("Gussed in :", count)
        break
    elif user < computer :
        print("Too low")
    else:
        print("Too high")        