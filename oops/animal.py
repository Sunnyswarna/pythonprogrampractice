from pandas.core.indexes.multi import names_compat


class Cat:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def info(self):
        print('my name is '+self.name + '\nMy age is ' + str(self.age))
    def make_sound(self):
        print('mew mew')
class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def info(self):
        print('My name is ' +self.name + '\nMy age is ' +str(self.age))
    def make_sound(self):
        print('bow bow')
def my_pet(pet):
    pet.info()
    pet.make_sound()
c= Cat('kitty',2)
d= Dog('Tommy',3)
my_pet(c)