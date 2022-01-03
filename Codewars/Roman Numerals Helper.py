def to_roman(val):
    result = ""
    while val > 0:
        while val >= 1000:
            result += "M"
            val -= 1000

        while val >= 500:
            result += "D"
            val -= 500

        while val >= 100:
            result += "C"
            val -= 100

        while val >= 50:
            result += "L"
            val -= 50

        while val >= 10:
            result += "X"
            val -= 10

        if val == 9:
            result += "IX"
        elif val == 8:
            result += "VIII"
        elif val == 7:
            result += "VII"
        elif val == 6:
            result += "VI"
        elif val == 5:
            result += "V"
        elif val == 4:
            result += "IV"
        elif val == 3:
            result += "III"
        elif val == 2:
            result += "II"
        elif val == 1:
            result += "I"

        val = 0
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

        if sign_map[first] < sign_map[second]: # MCMXC
            result -= sign_map[first]  # 1. -, 2. -, 3.
        else:
            result += sign_map[first]  # 1. 1000, 2. 1500,
        print(result)

    result += sign_map[roman_num[-1]]
    return result

#to_roman(1990) # should return 'M'
from_roman('MDCLXVI')