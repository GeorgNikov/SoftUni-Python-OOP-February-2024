from abc import ABC, abstractmethod


class Animal(ABC):

    def get_species(self):
        return self.__class__.__name__.lower()

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return 'Meow'


class Dog(Animal):

    def make_sound(self):
        return 'woof-woof'


class Cow(Animal):

    def make_sound(self):
        return 'Moyyy'

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Cow()]
animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
# animal_sound(animals)
