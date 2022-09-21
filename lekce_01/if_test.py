vstup = input('Rozumis tomu (ano/ne): ')

rozhodnuti = vstup == 'ano'

if rozhodnuti:
    print('To je super!')
elif vstup == 'ne':
    print(':(')
else:
    print('Tak se uz rozhodni!')
