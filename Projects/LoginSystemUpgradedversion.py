#login system upgraded version #authenticate user #update attempt #lock account
users = {
    "admin": {"password": "1234", "attempts": 3, "locked": False},
    "alice": {"password": "9999", "attempts": 3, "locked": False},
    "bob":   {"password": "5555", "attempts": 3, "locked": False},
    "john":  {"password": "1111", "attempts": 3, "locked": False}
}
def authenticate_user(user_name):
    if users[user_name]["locked"]!=True:
        while users[user_name]["attempts"]>0:
            user_pass=input("Enter the password: ")
            if users[user_name]["password"]==user_pass:
                return True
            print("Wrong password")                                       
            users[user_name]["attempts"]-=1
            print(f'Attempts left: {users[user_name]["attempts"]}')
        else:
            users[user_name]["locked"]=True
            print("Account Locked")
            return False
    else:
        print("Account Locked\nContact admin")
        return False
while True:
    user_name=input("Enter the username: ")
    if user_name not in users:
        print("User not found")
        retry=input("Wanna exit?(yes/no): ")
        if retry.lower() == "yes":
            break
    else:
        val=authenticate_user(user_name)
        if val:
           print("Login successfull")
           break



