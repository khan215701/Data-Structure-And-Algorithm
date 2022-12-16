import sys
sys.setrecursionlimit(100)

zero, one = 0, 1


def powerOfNumber(base, exp):
    assert zero <= exp == int(exp), 'Exponent must be positive and integer'
    if exp == zero:
        return one
    if exp == one:
        return base
    return base * powerOfNumber(base, exp-1)


base, exp = 2, 6
result = powerOfNumber(base, exp)
print(f'{base} by power of {exp}: {result}')