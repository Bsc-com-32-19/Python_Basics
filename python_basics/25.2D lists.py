
matrix = [
   [ 1, 2, 3],
   [ 4, 5, 6],
   [ 7, 8, 9]

 ]
# this means first matrix is in o index en print a number at index 1
matrix[0][1] = 30 # modifying
print(matrix[0][1])

# we can also use nested loops
for row in matrix:
    for item in row:
        print(item)