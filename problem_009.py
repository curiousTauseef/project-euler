def solve():
    for a in range(500, 0, -1):
        for b in range(500, 0, -1):
            if 1000*(a+b)-a*b == 500000:
                return a*b*(a**2+b**2)

if __name__ == '__main__':
    print(solve())
