a = [1,2,3]

def function(a):
    results = []
    newA = list(set(a))
    b = []

    sortedList = sorted(a)

    for i in range(1, max(sortedList)+1):
        b.append(i)

    for item in b:
        if item not in newA:
            results.append(item)

    print(b, newA, min(results))

function(a)