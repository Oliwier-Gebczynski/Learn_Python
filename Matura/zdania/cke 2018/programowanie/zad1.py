file = open("../Dane_PR/sygnaly.txt", "r")

#zadanie 4.1
print("zadanie 4.1")
file_list = []
wynik = ""
for line in file:
    file_list.append(line[:-1])

for i in range(39, len(file_list), 40):
    slowo = file_list[i]
    wynik += slowo[9]

print(wynik)

#zadanie 4.2
print("zadanie 4.2")
podwynik = []
najdluzszy = 0
wynik = []

for slowo in file_list:
    slowo_lista = []
    slowo_litera = ""
    for litera in slowo:
        if litera not in slowo_litera:
            slowo_litera += litera
    slowo_lista.append(slowo_litera)
    slowo_lista.append(len(slowo_litera))
    podwynik.append(slowo_lista )

for element in podwynik:
    if element[1] > najdluzszy:
        najdluzszy = element[1]

for element in podwynik:
    if element[1] == najdluzszy:
        wynik.append(element)

print(wynik)

#zadanie 4.3 do poprawienia

print("zadanie 4.3")
alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
zad3_podwynik = []
zad3_wynik = []
for slowo in file_list:
    dodanie_slowa = [slowo]
    for i in range(0,len(slowo)-1):
        if i <= len(slowo)-2:
            index_slowo0 = alfabet.index(slowo[i])
            index_slowo1 = alfabet.index(slowo[i+1])
            roznica = index_slowo1 - index_slowo0

            if roznica >= 10:
                dodanie_slowa = []

    zad3_podwynik.append(dodanie_slowa)

for element in zad3_podwynik:
    if element != []:
        zad3_wynik.append(element)

