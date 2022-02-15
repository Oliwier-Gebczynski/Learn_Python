def dig_pow(n, p):
    result = []
    end = 0
    for item in str(n):
        result.append(int(item))
    for i in range(len(str(n))):
        end += pow(result[i], p)
        p += 1
    k = (end/n)
    if end == pow(n,p):
        return p
    elif end % n == 0:
        return k
    else:
        return -1