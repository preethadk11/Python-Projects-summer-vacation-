import random
secret_number=random.randint(1,100)
guess=1
limit=5
def num_guess(secret_number):
    num=int(input("Enter your guess(limit:1-100): "))
    if num>secret_number:
        print("Too high!")
    elif num<secret_number:
        print("Too low!")
    else:
        return 0
print("\t\tNumber Guess Game")
print("You have 5 attempts to find it!")
while(guess<=limit):
    print(f'Attempts--{guess}')
    flag=num_guess(secret_number)
    if flag==0:
        print("You found it!")
    elif guess==limit:
        print("You lost all your attempts!")
    if flag==0 or guess==limit:
        again=input("Do you wanna play again(yes/no): ").lower()
        if again=="yes":
            secret_number=random.randint(1,100)
            guess=1
            print(f'Attempts--{guess}')
            num_guess(secret_number)
        else:
            print("Got it! better luck next time...")
            break
    
    guess+=1
  
        






