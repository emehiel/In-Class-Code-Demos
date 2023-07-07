#############
# Basic function definition
def my_function():
    print("Hello from a function")


my_function()


################
# Basic argument passing
def my_function(l, i):
    i += 3
    print(i)
    j = l[:]
    l[0] = 'a'
    for x in l:
        print(x)


L = [1, 2, 3]
i = 3

# notice, L is a reference type and i is a value type
my_function(L, i)
print(L)
print(i)

#############
# Advanced Arguments (slide 5)


def my_func1(*args):
    for x in args:
        print(x)


my_func1(1, 'a')


def my_func2(**kid):
    print("His last name is " + kid["lname"])


my_func2(fname="Tobias", lname="Refsnes")


def my_func3(a, b):
    print(a, b)


my_func3(b='three', a='a')


def my_func4(course='Aero 470'):
    print(course)


print(my_func4())
print(my_func4)

#############
# Return Values (slide 6)


def my_function(x):
    return 5 * x


x = my_function(3)

print(my_function(3))
print(my_function(5))
print(my_function(9))

###################
# Recursion (slide 7)


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

###############
# Class/Object Example


class Dog:
    # A simple class to represent a dog

    # class attributes - all instances of a dog have this variable/value
    genus = 'canine'

    # constructor
    def __init__(self, name, toy):
        # instance attributes - only this specific instance of a dog have these values
        self.name = name
        self.toy = toy

    # method
    def play(self):
        print('I like to play with a', self.toy)

    # Other methods like run and eat


piper = Dog('Piper', 'ball')
daisy = Dog('Daisy', 'rope')

print(piper.genus)
print(daisy.genus)

# Notice, when genus changes at class level of Dog, it changes for all Dogs
Dog.genus = "puppy"

print(piper.genus)
print(daisy.genus)

print(piper.play())
print(daisy.play())
