#PasswordStrengthChecker
import string
def strength_checker(password):
    has_lower=False
    has_upper=False
    has_digits=False
    has_symbol=False
    length=len(password)
    if any(ch in string.ascii_lowercase for ch in password):
        has_lower=True
    if any(ch in string.ascii_uppercase for ch in password):
        has_upper=True
    if any(ch in string.digits for ch in password):
        has_digits=True
    if any(ch in string.punctuation for ch in password):
        has_symbol=True
    if has_lower and has_upper and has_digits and has_symbol and length>=8:
        return "Strong password"
    elif sum([has_lower,has_upper,has_digits,has_symbol])>=3 and length>=6:
        return "Medium password"
    else:
        return "Weak password"
password=input("Enter the password to check: ")
print("Strength: ",strength_checker(password))
