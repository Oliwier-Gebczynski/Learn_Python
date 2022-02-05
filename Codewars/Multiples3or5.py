def solution(number):
    listMultiples = []
    result = 0
    three = 0
    five = 0
    if number <= 0:
        return 0
    else:
        while three < number:
            three += 3
            listMultiples.append(three)
        while five < number:
            five += 5
            listMultiples.append(five)
        listMultiples = list(dict.fromkeys(listMultiples))
        for item in listMultiples:
            if item < number:
                result += item
        return result


solution(16)