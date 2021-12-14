def move_zeros(array):
    zero_list = []
    for item in array:
        if item == 0:
            zero_list.append(item)

    while 0 in array:
        array.remove(0)

    array.extend(zero_list)
    return array

move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])