import random
def game():
    secret_number=random.randint(1,100)
    print(secret_number)
    limit=1
    gamelogic(limit,secret_number)
def gamelogic(limit,secret_number):
    while limit<=5:
       num=int(input("Enter your guess: "))
       if num>secret_number:
           print("Too high!")
       elif num<secret_number:
           print("Too low!")
       else:
           print("You found it!")
           again=input("Do you wanna play again(yes/no): ")
           if again=="yes":
               game()
           else:
               return 0
       limit+=1
    else:
        print("You lost all your attempts!")
print("\t\tNumber Guessing Game\n")
games=game()
   
       
              
    