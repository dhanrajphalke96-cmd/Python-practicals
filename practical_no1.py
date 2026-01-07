import random 

computer = random.randint(1, 100)
no_of_guesses = 0


while True:

    user = int(input("Enter a number between 1 and 100: "))
    no_of_guesses += 1
    if no_of_guesses > 10:
        print("Sorry, GAME OVER! The number was", computer)
        break

    if user < 1 or user > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    if computer == user:
        print("Congratulations! You guessed the correct number.")
        print("Number of guesses taken:", no_of_guesses)
        break
        
    elif computer > user:
        print("your guess is too low ")

    else:
        print("your guess is too high ")
        