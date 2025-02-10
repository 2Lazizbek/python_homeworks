password = input("Enter password: ")
while len(password) < 8 or not any(i.isupper() for i in password):
    if len(password) < 8:
        print("Password is too short.")
    if not any(i.isupper() for i in password):
        print("Password must contain an uppercase letter.")
    password = input("Enter password: ")
print("Password is strong.")