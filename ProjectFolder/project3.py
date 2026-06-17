#Password Strength checker
import string
def strength_checker(password):
    length=len(password)
    score=0
    has_lower=False
    has_upper=False
    has_digit=False
    has_symbol=False
    for ch in password:
        if ch in string.ascii_lowercase:
            has_lower=True
        elif ch in string.ascii_uppercase:
            has_upper=True
        elif ch in string.digits:
            has_digit=True
        else:
            has_symbol=True
    missing_list=[]
    if not has_lower:
        missing_list.append("Lowercase")
    if not has_upper:
        missing_list.append("Uppercase")
    if not has_digit:
        missing_list.append("Digits")
    if not has_symbol:
        missing_list.append("Symbols")
    if has_lower:
        score+=1
    if has_upper:
        score+=1
    if has_digit:
        score+=1
    if has_symbol:
        score+=1
    if length>=8:
        score+=1
    return score,missing_list
print("\t\tPassword Strength Checker\n")
password=input("Enter your password: ")
score,missing=strength_checker(password)
if score<=1:
    print("Strength: Weak")
elif score<=3:
    print("Strength: Medium")
else:
    print("Strength: Strong")
print(f"Strength Score: {score}/5")
if missing:
    print(f"Missing parts:{"".join(missing)}")
else:
    print("Missing parts: None")

