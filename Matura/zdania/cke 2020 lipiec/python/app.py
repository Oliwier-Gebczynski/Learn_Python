file = open("../DANE/identyfikator_przyklad.txt", "r")
file_list = []
zadanie_4_1 = []
zadanie_4_1_wynik = []

for line in file:
    file_list.append(line[:-1])

for item in file_list:
    list = []
    sum = 0
    number = item[3:]
    for n in number:
        sum += int(n)
    list.append(sum)
    list.append(item)
    zadanie_4_1.append(list)

zadanie_4_1.sort()

najwiekszy = zadanie_4_1[-1][0]

for item in zadanie_4_1:
    if item[0] == najwiekszy:
        zadanie_4_1_wynik.append(item[1])

print(f"zadanie 4.1 {zadanie_4_1_wynik}")

zadanie_4_2 = []

for item in file_list:
    number = item[3:]
    text = item[:3]

    if (number == number[::-1]) or (text == text[::-1]):
        zadanie_4_2.append(item)

print(f"zadanie 4.2 {zadanie_4_2}")

zadanie_4_3 = []
