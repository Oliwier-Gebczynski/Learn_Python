def square_sum(numbers):
    result = 0
    for number in numbers:
        result += number*number

    return result

square_sum([0, 3, 4, 5])