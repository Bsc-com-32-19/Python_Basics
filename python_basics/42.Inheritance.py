# this is the mechanism of reusing the code
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


def be_annoying():
    print("annoying")


dog1 = Dog()
dog1.walk()
dod2 = Dog()
dod2.bark()

cat1 = Cat()
be_annoying()
