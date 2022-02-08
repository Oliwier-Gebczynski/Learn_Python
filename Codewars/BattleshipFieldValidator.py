battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def validate_battlefield(field):
    shipCell = 0
    for row in field:
        for item in row:
            if item == 1:
                shipCell += 1

    if shipCell == 20:
        if check_cell(field) == False:
            return False
        elif check_cell(field) == None:
            return True
    else:
        return False

def check_cell(field):
    for i in range(9):
        for j in range(9):
            if ((1 <= j <= 8) and (1 <= i <= 8)) and field[i][j] == 1:
                if field[i+1][j+1] == 1 or field[i+1][j-1] == 1 or field[i-1][j+1] == 1 or field[i-1][j-1] == 1:
                    return False

def check_ships(field):
    result = []
    for i in range(9):
        list = []
        for j in range(9):
            if field[i][j] == 1:
                list







validate_battlefield(battleField)