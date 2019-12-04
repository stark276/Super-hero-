class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_time = sleep_duration

    def sleep(self):
        print(f"{self.name} sleeps for {self.sleep_time} hours ")


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


dog = Animal("Sophie", 12)
dog.sleep()
mydog = Dog("")