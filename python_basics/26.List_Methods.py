numbers = [5, 2, 1, 7, 4]
# inserting the number at the end of the list
numbers.append(20)
print(numbers)

# means at index 0 insert 10
numbers.insert(0, 10)
print(numbers)

# means removing number 4 from the list
numbers.remove(4)
print(numbers)
# means that all items in the list are going to be removed
numbers.clear()
print(numbers)

# remove the last item from the list
numbers = [5, 2, 1, 5, 7, 4]
numbers.pop()
print(numbers)

# to check the index of an item in the list
print(numbers.index(2))

# to check the existence of an item or list of characters
print(2 in numbers)
print(25 in numbers)
# we can count the frequency of an item by using count method
print(numbers.count(5))
# sort method // will be sorted in ascending order
numbers.sort()
# we can reverse the order by using reversal method // descending older
numbers.reverse()
print(numbers)
numbers = [5, 2, 1, 5, 7, 4]
# copy method, keep the copy of the first list
# being defined & does not change even if you want to add an item to the list
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)