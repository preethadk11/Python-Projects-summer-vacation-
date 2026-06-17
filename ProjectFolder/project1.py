#NumberGuessingGame
import random
def game():
    secret_number=random.randint(1,100)
    print(secret_number)
    attempts=0
    while attempts<=5:
        num=int(input("Enter your guess: "))
        if num>secret_number:
            print("Too high!")
        elif num<secret_number:
            print("Too low!")
        else:
            print(f'You won in {attempts+1} attempts!')
            return attempts
        attempts+=1
    print("You lost all your attempts!")
    print("The secret number was ",secret_number)
while True:
    val=game()
    again=input("Do you wanna play again(yes/no): ").lower()
    if again!="yes":
        print("Thanks for playing!")
        break
