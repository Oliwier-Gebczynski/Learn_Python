def digital_root(n):
    sumDigit = 0
    res = list(map(int, str(n)))

    for digit in res:
        sumDigit += int(digit)
    res = list(map(int, str(sumDigit)))












digital_root(942)