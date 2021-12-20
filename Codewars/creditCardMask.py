def maskify(cc):
    if (len(cc) == 0):
        return ""
    elif (len(cc) == 1) or (len(cc) == 2) or (len(cc) == 3):
        string = ""
        for item in cc:
            string += item
        return string
    elif (len(cc) > 3):
        string = ""
        hash_len = len(cc) - 4
        for i in range(hash_len):
            string += "#"
        string += cc[-4] + cc[-3] + cc[-2] + cc[-1]
        return string


