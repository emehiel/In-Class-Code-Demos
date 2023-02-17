###########
# Basic logic (slide 3)
a = True
b = False

r = a == b
r = a != b

a, b = 3, 5

r = a < b
r = a <= b
r = a > b
r = a >= b

###########
# Basic If ... Else (slide 4, 5, 6)
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# use pass if needed
if a < b:
    pass

# Ternary Operator like ? : in other languages
print("A") if a > b else print("B")

############
# The basic while loop (slide 7, 8)
i = 1
while i < 6:
    print(i)
    i += 1

# break and continue
i = 1

while i < 6:
    while 1 < 8:
        print(i)
        break
    i += 1

# add an else
i = 1
while i < 6:
    print(i)
    if i == 2:
        continue
    i += 1
else:
    print("i is greater than 5")

print('sdfs\'df')