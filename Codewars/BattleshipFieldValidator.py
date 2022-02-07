battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def validate_battlefield(field):
    shipCell = 0
    for row in field:
        for item in row:
            if item == 1:
                shipCell += 1

    if shipCell == 20:
        check_cell(field)

    print(shipCell)

# jezeli jest =1 sprawdz do okoła czy sa jedynki. Jezeli jest 1 w dół to sprawdzaj tylko kolumne w dół do =0 / przy okazji sprawdz wszystkie komorki czy nie maja po bokach innych jedynek, jesli tak to wyswietl false

def check_cell(field):
    for i in range(len(str(field))-1):
        for j in range(len(str(field))-1):
            if ((1 <= j <= 8) and (1 <= i <= 8)) and field[i][j] == 1:
                if field[i+1][j+1] == 1 or field[i+1][j-1] == 1 or field[i-1][j+1] == 1 or field[i-1][j-1] == 1:
                    return False




validate_battlefield(battleField)