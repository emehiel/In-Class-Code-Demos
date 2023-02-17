class Animal:

    genus = 'mammal'

    def __init__(self):
       pass

    def play(self):
        print('animals like to play')

class Dog(Animal):
    genus = 'canine'

    def __init__(self, name, toy):
        super().__init__()
        self.name = name
        self.toy = toy

    def play(self):
        print ("I'm a dog, and I like to play with", self.toy)

    def wag(self):
        print('My name is', self.name, "I'm a", self.genus, "and I wag my tail. Just sayin'")

class Cat(Animal):
    genus = 'feline'

    def __init__(self, name, toy):
        super().__init__()
        self.name = name
        self.toy = toy
    
    def play(self):
        print ("I'm a cat, and I like to play with", self.toy)

    def purr(self):
        print('My name is', self.name, "I'm a", self.genus, "and I purr. Just sayin'")

eleven = Animal()
piper = Dog('piper', 'ball')
tigger = Cat('tigger', 'yarn')

animals = [eleven, piper, tigger]

for animal in animals:
    animal.play()