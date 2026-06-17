#Password Score System
import string
def password_checker(password):
    score=0
    length=len(password)
    has_lower=False
    has_upper=False
    has_digits=False
    has_symbol=False
    for ch in password:
        if ch in string.ascii_lowercase:
            has_lower=True
        elif ch in string.ascii_uppercase:
            has_upper=True
        elif ch in string.digits:
            has_digits=True
        else:
            has_symbol=True
    if has_lower:
        score+=1
    if has_upper:
        score+=1
    if has_digits:
        score+=1
    if has_symbol:
        score+=1
    if length>=8:
        score+=1
    return score
password=input("Enter your password to check: ")
score=password_checker(password)
if score<=1:
    print("Weak")
elif score <=3:
    print("Medium")
else:
    print("Strong")
