import sys
sys.setrecursionlimit(100)
limit = 10


def sumOfDigits(n):
    assert 0 <= n == int(n), 'Number must be positive and integer.'
    if n < limit:
        return 1
    return int(n % 10) + int(sumOfDigits(n/10))


result = sumOfDigits(1345)
print(result)
