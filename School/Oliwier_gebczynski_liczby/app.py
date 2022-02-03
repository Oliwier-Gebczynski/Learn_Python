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
        if bin(int(item))[2:].count('1') % 2 != 0:
            zNieparzysta += 1
    print(zNieparzysta)

def zadanie2(list):
    iloscRosnacych = 0
    for item in list:
        wyciety = oct(int(item))[2:]
        pierwsza = []
        for item in wyciety:
            pierwsza.append(int(item))
        druga = pierwsza.copy()
        druga.sort()
        if pierwsza == druga:
            iloscRosnacych += 1
    print(iloscRosnacych)

def zadanie3(list):
    policzone = []
    wynik = []
    for item in list:
        wyciete = bin(int(item))[2:]
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
    print(f"{j}, {wynik}")

def zadanie4(list):
    ciagiLiczb = []
    pojedynczyCiag = []
    wynik = []
    for item in list:
        wyciete = hex(int(item))[2:]
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
    print(wynik)

#Start
list = delete_n(list)
print("-------Zadanie 1--------")
zadanie1(list)
print("-------Zadanie 2--------")
zadanie2(list)
print("-------Zadanie 3--------")
zadanie3(list)
print("-------Zadanie 4--------")
zadanie4(list)
