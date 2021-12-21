def find_it(seq):
    for item in seq:
        if seq.count(item)%2!=0:
            return item

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])