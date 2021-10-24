file = open('base.txt', 'r')
file_first_line = file.readline()
file_list = file.readlines()

def delete_n():
    i = 0
    for item in file_list:
        file_list[i] = item.strip()
        i+=1

def czy_pierwsza():
    number_list = file_first_line.split()
    i = 0
    for item in number_list:
        number_list[i] = int(item)
        i+=1

    for item in number_list:
        if item == 1:
            return False
        else:
            for i in range(2, item):
                if item % i == 0:
                    return False
            return True

def dlugosc_slowa(slowo):
    return len(slowo)

def palindrom(slowo):
    if slowo == slowo[::-1]:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")




#wywolanie funkcji
palindrom("taat")