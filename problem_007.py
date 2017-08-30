def solve():
    generator = generate_primes()
    for _ in range(10001):
        current = next(generator)
    return current

def generate_primes():
    #some improvement on the prime generator from problem 3
    comp = {}
    candidate = 2
    while True:
        if candidate not in comp:
            yield candidate
            comp[candidate**2] = [candidate]
        else:
            for prime in comp[candidate]:
                comp.setdefault(prime+candidate, []).append(prime)
            del comp[candidate]
        candidate += 1

if __name__ == '__main__':
    print(solve())
