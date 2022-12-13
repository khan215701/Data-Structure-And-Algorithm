import sys
sys.setrecursionlimit(100)


def factorial(n):
    # avoid to negative number
    assert 1 <= n == int(n), 'Number must be positive'
    # return 1 if number is 0 or 1
    if n in [0, 1]:
        return 1
    # set recursion formula
    return n * factorial(n-1)


# call factorial method
result = factorial(10)
print(result)