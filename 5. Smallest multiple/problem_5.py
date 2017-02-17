# coding=utf-8
"""
Smallest multiple
Problem 5. Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def factors(k):
    """
    求k中质因数的个数
    :param k:
    :return: {质因数: 个数}
    """
    a = {}
    i = 2

    while i <= k:
        if k % i == 0:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
            k /= i
            i = 2
        else:
            i += 1

    return a


def resolve(number):
    facts = {}
    for i in range(number, 1, -1):
        fac = factors(i)  # 求各个质因数的个数
        for k, v in fac.items():
            facts[k] = max(v, facts.get(k, 0))  # 更新质因数的个数为较大者

    return reduce(lambda x, y: x * y, [k ** v for k, v in facts.items()])


if __name__ == '__main__':
    # assert resolve(10) == 2520
    print resolve(20)
