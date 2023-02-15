import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
# select a names randomly from the list

members = ['mimie', 'shira', 'olie', 'Esinta']
leader = random.choice(members)
print(leader)


# Exercise
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
