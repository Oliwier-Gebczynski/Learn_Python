def snail(snail_map):
    result = []
    while len(snail_map) > 0:
        result += snail_map[0]
        del snail_map[0]
        if len(snail_map) > 0:
            for item in snail_map:
                result.append(item[-1])
                del item[-1]
            if snail_map[-1]:
                result += snail_map[-1][::-1]
                del snail_map[-1]
            for item in reversed(snail_map):
                result += [item[0]]
                del item[0]
    return result

snail([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
])