big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special_signs = ["!", "@", "#", "$", "%", "&", "*", "?"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

how_many = input("How long the password must be (max = 30): ")
how_many = int(how_many)

if how_many > 30:
    print("To many characters!")
elif how_many <= 0:
    print("You didnt specify the lenght!")
else:
    print(how_many)
