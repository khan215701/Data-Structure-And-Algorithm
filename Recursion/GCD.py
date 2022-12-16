import sys
sys.setrecursionlimit(100)

# Euclidean algorithm


def GCD(a, b):
    assert int(a) == a and int(b) == b, 'a and b must be integer number'
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    return GCD(b, a % b)


result = GCD(18, 3)
print(result)