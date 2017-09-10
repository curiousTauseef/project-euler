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
