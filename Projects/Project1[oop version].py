import random
class NumberGuessGame:
    def __init__(self):
        self.secret=random.randint(1,100)
        print(self.secret)
        self.attempts=5
    def check_guess(self,guess):
        if guess<self.secret:
            print("Too low!")
        elif guess>self.secret:
            print("Too high!")
        else:
            print("Yes you found!")
            return 0
    def play(self):
        while self.attempts>0:
            guess=int(input("Enter your guess: "))
            val=self.check_guess(guess)
            if val==0:
                return "won"
            self.attempts-=1
        print("You lost all your attempts!")
        return "lost"
print("\t\tNumberGuessingGame\n")
while True:
    game=NumberGuessGame()
    round=game.play()
    if round=="lost":
        break
    again=input("Do you wanna play again(yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
