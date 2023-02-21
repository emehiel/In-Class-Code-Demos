class Animal:

    genus = 'mammal'

    def __init__(self):
        pass

    def play(self):
        print('animals like to play')


# every Dog is an Animal
class Dog(Animal):
    genus = 'canine'


# every Cat is an Animal
class Cat(Animal):
    genus = 'feline'


eleven = Animal()
piper = Dog()
tiger = Cat()

print(eleven.genus)
print(piper.genus)
print(tiger.genus)

piper.play()
tiger.play()
