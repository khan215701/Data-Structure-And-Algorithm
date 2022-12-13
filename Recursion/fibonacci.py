import sys
sys.setrecursionlimit(100)


def fibonacci(n):
    assert 0 <= n == int(n), 'Number must be positive and integer number'
    if n in [0, 1]:
        return 1
    else:
        # set fibonacci formula
        return fibonacci(n-1) + fibonacci(n-2)


# call fibonacci method
result = fibonacci(10)
print(result)
