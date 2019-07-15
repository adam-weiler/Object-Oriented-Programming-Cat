class Cat(): #A Cat class.
    def __init__(self, name, preferred_food, meal_time): #Every Cat has attributes name, preferred_food, and meal_time.
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self): #Returns a meaningful string that describes the instance.
        return f"Cat instance:name={self.name} preferred_food={self.preferred_food} meal_time={self.meal_time}"

    def eats_at(self): #An instance method that converts a 24-hour time into a 12-hour time. ie: 13 becomes 1pm.
        if (self.meal_time == 0): #0:00 is 12am.
            return str(self.meal_time + 12) + ' am'
        elif (self.meal_time == 12): #12:00 is 12pm.
            return str(self.meal_time) + ' pm'
        elif (self.meal_time < 12): #Any other time less than 12 is in the AM.
            return str(self.meal_time) + ' am'
        elif (self.meal_time <= 23): #Any other time less than 23 is in the PM.
            return str(self.meal_time - 12) + ' pm'
        else:
            return ('12 pm') #If number is too high, sets default to 24.

    def meow(self): #Returns an plain-English string that describes the instance.
        return f'My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}.'


felix = Cat('Felix', 'oreos', 17) #Creates an instance of the Cat class.
print(felix) #Prints the meaningful string.
# print(felix.eats_at())
print(felix.meow()) #Calls the meow instance method.
print()

garfield = Cat('Garfield', 'lasagna', 23) #Creates an instance of the Cat class.
print(garfield) #Prints the meaningful string.
# print(garfield.eats_at())
print(garfield.meow()) #Calls the meow instance method.
print()

hobbes = Cat('Hobbes', 'tuna casserole', 0) #Creates an instance of the Cat class.
print(hobbes) #Prints the meaningful string.
# print(hobbes.eats_at())
print(hobbes.meow()) #Calls the meow instance method.
print()

#These are extra things inside the hobbes object.
# print (hobbes.__dict__) #Dictionary containing the class's namespace: {'name': 'Hobbes', 'preferred_food': 'tuna casserole', 'meal_time': 0}
# print (hobbes.__doc__) #Class documentation string: None
    # print (hobbes.__name__) #Class name: There is no attribute __name__
# print (hobbes.__module__) #Module name in which the class is defined: __main__
    # print (hobbes.__bases__) #A possibly empty tuple containing the base classes, in the order of their occurance in the base class list: There is no attribute __bases__