from random import randrange


#
# definition: tuple (immutable)
#
def dice_throw():
    return randrange(1, 6), randrange(1, 6)


a, b = dice_throw()
print(f'Hodila jsi čísla: {a} a {b}')


#
# definition: dict (mutable)
#
#   'key': 'value'
animals = {
    'dog': 'pes',
    'cat': 'kočka',
    'snake': 'had',
    'turtle': 'želvička',
}
for k, v in animals.items():
    print(f'{k} -> {v}')


#
# definition: list (mutable)
#

# indexes: 0  1  2  3  4  5   6  7
my_list = [1, 5, 6, 2, 8, 8, 99, 0]
# call
# my_list[4]  # returns: 8


# !!! never do this !!!
# for i in my_list:
#     my_list.append(i + 10)

# Do this instead:
# new_list = []
# for i in my_list:
#     new_list.append(i + 10)
