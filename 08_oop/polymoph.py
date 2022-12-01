class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}: I like {food}!')


class Kitten(Animal):
    def meow(self):
        print(f'{self.name}: Meow!')


class Puppy(Animal):
    def woof(self):
        print(f'{self.name}: Woof!')


animals = [Kitten('Micka'), Puppy('Azorek')]

for animal in animals:
    animal.eat('meat')
