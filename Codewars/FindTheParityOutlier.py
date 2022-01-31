def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i% 2 != 0:
            odd.append(i)
        elif i% 2 == 0:
            even.append(i)
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]


find_outlier([2, 4, 6, 8, 10, 3])