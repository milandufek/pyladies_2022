print("For with continue!")
for i in range(10):
    if i > 3 and i < 7:
        continue
    print(i)

print("\nFor with break!")
for i in range(10):
    if i > 3 and i < 7:
        break
    print(i)
