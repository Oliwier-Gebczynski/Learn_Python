from datetime import date
from unicodedata import name


cat = """
|\__/,|   (`)
|_ _  |.--.) )
( T   )     /
(((^_(((/(((_/
"""

class Cat:
    def __init__(self, name, age, color, date):
        self.name = name
        self.age = age
        self.color = color
        self.date = date

newKitty = Cat("Kinny", 1, "black", "10.11.2022")



