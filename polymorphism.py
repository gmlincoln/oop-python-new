class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Tiger:
    def sound(self):
        print("Roar")


for animal in [Dog(), Cat(), Tiger()]:
    animal.sound()


