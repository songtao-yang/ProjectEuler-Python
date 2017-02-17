"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def resolve1(n):
    seq = range(1, n + 1)
    return sum(seq) ** 2 - sum([i ** 2 for i in seq])


def resolve2(n):
    _sum = n * (n + 1) / 2
    sum_square = n * (n + 1) * (2 * n + 1) / 6
    return _sum ** 2 - sum_square


assert resolve1(10) == 2640
assert resolve2(10) == 2640

print resolve1(100)
print resolve2(100)
