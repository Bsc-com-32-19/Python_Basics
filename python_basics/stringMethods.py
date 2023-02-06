course = 'python for Beginners'
# len is a function which is general it can count everything not only chars
print(len(course))

# method is when a function belongs to a specific object // here upper method belongs to strings
course = 'python for Beginners'
print(course.upper())
print(course.lower())
print(course)

# To find the index of the character we use find method
course = 'python for Beginners'

# find method is case-sensitive it will display -1 because there is no small b
print(course.find('b'))
print(course.find('p'))

# To replace the characters we use replace method
course = 'python for Beginners'
print(course.replace('Beginners','absolute Beginners'))

# Replace method is also case-sensitive since we do not have small b in the word Beginners it will print the original
print(course.replace('beginners','absolute Beginners'))

# if we want to see the sequence of the character
course = 'python for Beginners'
print('python' in course)
# if it is not there it will display for we use boolean value
course = 'python for Beginners'
print('Python' in course)

# len() method used to count characters
# find() method to check index of words or characters
# replace() method to replace word or characters
# upper() method to display the characters in upper case
# lower() method to display the characters in lower case
# title() method to display the title
# '....'in() method to check if that word or characters are present or not
