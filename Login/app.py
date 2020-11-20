import pickle
import os

# login dict
if os.stat("database.txt").st_size == 0:
    with open("database.txt", "wb") as database:
        login_input = {
            1: ["test"],
            2: ["test"]
        }
        pickle.dump(login_input, database)
        database.close()

print("Hello in basic login system!")

# load data
data_in = open("database.txt", "rb")
login_data = pickle.load(data_in)
data_in.close()

# choose option
print("1.Login")
print("2.Registration")
menu = input("Choose [1/2]: ")

while menu != "1" and menu != "2":
    menu = input("Wrong option! Choose [1/2]: ")


def login_function():
    # input login, get login index
    login = input("Login: ")
    login_user = login_data[1]
    x = login_user.index(login)

    # search login in database, "x" is the login index of array, "login and password" pairs have the same index
    if login_data[1][x] == login:
        password = input("Password: ")
        if login_data[2][x] == password:
            print("Succes!")
        else:
            print("Incorrect password")
    else:
        print("Incorrect login")


def registration_function():
    # input new login
    new_user = input("Your login: ")
    user = login_data[1]

    # checking the availability of the login
    if new_user in user:
        print("This login is taken")
    else:
        new_password = input("Your new password: ")
        repeat_password = input("Repeat password: ")

        while new_password != repeat_password:
            repeat_password = input(
                "Password dont match! Repeat password: ")

        # save new user
        if new_password == repeat_password:
            data_out = open("database.txt", "wb")

            user_data = login_data[1]
            password_data = login_data[2]

            user_data.append(new_user)
            password_data.append(new_password)

            pickle.dump(login_data, data_out)
            data_out.close()

            print("Account created!")


# function call
if menu == "1":
    login_function()
elif menu == "2":
    registration_function()
