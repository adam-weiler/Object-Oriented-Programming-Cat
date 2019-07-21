class Cat:  # A Cat class.
    def __init__(
        self, name, preferred_food, meal_time
    ):  # Every Cat has attributes name, preferred_food, and meal_time.
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f'''The cat {self.name} likes {self.preferred_food} at {self.meal_time}:00.'''

    def eats_at(
        self
    ):  # Converts 24-hour time to a 12-hour time. ie: 13 becomes 1pm.
        if self.meal_time == 0:  # 0:00 is 12am.
            return str(self.meal_time + 12) + " am"
        elif self.meal_time == 12:  # 12:00 is 12pm.
            return str(self.meal_time) + " pm"
        elif self.meal_time < 12:  # Any other time less than 12 is in the AM.
            return str(self.meal_time) + " am"
        elif self.meal_time <= 23:  # Any other time less than 23 is in the PM.
            return str(self.meal_time - 12) + " pm"
        else:
            return "12 pm"  # If number is too high, sets default to 24.

    def meow(self):  # Returns an plain-English string.
        return f"My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}."


felix = Cat("Felix", "oreos", 17)
print(felix)
# print(felix.eats_at())
print(felix.meow())
print()

garfield = Cat("Garfield", "lasagna", 23)
print(garfield)
# print(garfield.eats_at())
print(garfield.meow())
print()

hobbes = Cat("Hobbes", "tuna casserole", 0)
print(hobbes)
# print(hobbes.eats_at())
print(hobbes.meow())
