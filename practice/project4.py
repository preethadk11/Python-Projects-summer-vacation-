#Login system authentication
users = {
    "admin": {"password": "1234", "attempts": 3, "locked": False},
    "alice": {"password": "9999", "attempts": 3, "locked": False},
    "bob":   {"password": "5555", "attempts": 3, "locked": False},
    "john":  {"password": "1111", "attempts": 3, "locked": False}
}
def authenticate_user(username):
    user=users[username]
    if user["locked"]:
        print("Account locked\nContact admin")
        return False
    while user["attempts"]>0:
        user_pass=input("Enter the password: ")
        if user["password"]==user_pass:
            user["attempts"]=3
            return True
        user["attempts"]-=1
        print("Wrong password")
        print(f'Attempts left: {user["attempts"]}')
    user["locked"]=True
    print("Account locked")
    return False
        
while True:
    username=input("Enter the username(or exit): ")
    if username=="exit":
        break
    if username not in users:
        print("User not found")
        continue
    result=authenticate_user(username)
    if result:
        print("Login successfull")
        break