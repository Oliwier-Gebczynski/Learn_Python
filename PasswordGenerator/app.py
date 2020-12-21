import random

big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special_signs = ["!", "@", "#", "$", "%", "&", "*", "?"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def password_generator(how_many):
    password = []
    password.append(random.choice(big_letters))
    password.append(random.choice(small_letters))
    password.append(random.choice(special_signs))
    password.append(random.choice(numbers))

    all_signs = []
    all_signs.extend(big_letters)
    all_signs.extend(small_letters)
    all_signs.extend(special_signs)
    all_signs.extend(numbers)

    while len(password) < how_many:
        password.append(random.choice(all_signs))

    random.shuffle(password)

    print(password)


how_many = input("How long the password must be (max = 30, min = 4): ")
how_many = int(how_many)

if how_many > 30:
    print("To many characters!")
elif how_many < 4:
    print("You didnt specify the lenght!")
else:
    password_generator(how_many)
