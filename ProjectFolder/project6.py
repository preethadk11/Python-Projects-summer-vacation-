#smart number guessing game
import random
def smart_game(attempts,range,very_close,close,far):
    attempts_used=0
    score=100
    secret=random.randint(1,range)
    print(secret)
    while attempts_used<attempts:
        num=input("Enter your guess: ")
        if num.isdigit():
            num=int(num)
            if num>0 and num<=range:
                attempts_used+=1
                if num>secret:
                    print("high!")
                elif num<secret:
                    print("low!")
                else:
                    return score,attempts_used,secret,True
                distance=abs(num-secret)          #proximity distance check
                if distance<=very_close:
                    print("Very close")
                elif distance<=close:
                    print("Closer")
                elif distance<=far:
                    print("little far")
                else:
                    print("Too far")
                score-=10
            else:
                print("Number must be between the limited range")
        else:
            print("Only numbers are allowed")
    else:
        return score,attempts_used,secret,False
print("\t\tSmart Number Guessing Game\n")
print("1. Easy [1-20] [10 attempts]\n2. Medium [1-50] [7 attempts]\n3. Hard [1-100] [5 attempts]")
while True:
    level=input("Choose difficulty level number: ")
    if level.isdigit():
        level=int(level)
        if level==1:
            score,attempts,secret,val=smart_game(10,20,3,5,9)
        elif level==2:
            score,attempts,secret,val=smart_game(7,50,5,10,15)
        elif level==3:
            score,attempts,secret,val=smart_game(5,100,10,15,30)
        else:
            print("Print known level(1/2/3)!")
    else:
        print("Only enter digits!")
        continue
    if val:
        print("You won!")
        print(f'Secret number: {secret}')
        print(f'Attempts used: {attempts}')
        print(f'Score: {score}')
    else:
        print("You lost!")
        print(f'Secret number: {secret}')
    break
    