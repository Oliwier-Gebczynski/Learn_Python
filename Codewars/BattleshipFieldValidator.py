
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
            if check_ships(field) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]:
                print("True")
                return True
            elif check_ships(field) != [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]:
                print("false")
                return False
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
        for j in range(9):
            if field[i][j] == 1:
                if field[i][j+1] == 1:
                    z = j+1
                    ship = 1
                    if z <= 8:
                        while field[i][z] == 1:
                            field[i][z] = 2
                            z += 1
                            ship += 1
                    if z == 9:
                        if field[i][z] == 1:
                            ship += 1
                    result.append(ship)
                if field[i+1][j] == 1:
                    z = i+1
                    ship = 1
                    if z <= 8:
                        while field[z][j] == 1:
                            field[z][j] = 2
                            z += 1
                            ship += 1
                    if z == 9:
                        if field[z][j] == 1:
                            ship += 1
                    result.append(ship)
                if field[i-1][j] == 0 and field[i+1][j] == 0 and field[i][j-1] == 0 and field[i][j+1] == 0:
                    field[i][j] = 2
                    result.append(1)
    result.sort()
    return result

validate_battlefield(battleField)
