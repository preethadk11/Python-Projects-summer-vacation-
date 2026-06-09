users = {
    "admin": {"password": "1234", "attempts": 3, "locked": False},
    "alice": {"password": "9999", "attempts": 3, "locked": False},
    "bob":   {"password": "5555", "attempts": 3, "locked": False},
    "john":  {"password": "1111", "attempts": 3, "locked": False}
}


def authenticate_user(user_name):

    user = users[user_name]

    # If already locked
    if user["locked"]:
        print("Account Locked\nContact admin")
        return False

    # Password attempts loop
    while user["attempts"] > 0:

        user_pass = input("Enter the password: ")

        if user["password"] == user_pass:
            user["attempts"] = 3   # reset after success
            return True

        user["attempts"] -= 1
        print("Wrong password")
        print(f'Attempts left: {user["attempts"]}')

    # Lock account after attempts end
    user["locked"] = True
    print("Account Locked")
    return False


# ---------------- MAIN FLOW ---------------- #

while True:

    user_name = input("Enter username (or type exit): ")

    # clean exit option
    if user_name.lower() == "exit":
        print("Program ended")
        break

    # username validation
    if user_name not in users:
        print("User not found")
        continue   # go back to username input

    # authentication step
    result = authenticate_user(user_name)

    if result:
        print("Login successful")
        break