# Collections
# List = [] ordered and changeable. Duplicates ok
# Set = {} unordered and immutable, but add/remove ok. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates ok. Faster (use tuples for speed/efficiency when possible)

## LISTS

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# print(fruits[0:3])
# print(fruits[::2])

# for fruit in fruits:
#     print(fruit)

fruits = ["apple", "orange", "banana", "coconut"]
fruits[1] = "kiwi"
fruits.append("dragonfruit")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
## fruits.clear()
## print(fruits.index("apple"))
print(fruits.count("kiwi"))
for fruit in fruits:
    print(fruit)

## SETS

# fruits = {"apple", "orange", "banana", "coconut"}

# fruits.add("pineapple")
# fruits.pop() # random deletion of item
# print(fruits)

## TUPLES

# fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(fruits.index("apple"))
# print(fruits.count("coconut"))
