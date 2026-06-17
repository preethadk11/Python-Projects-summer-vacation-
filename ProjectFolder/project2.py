#Password Generator
import string
import random
def password_generator(length):
    if length<6:
        return "The length must be minimum of 6"
    lower=random.choice(string.ascii_lowercase)
    upper=random.choice(string.ascii_uppercase)
    digits=random.choice(string.digits)
    symbol=random.choice(string.punctuation)
    all_char=string.ascii_letters+string.digits+string.punctuation
    password_list=[lower,upper,digits,symbol]
    for i in range(length - 4):
        password_list.append(random.choice(all_char))
    random.shuffle(password_list)
    return "".join(password_list)
print("\t\tPassword Generator\n")
length=int(input("Enter your desired length: "))
print(f'Generated password:{password_generator(length)}')