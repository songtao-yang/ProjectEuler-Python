# -*- coding: utf-8 -*-
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math


def is_prime(n):
    if n == 2:
        return True
    else:
        r = math.floor(math.sqrt(n))  # n rounded to the greatest integer r so that r*r<=n
        f = 3
        while f <= r:
            if n % f == 0:
                return False
            f += 2
        return True  # (in all other cases)


def calc_prime(limit):
    count = 1  # we know that 2 is prime
    candidate = 3
    while count < limit:
        if is_prime(candidate):
            count += 1
        candidate += 2
    return candidate


if __name__ == '__main__':
    print calc_prime(10001)
