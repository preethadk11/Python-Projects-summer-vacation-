#Rock Paper Scissors
import random
def machine():
    items=["👊","✋","✌️"]
    attempt=machine_count=user_count=0
    while attempt<3:
        choice=input("Rock, paper, or scissors? (r/p/s): ").lower()
        if choice=="r":
            print("You chose 👊")
        elif choice=="p":
            print("You chose ✋")
        elif choice=="s":
            print("You chose ✌️")
        else:
            print("Invalid Choice!")
            continue
        computer=random.choice(items)
        print(f'Computer chose {computer}')
        if choice=="r" and computer=="✋":
            print("You lose")
            machine_count+=1
        elif choice=="p" and computer=="✌️":
            print("You lose")
            machine_count+=1
        elif choice=="s" and computer=="👊":
            print("You lose")
            machine_count+=1
        elif choice=="r" and computer=="👊" or choice=="p" and computer=="✋" or choice=="s" and computer=="✌️":
            print("Tie")
        else:
            print("You win")
            user_count+=1
        attempt+=1
    if user_count>machine_count:
        print(f'You won this match with {user_count} point out of 3 points\nComputer lose this match with {machine_count} points')
    elif user_count==machine_count:
        print(f'Match ends with draw')
    else:
        print(f'The computer win this match with {machine_count} out of 3 points\nYou lose this match with {user_count} points')


def two_player():
    attempt=player1=player2=0
    while attempt<3:
        while True:
            print("Player1:")
            choice1=input("Rock paper scissor? (r/p/s): ").lower()
            if choice1=="r":
                print("Player 1 chose: 👊")
                break
            elif choice1=="p":
                print("Player 1 chose: ✋")
                break
            elif choice1=="s":
                print("player 1 chose: ✌️")
                break
            else:
                print("Invalid choice!")
        input("Press enter when player2 is ready...")
        print("\n"*50)
        while True: 
            print("Player2:")
            choice2=input("Rock paper scissor? (r/p/s): ").lower()
            if choice2=="r":
                print("Player 2 chose: 👊")
                break
            elif choice2=="p":
                print("Player 2 chose: ✋")
                break
            elif choice2=="s":
                print("Player 2 chose: ✌️")
                break
            else:
                print("Invalid choise")
        if choice1==choice2:
            print("Tie")
        elif choice1=="r" and choice2=="p":
            print("Player2 wins")
            player2+=1
        elif choice1=="p" and choice2=="s":
            print("Player2 wins")
            player2+=1
        elif choice1=="s" and choice2=="r":
            print("Player2 wins")
            player2+=1
        else:
            print("Player1 wins")
            player1+=1
        attempt+=1
        input("Press enter when player 1 is ready...")
        print("\n"*50)
    if player1>player2:
        print(f'Player1 won this match with {player1} point out of 3 points\nPlayer2 lose this match with {player2} points')
    elif player1==player2:
        print(f'Match ends with draw')
    else:
        print(f'Player2  win this match with {player2} out of 3 points\nPlayer1 lose this match with {player1} points')

menu="====Rock Paper Scissor Game====\n1. Against Computer\n2. Two player mode\n"
while True:
    print(menu)
    choice=input("Enter your choice: ")
    if choice.isdigit():
        if choice=="1":
            machine()
        elif choice=="2":
            two_player()
        else:
            print("Unknown choice!")
    else:
        print("The choice must be digit(1/2)!")
    again=input("Another match? (y/n): ").lower()
    if again!="y":
        print("THANKS FOR PLAYING!")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


