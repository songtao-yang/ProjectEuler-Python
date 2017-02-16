# coding=utf-8
"""
Largest prime factor
Problem 3.Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def factors(k):
    assert k >= 2
    a = []
    i = 2

    while i <= k:
        if k % i == 0:
            a.append(i)  # 存入因数
            k /= i  # 继续对余数进行因数分解
            i = 2
        else:
            i += 1

    return a


if __name__ == '__main__':
    print factors(600851475143)[-1]
