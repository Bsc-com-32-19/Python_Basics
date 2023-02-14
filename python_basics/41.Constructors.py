class Point:
    # constructor method
    def __init__(self, x, y):
        # initialising object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point = Point(10, 20)
Point.x = 11
print(Point.x)


# EXercise

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        # you can comment line 28
        print("talk")
        # or
        print(f"Hi, I am {self.name}")


Mirriam = Person("Mirrriam Yambeni")
# we can even remove or comment line 35
print(Mirriam.name)
Mirriam.talk()

Olivia = Person("Olivia Mtipeh")
Olivia.talk()
