def solve():
    step = 2*3*5*7*11*13*17*19
    divisors = [4, 8, 9, 12, 16, 18, 20]
    current = step
    while not divisible_by_all(current, divisors):
        current += step
    return current

def divisible_by_all(number, divisors):
    for divisor in divisors:
        if number%divisor != 0:
            return False
    return True

if __name__ == '__main__':
    print(solve())
