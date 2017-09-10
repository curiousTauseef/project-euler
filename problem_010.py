from utils import generate_primes

def solve():
    total = 0
    for prime in generate_primes():
        if prime > 2000000:
            return total
        else:
            total += prime

if __name__ == '__main__':
    print(solve())
