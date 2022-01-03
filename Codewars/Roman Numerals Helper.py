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
    dozens = ""
    for letter in roman_num:
        if letter == "M":
            result += 1000
            dozens += letter
        elif letter == "D":
            result += 500
            dozens += letter
        elif letter == "C":
            result += 100
            dozens += letter
        elif letter == "L":
            result += 50
            dozens += letter
        elif letter == "X":
            result += 10
            dozens += letter

    roman_len = len(roman_num)
    dozens_len = len(dozens)
    index = roman_len - dozens_len

    if roman_num[-index:] == "IX":
        result += 9
    elif roman_num[-index:] == "VIII":
        result += 8
    elif roman_num[-index:] == "VII":
        result += 7
    elif roman_num[-index:] == "VI":
        result += 6
    elif roman_num[-index:] == "V":
        result += 5
    elif roman_num[-index:] == "IV":
        result += 4
    elif roman_num[-index:] == "III":
        result += 3
    elif roman_num[-index:] == "II":
        result += 2
    elif roman_num[-index:] == "I":
        result += 1

    return result



to_roman(1990) # should return 'M'
#from_roman('MDCLXVI') # should return 1000