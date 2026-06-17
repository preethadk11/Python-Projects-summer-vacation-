#PasswordGenerator
import string
import random
def PasswordGenerator(length):
    char_pool=(
        string.ascii_letters+string.digits+string.punctuation
    )
    password=""
    for i in range(length):
        password+=random.choice(char_pool)
    return "".join(password)
print("\t\tPassword Generator\n")
length=int(input("Enter the length for your password: "))
password=PasswordGenerator(length)
print(f"Generated password: {password}")