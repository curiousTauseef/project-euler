def solve():
    return sum(range(101))**2-sum(x**2 for x in range(101))

if __name__ == '__main__':
    print(solve())
