def find_largest_prime_factor(number):
    factors = set() 
    for prime in generate_primes():
        while number%prime == 0:
            factors.add(prime)
            number /= prime
        if number == 1:
            break
    return max(factors)

def generate_primes():
    # horrible, but will do
    current = 2
    primes = []
    while True:
        for prime in primes:
            if current%prime == 0:
                break
        else:
            primes.append(current)
            yield current
        current += 1

if __name__ == '__main__':
    number = 600851475143
    print(find_largest_prime_factor(number))
