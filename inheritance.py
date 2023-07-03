class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("child classes must be implemented")


class Dog(Animal):

    def speak(self):
        return "woof!"


class Cat(Animal):

    def speak(self):
        return "meow"


class Cow(Animal):

    def speak(self):
        return "moo"


# create an object
dog = Dog("tom", "\nblack")
print(dog.name, dog.color)
print(dog.speak())

cat = Cat("\nJerry", "\nWhite")
print(cat.name, cat.color)
print(cat.speak())

cow = Cow("\nBen", "\nBrown")
print(cow.name)
print(cow.color)
print(cow.speak())
