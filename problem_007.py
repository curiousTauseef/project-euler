from utils import generate_primes

def solve():
    generator = generate_primes()
    for _ in range(10001):
        current = next(generator)
    return current

if __name__ == '__main__':
    print(solve())
