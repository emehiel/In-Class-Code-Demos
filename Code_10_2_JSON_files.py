import json
from json import JSONEncoder

class Contact():
    def __init__(self, name, age, address):
        if type(name) == Name:
            self.name = name
        else:
            self.name = Name(**name)
        self.age = age
        if type(address) == Address:
            self.address = address
        else:
            self.address = Address(**address)
            
    def __str__(self):
        return '{0} lives at {1} and is {2} years old'.format(self.name, self.address, self.age)

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class Address:
    def __init__(self, number, street):
        self.number = number
        self.street = street

    def __str__(self):
        return "{0} {1}".format(self.number, self.street)

class ContactEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

name = Name('Eric', 'Mehiel')
address = Address(123, 'Main St.')

contact = Contact(name, 49, address)

contactJson = json.dumps(contact, indent=4, cls=ContactEncoder)
print('Contact JSON')
print(contactJson)

j = json.loads(contactJson)
#Contact({'name':'Eric'})
#Contact(**{'name':'Eric', 'address': 3, 'age': 37})
contactObj = Contact(**j)
print(contactObj)