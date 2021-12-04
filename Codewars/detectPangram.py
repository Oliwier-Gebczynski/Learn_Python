import string

def is_pangram(text):
    result = False
    sign_list = []
    end_list =[]
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    for letter in text:
        if (letter.isspace() is False) and (letter not in string.punctuation) and (letter not in string.digits):
            sign_list.append(letter.lower())

    sign_list.sort()
    for element in sign_list:
        if element not in end_list:
            end_list.append(element)

    if end_list == alphabet_list:
        result = True

    return result



is_pangram("The quick, brown fox jumps over the lazy dog!")