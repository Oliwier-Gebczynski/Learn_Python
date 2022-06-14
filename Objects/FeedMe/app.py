from datetime import date
import pandas as pd

#start with pandas

cat = """
|\__/,|   (`)
|_ _  |.--.) )
( T   )     /
(((^_(((/(((_/
"""
# pets calss
class Cat:
    def __init__(self, name, age, color, date, kind):
        self.name = name
        self.age = age
        self.color = color
        self.date = date
        self.kind = kind

    def addToDataframe(self):
        new_row = pd.DataFrame({'kind': [self.kind], 'name': [self.name], 'age': [self.age], 'color': [self.color], 'date': [self.date]})
        return new_row

class Dog:
    def __init__(self, name, age, color, date, kind):
        self.name = name
        self.age = age
        self.color = color
        self.date = date
        self.kind = kind

    def addToDataframe(self):
        new_row = pd.DataFrame({'kind': [self.kind], 'name': [self.name], 'age': [self.age], 'color': [self.color], 'date': [self.date]})
        return new_row

#functions
def newPuppy(name, age, color, today, kind, df):
    if kind == "DOG":
        doggo = Dog(name, age, color, today, kind)
        database_doggo = doggo.addToDataframe()
        file = pd.concat([df,database_doggo])
        return file
    elif kind == "CAT":
        kitty = Cat(name, age, color, today, kind)
        database_kitty = kitty.addToDataframe()
        file = pd.concat([df, database_kitty])
        return file
    elif (kind != "DOG") or (kind != "CAT"):
        print("There is no such type of pet")
        
def openFile():
    df = pd.read_csv('database.csv')
    return df

def main():
    file = openFile()
    kind = input("Type kind of pet(dog or cat): ").upper()
    
    if (kind == "DOG") or (kind == "CAT"):
        name = input("Name: ")
        age = input("Age: ")
        color = input("Color: ")
        today = date.today()

        file = newPuppy(name, age, color, today, kind, file)

        file.to_csv("database.csv", index=False)

        print(file)

    elif (kind != "DOG") or (kind != "CAT"):
        main()

    return file

main()






