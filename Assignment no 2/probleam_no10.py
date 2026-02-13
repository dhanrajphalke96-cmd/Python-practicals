n = int(input("Enter a number : "))
count=0 

while True:

    a = int(input("Enter a number : "))

    count +=1
    if a == n:
        print("Correct")
        break
    
    else:

        if a > n:
            print("Too high ")
        elif a < n :
            print("Too low") 
        else:
            print("Enter a valid number")
print("The attempt it's taken",count)