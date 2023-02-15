def find_max(numbers):
    maximun = numbers[0]
    for number in numbers:
        if number > maximun:
            maximun = number
    return maximun
