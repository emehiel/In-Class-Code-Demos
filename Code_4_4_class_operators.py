import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "I'm a circle, and my radius is " + str(self.radius)

    def __add__(self, o):
        # note: double-* is interpreted as exponent; you can also use math.exp, but *NOT* "^" which is a bitwise XOR
        r3 = math.sqrt(self.radius**2 + o.radius**2)
        return Circle(r3)


C1 = Circle(3)
C2 = Circle(4)

print(C1)

C3 = C1 + C2

print(math.pi)

print(C3)
