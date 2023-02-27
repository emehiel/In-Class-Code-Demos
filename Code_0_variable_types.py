# Comments (slide 8)

# this is a comment
"""
This is a literal multi-line string
that looks like a comment
and will be ignored by Python
"""

# Python is dynamically typed (slide 9)

x = 2  # int
y = 2.  # float

s = str(3)  # cast an int to a double
s = 'name'
s = "name"

# the type key word
sType = type(s)
print(sType)

xType = type(x)
print(xType)

thisVariable = 42  # camelCase

x, y, z = 1, 2, 3
x = y = z = 'strange'
x, y = ['apple', 'banana']

print(s)

# Strings (slide 12)

A = 'string'
print(A[1])

age = 3
txt = "My name is John, and I am {}"
print(txt.format(age))

# Operators to watch (slide 14)

x = 2**3
x = 2//3

i = 3
i += 1
