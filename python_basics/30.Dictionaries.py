# defining keys in dictionary // each key should be unique no duplicate
customer = {
    "name": "Mirriam Yambeni",
    "age": 22,
    "is_verified": True
}
# to access the values from the dictionary
print(customer["name"])
# use get method
print(customer.get("birthdate"))  # this will display none cos
# in the dictionary we don't have that key word.

# we may assign the value together with
# the key word if in the dictionary doesn't exist
print(customer.get("birthdate", "May 04 2000"))

# we can update the keys in the dictionary
customer["name"] = "Olivia Mtipeh"
print(customer["name"])
