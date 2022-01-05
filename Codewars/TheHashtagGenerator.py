def generate_hashtag(s):
    result = "#"
    if (len(s) == 0) or (len(s)>140):
        return False
    else:
        list = s.split(" ")

        for item in list:
            if item != '':
                word = (item[0].upper() + item[1:].lower())
                result += word

    return result

#done