def lsb_to_kg(weight):
    return weight * 0.45


def kg_to_lsb(weight):
    return weight / 0.45


# Exercise
from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(max(numbers))
