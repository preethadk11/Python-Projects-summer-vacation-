#Login system 
username="admin"
def_password=1234
def LoginSystem():
    attempts=3
    while attempts>0:
        name=input("Enter the username: ")
        password=int(input("Enter the password: "))
        if username==name and def_password==password:
            print("Login Successfull")
            break
        attempts-=1
        print(f'Attempts left:{attempts}')
    else: 
        print("Account Locked")
print("\t\tLogin System\n")
LoginSystem()

