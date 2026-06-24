#dice rolling game
import random
count=0
dice_count=int(input("How many dice you want to roll?: "))
while True:
        this_list=[]
    
        dice=input("Roll the dice?(y/n): ").lower()
        if dice=="y":
            count+=1
            for i in range(dice_count):
                this_list.append(random.randint(1,6))
            print("("+",".join(map(str,this_list))+")")
        elif dice=="n":
            print(f'You have rolled the dice for {count} times!')
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")



    