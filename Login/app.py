import pickle

print("Hello in basic login system!")

login_input = {1: "oliwier", 2: "qwerty"}

data_out = open("database.txt", "wb")
pickle.dump(login_input, data_out)
data_out.close()

data_in = open("database.txt", "rb")
login_data = pickle.load(data_in)

print(login_data[2])
