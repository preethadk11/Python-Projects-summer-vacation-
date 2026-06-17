import random
def game():
    secret_number=random.randint(1,100)
    print(secret_number)
    limit=1
    while limit<=5:
       num=int(input("Enter your guess: "))
       if num>secret_number:
           print("Too high!")
       elif num<secret_number:
           print("Too low!")
       else:
           print("You found it!")
           return
       limit+=1
    print("You lost all your attempts!")
    return 0
print("\t\tNumber Guessing Game\n")
while True:
    value=game()
    if value==0:
        print("Thanks for playing!")
        break
    again=input("Do you wanna play again(yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break