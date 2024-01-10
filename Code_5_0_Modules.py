# Import the whole library
import math

# Give the library a shorter name/alias
import statistics as sts

# Import only specific functions or objects
from math import sinh, cosh, tanh

# Import a specific object and rename it
from math import pi as PI

# Does not work...
# from math import cos, sin as trigs

math.sinh(1)
sinh(2)

# Import the code that has the Animal Class definitions
# Note, this is terrible naming, but we can make it work
import Code_4_3_classes_poly_2 as ans

animal1 = ans.Animal()

piper = ans.Dog('Piper', 'Ball')
daisy = ans.Dog('Daisy', 'Rope')

dogs = [piper, daisy]
for d in dogs:
    print(d.name)