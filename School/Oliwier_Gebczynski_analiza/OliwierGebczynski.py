# ----------------------POLECENIA--------------------------------
#1. wypisz wszystkie słowa z tego pliku ( mogą sie powtarzać )
#2. podaj największa i najmniejszą liczbą w pliku
#3. wypisz wszystkie słowa które mają długość taką jak druga liczba w danej linii w której jest słowo
#4. wypisz wszystkie liczby które są mniejsze niż wartość liczby podanej jako pierwsza liczba w linii
#5. podaj te słowa które zawierają dokładnie 2 samogłoski
#Autor: Oliwier Gębczyński 4i

file = open('dane.txt', 'r')
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
liczby = []
wyrazy = []
z_samogloskami = []

def wszystkie_wyrazy(jedna_linia):
    for item in jedna_linia:
        if item.isnumeric():
            item = int(item)
            liczby.append(item)
        else:
            wyrazy.append(item)

def najwieksza_i_najmniejsza():
    liczby.sort()
    print(f"Najmniejsza liczba: {liczby[0]}, najwieksza liczba: {liczby[-1]}")

def wyraz_o_dlugosci(jedna_linia):
    global ilosc_liter
    ilosc_liter = int(jedna_linia[1])
    global zgodne_wyrazy
    zgodne_wyrazy = []

    for item in jedna_linia:
        if item.isalpha():
            if len(item) == ilosc_liter:
                zgodne_wyrazy.append(item)

    print(f"Slowa o dlugosci {ilosc_liter} to: {zgodne_wyrazy} ")

def liczby_mniejsze(jedna_linia):
    pierwsza_liczba = int(jedna_linia[0])
    zbior_liczb = []

    for item in jedna_linia:
        if item.isnumeric():
            if int(item) < pierwsza_liczba:
                zbior_liczb.append(item)
    print(f"Liczby mniejsze od {pierwsza_liczba}: {zbior_liczb}")

def samogloski_wyrazy(jedna_linia):
    for item in jedna_linia:
        if item.isalpha():
            i = 0
            for letter in item:
                if letter in samogloski:
                    i += 1
            if i == 2:
                if item not in z_samogloskami:
                    z_samogloskami.append(item)

print("Zadanie 1__________________________________________________________")
for line in file:
    jedna_linia = line.split()
    wszystkie_wyrazy(jedna_linia)
print(f"Wszystkie wyrazy: {wyrazy}")

print("Zadanie 2__________________________________________________________")
najwieksza_i_najmniejsza()

print("Zadanie 3__________________________________________________________")
file.seek(0)
for line in file:
    jedna_linia = line.split()
    wyraz_o_dlugosci(jedna_linia)

print("Zadanie 4__________________________________________________________")
file.seek(0)
for line in file:
    jedna_linia = line.split()
    liczby_mniejsze(jedna_linia)
print("Zadanie 5__________________________________________________________")
file.seek(0)
for line in file:
    jedna_linia = line.split()
    samogloski_wyrazy(jedna_linia)
print(f"Slowa z dwoma samogloskami: {z_samogloskami}")


