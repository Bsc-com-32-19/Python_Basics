coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# in prython there is a simple way to do everything as above by using unpacking method
x, y,z = coordinates # here it means unpacking the tuple of items and assign them to the variables respectively
print(x, y, z)

# we can unpack the list as well
coordinates = [1, 2, 3]
x, y,z = coordinates
print(x, y, z)
