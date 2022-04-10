file = open("../Dane_PR/przyklad.txt", "r")
file_lista = []

for line in file:
    file_lista.append(int(line[:-1]))

#zadanie 1
wynik_1 = []

for item in file_lista:
    if (item % 3 == 0) and (item % 2 != 0):
        for i in range(1, 11):
            if pow(3, i) == item:
                wynik_1.append(item)
    elif item == 1:
        wynik_1.append(item)

print(f"Zadanie 1. Długość wynosi: {len(wynik_1)}")

#zadanie 2
wynik_2 = []
def silnia(n):
    silnia = 1
    for i in range(1, n+1):
        silnia *= i
    return silnia

for item in file_lista:
    wyniki_silni = []
    suma_silnia = 0
    for number in str(item):
        if int(number) == 0 or int(number) == 1:
            wyniki_silni.append(1)
        else:
            wyniki_silni.append(silnia(int(number)))

    for element in wyniki_silni:
        suma_silnia += element

    if suma_silnia == item:
        wynik_2.append(item)

print(f"Zadanie 2. Wynik zadania: {wynik_2}")

#zadanie 3

