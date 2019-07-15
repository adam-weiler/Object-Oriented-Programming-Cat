class Cat(): #A Cat class.
    def __init__(self, name, preferred_food, meal_time): #Every Cat has attributes name, preferred_food, and meal_time.
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self): #Returns a meaningful string that describes the instance.
        return f'{self.name} likes to eat {self.preferred_food} at {self.meal_time}:00.'

    def eats_at(self): #An instance method that converts a 24-hour time into a 12-hour time. ie: 13 becomes 1pm.
        if (self.meal_time == 0):
            return str(self.meal_time + 12) + ' am'
        elif (self.meal_time == 12):
            return str(self.meal_time) + ' pm'
        elif (self.meal_time < 13):
            return str(self.meal_time) + ' am'
        elif (self.meal_time < 24):
            return str(self.meal_time - 12) + ' pm'
        else:
            return ('12 pm')

    def meow(self): #An instance method subtracts the amount from the instance's balance.
        return f'My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}.'

felix = Cat('Felix', 'oreos', 17) #Creates an instance of the Cat class.
print(felix) #Prints the meaningful string.
# print(felix.eats_at())
print(felix.meow()) #Calls the meow instance method.
print()

garfield = Cat('Garfield', 'lasagna', 10) #Creates an instance of the Cat class.
print(garfield) #Prints the meaningful string.
# print(garfield.eats_at())
print(felix.meow()) #Calls the meow instance method.
print()

hobbes = Cat('Hobbes', 'tuna casserole', 24) #Creates an instance of the Cat class.
print(hobbes) #Prints the meaningful string.
# print(hobbes.eats_at())
print(hobbes.meow()) #Calls the meow instance method.
print()