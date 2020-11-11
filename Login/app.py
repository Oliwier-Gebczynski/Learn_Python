import pickle

print("Hello in basic login system!")

# login dict
# login_input = {
#  1: ["oliwier", "karol", "kuba"],
#  2: ["qwerty", "haslo", "maslo"]
# }

# add new users
#data_out = open("database.txt", "wb")
#pickle.dump(login_input, data_out)
# data_out.close()

# read data from .txt
data_in = open("database.txt", "rb")
login_data = pickle.load(data_in)
data_in.close()

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
