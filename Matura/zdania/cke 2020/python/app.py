file = open("../Dane_PR2/przyklad.txt", "r")

file_list = []

for line in file:
    file_list.append(line[:-1].split(" "))

#zadanie 1

pierwsze = [2]

def czy_pierwsza(liczba):
    for dzielnik in pierwsze:
        if liczba % dzielnik == 0:
            return False
        if dzielnik * dzielnik > liczba:
            return True
    return True


def wyznacz_pierwsze(liczba):
    for i in range(2, liczba):
        if czy_pierwsza(i) is True:
            pierwsze.append(i)
    return

wyznacz_pierwsze(100)
print(pierwsze)

def zadanie1():
    for item in file_list:
        for element in range(3,100):
            if czy_pierwsza(int(item[0])) and czy_pierwsza(int(item[0])-element):
                print(int(item[0]), element, int(item[0])-element)

zadanie1()