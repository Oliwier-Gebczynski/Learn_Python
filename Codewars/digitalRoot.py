def digital_root(n):
    result = 0
    for item in str(n):
        result += int(item)
    print(result)
    while len(str(result)) > 1:
        print("okej")
        result = function(result)
    return result

def function(result):
    i = 0
    for item in str(result):
        i += int(item)
    print(i)
    return i





digital_root(942)