

class Kitten:

    def __init__(self, name):
        self.max_lives = 12
        self.name = name
        self.lives = self.max_lives

    def meow(self):
        if self.is_alive():
            print(f'{self.name}: Meow!')

    def eat(self, food):
        if self.is_alive():
            if self.lives < self.max_lives and food == 'fish':
                self.lives += 1
            print(f'{self.name}: Meow meow! I like {food}!')
            self.meow()

    def set_name(self, new_name):
        self.name = new_name

    def is_alive(self):
        return self.lives > 0

    def lose_live(self):
        if self.is_alive():
            self.lives -= 1


micka = Kitten(name)
micka.meow()
print(micka.lives)
for _ in range(4):
    micka.lose_live()
    print(micka.lives)
micka.eat('fish')
micka.eat('dog')
micka.meow()
