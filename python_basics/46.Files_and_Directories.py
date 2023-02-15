from pathlib import Path

path = Path("ecommerce")
print(path.exists())
# create directory
#path = Path("email")
#print(path.mkdir())

path = Path("email")
print(path.exists())

# remove directory
path = Path("email")
#print(path.rmdir())

path = Path()
# use globe to search files
for file in path.glob('*.py'):
    for file in path.glob('*'):
        print(file)
print(file)
