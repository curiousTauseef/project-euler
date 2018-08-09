import numpy as np
from itertools import count

def solve():
    for i in generate_sums():
        print(i)
        if i == 28:
            break

def generate_sums():
    for i in count():
        yield (i*(i+1))//2

if __name__ == '__main__':
    print(solve())
