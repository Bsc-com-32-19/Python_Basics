names = ['mimie', 'jon', 'shilla', 'olivia']
print(names)
# we can print the list using index
names = ['mimie', 'jon', 'shilla', 'olivia']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

# we can print the list by specifying the first or the last index
names = ['mimie', 'jon', 'shilla', 'olivia']

# we can modify by using square brackets
names[1] = 'pro'
print(names[1: ])

# Exercise: find the largest number  in the list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print(max)
