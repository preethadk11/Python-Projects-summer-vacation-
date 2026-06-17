#NumberGuessingGameUsingClassesAndObjects
import random
class NumberGuessingGame:
    def __init__(self):
        self.secret_number=random.randint(1,100)
        print(self.secret_number)
        self.attempts=5
    def play(self,num):
        if num>self.secret_number:
            print("Too high!")
        elif num<self.secret_number:
            print("Too low!")
        else:
            print("You found it!")
            return 0
    def guess_logic(self):
        while self.attempts>0:
             num=int(input("Enter your guess: "))
             val=self.play(num)
             if val==0:
                 return "won"
             self.attempts-=1
        print("You lost all your attempts!")
        return "lost"
while True:
    game=NumberGuessingGame()
    round=game.guess_logic()
    if round=="lost":
        print("Thanks for playing!")
        break
    again=input("Do you wanna play again!(yes/no): ")
    if again!="yes":
        print("Thanks for playing!")
        break

        
