import sys
sys.setrecursionlimit(100)


def decimalToBinary(n):
    assert int(n) == n, 'number must be integer.'
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(int(n/2))


result = decimalToBinary(10)
print(result)

0