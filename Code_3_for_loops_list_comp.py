############
# The basic while loop (slide 3, 4, 5)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The range() method is new – kind of like linspace()
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 10, 3):
    print(x)

# Can use break, continue and else just like while loops

# nested loops just like Matlab

############
# More on list comprehension (slide 6)
# basic syntax l = [expression for item in list]

# expression can be a function


def myFunc(x):
    x *= 2
    return x


# notice l is a new variable, not a refernece to some other list (range(0,5,1) in this case)
l = [myFunc(x) for x in range(0, 5, 1)]
print(l)

############
# More on list comprehension (slide 7)
# Add some logic to determine which elements of the list to comprahend

c_list = ["green", "red", "blue", "yellow"]

midColors = [c for c in c_list if len(c) > 2 and len(c) < 5]

print(midColors)

############
# watch it - the iterable collection can be modified
# but, the 'color' is always the next item in the iterable list
# and does not change the iterable collection
# (if you are familiar with c-family and/or memory management:
#   * color' is a primitive, whereas...
#   * values within structures are stored as a reference)
for color in c_list:
    color = "purple"
    c_list[1] = "orange"
print(c_list)
