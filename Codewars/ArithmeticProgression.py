def find_missing(sequence):
    difference = (sequence[-1]-sequence[-2])

    for i in range(len(sequence)-1):
        if sequence[i] + difference != sequence[i+1]:
            return sequence[i]+difference


find_missing([1, 2, 3, 4, 6, 7, 8, 9])