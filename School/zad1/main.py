# w pliku daneslowa.txt znajdz te wiersze które zawieraja slowa z taka iloscia powtorzen samoglosek jaka jest wartosc liczby na poczatku wiersza wypisz te slowo usuwajac te litery oraz usuniete litery
file = open('daneslowa.txt', 'r')
fileList = file.readlines()
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

def delete_n(): #delete /n from
    i = 0
    for item in fileList:
        fileList[i] = item.strip()
        i += 1

def splitList(): # split list and change number into int
    i = 0
    for item in fileList:
        fileList[i] = fileList[i].split()
        fileList[i][0] = int(fileList[i][0])
        i += 1

def deleteLetters():
    for item in fileList:
        number = item[0]
        word = item[1]
        deleted = []
        for samogloska in samogloski:
            if number == word.count(samogloska):
                newWord = word.replace(samogloska, '')
                deleted.append(samogloska)
        if len(deleted) > 0:
            print(f"{newWord}, usunieto: {deleted}")

delete_n()
splitList()
deleteLetters()
