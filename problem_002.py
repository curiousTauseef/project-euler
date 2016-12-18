MAX_VALUE = 4000000

def solve():
    return sum([i for i in fibonacci() if is_even(i)])

def fibonacci(): #we only care for even elements, so we may skip the first two
    x1 = 1
    x2 = 1
    while x2 < MAX_VALUE:
        x1 = x1+x2
        x1, x2 = x2, x1
        yield x2

def is_even(number):
    return (number & 1) == 0

if __name__ == '__main__':
    print(solve())
