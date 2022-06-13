from datetime import date
#start with pandas

cat = """
|\__/,|   (`)
|_ _  |.--.) )
( T   )     /
(((^_(((/(((_/
"""

kitties = []
doggos = []

# pets calss
class Cat:
    def __init__(self, name, age, color, date):
        self.name = name
        self.age = age
        self.color = color
        self.date = date

class Dog:
    def __init__(self, name, age, color, date):
        self.name = name
        self.age = age
        self.color = color
        self.date = date

#functions
def newPuppy(name, age, color, today, kind):
    if kind == "DOG":
        doggo = Dog(name, age, color, today)
        doggos.append(doggo)
    elif kind == "CAT":
        kitty = Cat(name, age, color, today)
        kitties.append(kitty)
    elif (kind != "DOG") or (kind != "CAT"):
        print("There is no such type of pet")

    print(doggos, kitties)

def main():
    kind = input("Type kind of pet(dog or cat): ").upper()
    
    if (kind == "DOG") or (kind == "CAT"):
        name = input("Name: ")
        age = input("Age: ")
        color = input("Color: ")
        today = date.today()

        newPuppy(name, age, color, today, kind)

    elif (kind != "DOG") or (kind != "CAT"):
        main()

main()

for item in kitties:
    print(f"{item.name}, {item.age}, {item.color}, {item.date}")





