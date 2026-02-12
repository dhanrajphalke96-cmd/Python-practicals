while True:

    n = input("Enter a no or enter q to quit : ")
    if n.lower() == 'q':
        break
    else:
        no = int(n)
        if no > 0:
            print("Positive Number")
        elif no < 0:
            print("Negative Number")
        else :
            print("Number is 0")         