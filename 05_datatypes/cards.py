stack = []

for color in ['♠', '♥', '♦', '♣']:
    for value in [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q','K', 'A']:
        stack.append(str(value) + color)

print(stack)
