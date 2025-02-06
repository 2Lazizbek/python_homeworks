username = input("Inpur username: ")
password = input("Input password: ")
if bool(username) or bool(password) == False:
    print("Input both password and username:")
else:
    print("Both password and username are entered.")