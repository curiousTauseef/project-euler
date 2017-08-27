def solve():
    a = range(100, 1000)
    return max(i*j for i in a for j in a if is_palindrome(i*j))

def is_palindrome(number):
    return str(number) == str(number)[::-1]

if __name__ == '__main__':
    print(solve())
