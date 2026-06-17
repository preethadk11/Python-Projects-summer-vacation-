#PasswordGenerator
import random
import string
def generator(length):
    if length<4:
        return "Then length must be atleast of 4"
    lower=random.choice(string.ascii_lowercase)
    upper=random.choice(string.ascii_uppercase)
    digit=random.choice(string.digits)
    symbol=random.choice(string.punctuation)
    all_chars=string.ascii_letters+string.digits+string.punctuation
    password_list=[lower,upper,digit,symbol]
    for i in range(length - 4):
        password_list.append(random.choice(all_chars))
    random.shuffle(password_list)
    return "".join(password_list)
length=int(input("Enter the length of your password: "))
print("Generator password: ",generator(length))