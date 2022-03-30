tekst = "Litwo! Ojczyzno maja! Ty jesteś jak zdrowie, Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie Panno święta, co Jasnej bronisz Częstochowy I w Ostrej świecisz Bramie! Ty, co gród zamkowy Nowogródzki ochraniasz z jego wiernym ludem! Jak mnie dziecko do zdrowia powróciłaś cudem, (Gdy od płaczącej matki pod Twoją opiekę Ofiarowany, martwą podniosłem powiekę I zaraz mogłem pieszo do Twych świątyń progu Iść za wrócone życie podziękować Bogu), Tak nas powrócisz cudem na Ojczyzny łono. Tymczasem przenoś moją duszę utęsknioną Do tych pagórków leśnych, do tych łąk zielonych, Szeroko nad błękitnym Niemnem rozciągnionych; Do tych pól malowanych zbożem rozmaitem, Wyzłacanych pszenicą, posrebrzanych żytem; Gdzie bursztynowy świerzop, gryka jak śnieg biała, Gdzie panieńskim rumieńcem dzięcielina pała, A wszystko przepasane jakby wstęgą, miedzą Zieloną, na niej z rzadka ciche grusze siedzą."
wzorzec = input("Podaj szukany wzorzec: ")

wynik = []
ostateczny_wynik = []

for i in range(0, len(tekst)):
    if tekst[i] == wzorzec[0]:
        a = i
        string = ''
        string += tekst[i]
        for j in range(1, len(wzorzec)):
            a += 1
            if wzorzec[j] == tekst[a]:
                string += tekst[a]
        podwynik = []
        podwynik.append(i)
        podwynik.append(string)
        wynik.append(podwynik)

for i in range(0, len(wynik)):
    if wynik[i][1] == wzorzec:
        ostateczny_wynik.append(wynik[i])

print(ostateczny_wynik)



