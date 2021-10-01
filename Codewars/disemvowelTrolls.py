vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def disemvowel(string_):
    for letter in string_:
        for vowel in vowels:
            if letter == vowel:
                string_ = string_.replace(letter,"")
    return string_

#DONE