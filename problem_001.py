def solve():
    return sum([i for i in range(1000) if is_multiple(i)])

def is_multiple(number):
    return number%3==0 or number%5==0

if __name__ == '__main__':
    print(solve())
