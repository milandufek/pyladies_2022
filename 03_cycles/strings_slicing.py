#    01234567
x = 'Čokoláda'

print(f'Celý řetězec je: {x}')
print('Indexován jako:  01234567')
print()
print(f'První 2 znaky: {x[:2]}')
print(f'Od 3. znaku až po konec: {x[2:]}')
print(f'Poslední 2 znaky: {x[-2:]}')
print(f'3-6 znak: {x[2:6]}')
print(f'Poslední znak: {x[len(x) - 1]:}')
