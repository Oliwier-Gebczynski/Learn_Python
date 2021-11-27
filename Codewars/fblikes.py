def likes(names):
    equals = str

    if len(names) == 0:
        equals = 'no one likes this'
    elif len(names) == 1:
        equals = f'{names[0]} likes this'
    elif len(names) == 2:
        equals = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        equals = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        equals = f'{names[0]}, {names[1]} and {len(names)-2} others like this'

    return equals
