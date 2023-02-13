def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome dear')


print("Start")
greet_user("mimie", "Yambeni")
# a keyword argument always come after the position argument not the vicavesa
greet_user("Olivia", last_name="Mtipe")


def calc_cost(total, shipping, discount):
    pass

# keyword arguments assign the values to the parameters
calc_cost(total=50, shipping=5,discount=0.1)
print("Finish")
