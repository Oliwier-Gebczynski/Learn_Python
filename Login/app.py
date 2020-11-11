import pickle

print("Hello in basic login system!")

#login_input = {1: "oliwier", 2: "qwerty"}

#data_out = open("database.txt", "wb")
#pickle.dump(login_input, data_out)
# data_out.close()

data_in = open("database.txt", "rb")
login_data = pickle.load(data_in)
data_in.close()

login = input("Login: ")

if login_data[1] == login:
    password = input("Password: ")
    if login_data[2] == password:
        print("Succes!")
    else:
        print("Incorrect password")
else:
    print("Incorrect login")
