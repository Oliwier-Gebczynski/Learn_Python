def to_roman(val):
    result = ""
    value = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbol = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    i = 0
    while val > 0:
        for _ in range(val // value[i]):
            result += symbol[i]
            val -= value[i]
        i += 1
    return result


def from_roman(roman_num):
    result = 0
    sign_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    for index in range(len(roman_num) - 1):
        first = roman_num[index]
        second = roman_num[index + 1]
        print(first)
        print(second)

        if sign_map[first] < sign_map[second]:
            result -= sign_map[first]
        else:
            result += sign_map[first]
        print(result)
        print("____________________________")

    result += sign_map[roman_num[-1]]
    return result

#to_roman(1990) # should return 'M'
from_roman('MDCLXVI')