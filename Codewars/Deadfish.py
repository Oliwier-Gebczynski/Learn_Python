def parse(data):
    result = []
    i = 0
    for item in data:
        if item == "i":
            i += 1
        if item == "d":
            i -= 1
        if item == "s":
            i = i * i
        if item == "o":
            result.append(i)

    return result