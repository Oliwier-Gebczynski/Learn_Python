print("Hello in basic login system!")

login_data = open("database.txt", "r")
login = input("Login: ")

if login == login_data.readlines()[0].split()[0]:
    password = input("Password: ")
    print(password)

    if password == login_data.readlines()[0].split()[-1]:
        print("Succesfull!")
else:
    print("Its wrong login!")
