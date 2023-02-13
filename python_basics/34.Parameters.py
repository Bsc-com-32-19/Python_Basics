# pass information to your functions
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome dear')


print("Start")
greet_user("mimie")
greet_user("Olivia")
print("Finish")


# adding more parameters
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome dear')


print("Start")
greet_user("mimie", "Yambeni")
greet_user("Olivia", "Mtipe")
print("Finish")
