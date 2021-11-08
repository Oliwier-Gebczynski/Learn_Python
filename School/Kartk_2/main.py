# ----------------------POLECENIA--------------------------------
#1. wypisz wszystkie słowa z tego pliku ( mogą sie powtarzać )
#2. podaj największa i najmniejszą liczbą w pliku
#3. wypisz wszystkie słowa które mają długość taką jak druga liczba w danej linii w której jest słowo
#4. wypisz wszystkie liczby które są mniejsze niż wartość liczby podanej jako pierwsza liczba w linii
#5. podaj te słowa które zawierają dokładnie 2 samogłoski


file = open('dane.txt', 'r')
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
liczby = []
wyrazy = []

def wszystkie_wyrazy():
    print("Zadanie 3")
    for line in file:
        jedna_linia = line.split()

        wyraz_o_dlugosci(jedna_linia)

        for item in jedna_linia:
            if item.isnumeric():
                item = int(item)
                liczby.append(item)
            else:
                wyrazy.append(item)
    print("Zadanie 1")
    print(f"Wszystkie wyrazy: {wyrazy}")

def najwieksza_i_najmniejsza():
    liczby.sort()
    print("Zadanie 2")
    print(f"Najmniejsza liczba: {liczby[0]}, najwieksza liczba: {liczby[-1]}")

def wyraz_o_dlugosci(jedna_linia):
    ilosc_liter = int(jedna_linia[1])
    zgodne_wyrazy = []

    for item in jedna_linia:
        if item.isalpha():
            if len(item) == ilosc_liter:
                zgodne_wyrazy.append(item)

    print(f"Slowa o dlugosci {ilosc_liter} to: {zgodne_wyrazy} ")

wszystkie_wyrazy()
najwieksza_i_najmniejsza()
print("___________________________________________________________________")