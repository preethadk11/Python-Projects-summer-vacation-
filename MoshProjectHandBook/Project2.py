#Number Guessing Game
import random
best_score=None
while True:
    minimum,maximum=map(int,input("Enter the minimum and maximum value for number range: ").split())
    secret=random.randint(minimum,maximum)
    print(secret)
    attempt=1
    while attempt<=5:
        num=input("Enter you guess: ")
        if num.isdigit():
            num=int(num)
            if num>secret:
                print("Too high! Try again.")
            elif num<secret:
                print("Too low! Try again.")
            else:
                print(f'You found in {attempt} attempts!')
                if best_score is None or attempt<best_score:
                    best_score=attempt
                    print(f'Best Score is {best_score}')
                break
        else:
            print("The number must be a digit")
        attempt+=1
    again=input("Do you wanna play again?(y/n): ").lower()
    if again!="y":
        print("Thanks for playing!")
        break