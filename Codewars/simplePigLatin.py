import string

def pig_it(text):
    result = []
    result_text = " "
    words_list = text.split(" ")

    for item in words_list:
        word = []
        word_string = ""
        if item not in string.punctuation:
            for letter in item:
                word.append(letter)
            first = word[0]
            word.pop(0)
            word.append(first)
            word.append('ay')
            word_string.join(word)

            for element in word:
                word_string += element

            result.append(word_string)
        else:
            result.append(item)

    return (result_text.join(result))

pig_it('Hello world !')