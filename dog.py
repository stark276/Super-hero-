class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    # Methods are defined as their own named functions inside the class
    # Remember to put the "self" parameter every time we make a class method!
    def bark(self):
        print("Woof!")

my_dog = Dog("Rex", "SuperDog")
# Remember python implicitly passes in "self",
# so we don't need to pass it in when we call the function!
my_dog.bark()