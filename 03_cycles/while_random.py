from itertools import count
from random import randrange

lucky_number = int(input('Zadej svoje šťastné číslo (1-100): '))

print('Tak jdeme losovat...')

counter = 0
while True:
    counter += 1
    random_number = randrange(1, 101)

    if random_number == lucky_number + 1 or random_number == lucky_number - 1:
        print('Skoro!')
        continue

    if random_number == lucky_number:
        print('Tak to vyšlo!')
        print(f'Trvalo to jenom {counter}x')
        break

    print("Nevyšlo to :((")
