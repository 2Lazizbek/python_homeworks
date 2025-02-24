class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating some food."

    def make_sound(self):
        return f"{self.name} makes a generic sound."

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age} years"

class Cow(Animal):
    def __init__(self, name, age, milk_produced):
        super().__init__(name, age)
        self.milk_produced = milk_produced

    def produce_milk(self):
        return f"{self.name} produced {self.milk_produced} liters of milk today."

    def make_sound(self):
        return f"{self.name} says 'Moo!'"

    def __str__(self):
        return f"{super().__str__()}, Milk Produced: {self.milk_produced} liters/day"

class Chicken(Animal):
    def __init__(self, name, age, eggs_laid):
        super().__init__(name, age)
        self.eggs_laid = eggs_laid

    def lay_egg(self):
        return f"{self.name} laid {self.eggs_laid} eggs today."

    def make_sound(self):
        return f"{self.name} says 'Cluck!'"

    def __str__(self):
        return f"{super().__str__()}, Eggs Laid: {self.eggs_laid}/day"

class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def gallop(self):
        return f"{self.name} is galloping at {self.speed} km/h!"

    def make_sound(self):
        return f"{self.name} says 'Neigh!'"

    def __str__(self):
        return f"{super().__str__()}, Speed: {self.speed} km/h"

# Demonstration of the farm model
def main():
    # Create some animals
    cow = Cow("Bessie", 4, 10)
    chicken = Chicken("Clara", 2, 3)
    horse = Horse("Thunder", 5, 40)

    # Store them in a list to iterate over
    farm_animals = [cow, chicken, horse]

    # Output details and behaviors
    print("Welcome to the Farm!")
    print("-" * 20)
    for animal in farm_animals:
        print(animal)  # Display attributes via __str__
        print(animal.eat())  # Shared behavior
        print(animal.make_sound())  # Unique sound
        # Call unique behavior based on type
        if isinstance(animal, Cow):
            print(animal.produce_milk())
        elif isinstance(animal, Chicken):
            print(animal.lay_egg())
        elif isinstance(animal, Horse):
            print(animal.gallop())
        print("-" * 20)

if __name__ == "__main__":
    main()