battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def validate_battlefield(field):
    shipCell = 0
    for row in field:
        for item in row:
            if item == 1:
                shipCell += 1

    if shipCell == 20:
        print("Okej")

    print(shipCell)

# jezeli jest =1 sprawdz do okoła czy sa jedynki. Jezeli jest 1 w dół to sprawdzaj tylko kolumne w dół do =0 / przy okazji sprawdz wszystkie komorki czy nie maja po bokach innych jedynek, jesli tak to wyswietl false



validate_battlefield(battleField)