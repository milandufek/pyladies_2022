from math import pi, sqrt


def sum(a, b):
    return a + b


def multiply(number, multiplicator):
    return number * multiplicator


def milans_theorem(x, y, z):
    quantum = pi * x**3 + 16 / y + z
    # return str(round(sqrt(quantum)))
    return round(sqrt(quantum))


if __name__ == '__main__':
    print(sum(1, 6))
    print(multiply(5, 5))
    print(milans_theorem(1, 2, 3))
