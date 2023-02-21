# Lists (slide 3)
# Basic definition with []
L = [1, 2, 3]

# A list can contain differt type elements
thisList = ['apple', 3, 2+4j]

# Lists can be indexed (0 based)
print(L[1])
print(L[0])

# Slice a list with :
print(L[1:2])

# this is a new list
L2 = L[:2]

# Lists are Ordered, Changeable, and Allow Duplicates

# List methods
L.insert(1, 5)
L.sort()
#thisList.sort() - error

###############################################
# Tuples (slide 4)
# Basic definition
T = (1, 2, 3)

# A tuple can contain differt type elements
thisTuple = ('apple', 3, 2+4j)

# Tuples can be indexed (0 based)
print(T[1])
print(T[0])

# Slice a tuple with :
print(T[1:2])

# this is a new tuple
L2 = T[:2]

# Tuples are Ordered, Unchangeable, and Allow Duplicates

# List methods
print(T.count(1))

print(thisTuple)

###############################################
# Sets (slide 5)
# Basic definition
S = {1, 2, 3}

# A tuple can contain differt type elements
thisSet = {'apple', 3, 2+4j}

# Tuples cannot be indexed
# print(S[1]) - Error

# or Sliced
# print(S[1:2]) - Error

# Sets are Unordered, Unchangeable, Unidexed and do not Allow Duplicates

# List methods
print(S.add(5))

print(thisSet)

###############################################
# Dictionaries (slide 6)
# Basic definition - a set of key:value pairs
D = {'a': 65, 'b': 66}


# A dictionary can contain differt type elements
thisDictionary = {'a': 65, 3: 2+4j, 'colors': ['R', 'G', 'B']}


# Dictionaries cannot be indexed
# print(S[1]) - Error

# or Sliced
# print(S[1:2]) - Error

# but we can index values by key
v = thisDictionary['colors']

# Dictionaries are Ordered, Changeable, and do not Allow Duplicates

# List methods
print(D.keys())
D.pop('a')

print(thisDictionary)

##########
# Looping on iterable collections (slide 7)
for x in thisList:
    print(x)

#############
# finding elements with in (slide 8)
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#############
# List comprahension (slide 9)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#############
# Copying Objects (slide 10)

L3 = L

L[1] = 'a'  # both L and L3 change

L4 = L.copy()
L[2] = 'b'  # L and L3 change, L4 does not

print(L)
