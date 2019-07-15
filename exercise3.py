class Cat():
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return (f'{self.name} likes to eat {self.preferred_food} at {self.meal_time}:00.')


felix = Cat('Felix', 'oreos', 17)
print(felix)
print()

garfield = Cat('Garfield', 'lasagna', 10)
print(garfield)
print()

hobbes = Cat('Hobbes', 'tuna casserole', 12)
print(hobbes)
print()