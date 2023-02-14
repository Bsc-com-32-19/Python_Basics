# this prevents the code from crushing wen encountering an error it throws an exception
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0.')
except ValueError:
    print('Invalid value')