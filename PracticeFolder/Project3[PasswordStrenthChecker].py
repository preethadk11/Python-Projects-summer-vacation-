import string
def strength_checker(password):
    has_lower=False
    has_upper=False
    has_digits=False
    has_symbol=False
    length=len(password)
    for ch in password:
        if ch in string.ascii_lowercase:
            has_lower=True
        if ch in string.ascii_uppercase:
            has_upper=True
        if ch in string.digits:
            has_digits=True
        if ch in string.punctuation:
            has_symbol=True
    missing=[]  #findign the missing parameter in a password
    if not has_lower:
        missing.append("lowercase")
    if not has_upper:
        missing.append("uppercase")
    if not has_digits:
        missing.append("digits")
    if not has_symbol:
        missing.append("symbols")
    
    if has_lower and has_upper and has_digits and has_symbol and length>=8: #Strenth checker using condition and flag
        return "Strong password" , missing
    elif sum([has_lower,has_upper,has_digits,has_symbol])>=3 and length>=6:
        return "Medium password" , missing
    else:
        return "Weak password" , missing
password=input("Enter your password: ")
strength,missing=strength_checker(password)
print("strength: ",strength)
if missing:
    print("missing: ","".join(missing))
else:
    print("missing: None")