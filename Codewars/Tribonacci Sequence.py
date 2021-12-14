def tribonacci(signature, n):
    while len(signature) < n:
        last = signature[-1] + signature[-2] + signature[-3]
        signature.append(last)

    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return signature[0:1]
    elif n == 3:
        return signature[0:2]
    return signature

tribonacci([1, 1, 1], 1)