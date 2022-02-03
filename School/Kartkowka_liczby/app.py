file = open('dane.txt', 'r')
list = file.readlines()

def delete_n(fileList):
    i = 0
    for item in fileList:
        fileList[i] = item.strip()
        i += 1
    return fileList

def zadanie1(list):
    zNieparzysta = 0

    for item in list:
        item = int(item)
        binItem = bin(item)
        strItem = str(binItem)
        wyciete = strItem[2:]

        iloscJedynek = 0

        for letter in wyciete:
            if letter == "1":
                iloscJedynek += 1

        if iloscJedynek%2 == 1:
            zNieparzysta += 1

    return zNieparzysta

def zadanie2(list):
    iloscRosnacych = 0

    for item in list:
        item = int(item)
        octItem = oct(item)
        strItem = str(octItem)
        wyciety = strItem[2:]

        pierwsza = []
        for item in wyciety:
            pierwsza.append(int(item))

        druga = pierwsza.copy()
        druga.sort()

        if pierwsza == druga:
            iloscRosnacych += 1

    return iloscRosnacych

def zadanie3(list):
    policzone = []
    wynik = []
    for item in list:
        item = int(item)
        binItem = bin(item)
        strItem = str(binItem)
        wyciete = strItem[2:]


        tablica = []
        iloscJedynek = 0
        for letter in wyciete:
            if letter == "1":
                iloscJedynek += 1

        tablica.append(iloscJedynek)
        tablica.append(wyciete)

        policzone.append(tablica)

    j = 0
    for item in policzone:
        i = item[0]

        if i > j:
            j = i

    for item in policzone:
        if item[0] == j:
            wynik.append(item[1])

    return j, wynik

def zadanie4(list):
    ciagiLiczb = []
    pojedynczyCiag = []
    wynik = []
    for item in list:
        item = int(item)
        hexItem = hex(item)
        strItem = str(hexItem)
        wyciete = strItem[2:]

        if wyciete.isnumeric():
            pojedynczyCiag.append(wyciete)
        else:
            if pojedynczyCiag != []:
                ciagiLiczb.append(pojedynczyCiag)
                pojedynczyCiag = []

    for item in ciagiLiczb:
        dlugosc = len(item)
        item.append(dlugosc)

    j = 0
    for item in ciagiLiczb:
        i = item[-1]

        if i > j:
            j = i

    for item in ciagiLiczb:
        if item[-1] == j:
            item.pop(-1)
            wynik.append(item)

    return wynik

#Start
list = delete_n(list)

print("-------Zadanie 1--------")
zadanie1 = zadanie1(list)
print(zadanie1)

print("-------Zadanie 2--------")
zadanie2 = zadanie2(list)
print(zadanie2)

print("-------Zadanie 3--------")
zadanie3 = zadanie3(list)
print(zadanie3)

print("-------Zadanie 4--------")
zadanie4 = zadanie4(list)
print(zadanie4)
