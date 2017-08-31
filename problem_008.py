import numpy as np

def solve(number):
    current_max = 0
    for slc in generate_slices(number):
        current_max = max(current_max, np.prod(to_list(slc)))
    return current_max

def to_list(string):
    return [int(a) for a in string]

def generate_slices(number, slice=13):
    for i in range(len(number)-slice):
        yield number[i:i+slice]

if __name__ == '__main__':
    number = open('data/problem_008').read().strip()
    generator = generate_slices(number, 10)
    print(solve(number))
