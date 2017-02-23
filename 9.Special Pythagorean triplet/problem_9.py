# -*- coding: utf-8 -*-
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def resolve(n):
    for a in range(1, n / 2 - 2):
        for b in range(a, n / 2 - 1):
            c = n - a - b
            if not c > b:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return None

if __name__ == '__main__':
    ret = resolve(1000)
    print ret, reduce(lambda x, y: x * y, ret)
