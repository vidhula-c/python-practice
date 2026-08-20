# Creating a list
fruits = ["apple", "banana", "mango"]

print(fruits)

# Accessing elements
print(fruits[0])
print(fruits[1])

# Adding an element
fruits.append("orange")
print(fruits)

# Changing an element
fruits[1] = "grapes"
print(fruits)

# Removing an element
fruits.remove("mango")
print(fruits)

# Length of the list
print(len(fruits))

# Checking if an element exists
print("apple" in fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)