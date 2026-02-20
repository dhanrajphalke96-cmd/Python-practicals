def digits_of_number (n):
    while n > 0:
        number = n % 10
        print(number)
        n = n // 10
n = int(input("Enter a number : "))  
digits_of_number(n)  