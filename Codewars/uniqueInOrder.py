def unique_in_order(text):
    result = ["delete"]
    for letter in text:
        if letter not in result:
            result.append(letter)
        elif letter != result[-1]:
            result.append(letter)

    result.remove("delete")
    return result

unique_in_order('AAAABBBCCDAABBB')
unique_in_order([1,2,2,3,3])