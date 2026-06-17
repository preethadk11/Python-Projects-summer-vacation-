#PasswordGenerator
import random
def generator(length):
    char_pool="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*():><?']"
    password_list=[]
    for i in range(length):
        char=random.choice(char_pool)
        password_list.append(char)
    generator_password="".join(password_list)
    return generator_password

length=int(input("Enter the length for your password: "))
password=generator(length)
print(f"Generated password: {password}")