"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(value):
    tmp = str(value)
    for i in range(0, len(tmp) / 2):
        if not tmp[i] == tmp[-i - 1]:
            return False
    return True


def max_palindrome():
    a = b = ret = 0
    min_value = 10 ** 2
    max_value = 10 ** 3 - 1
    for i in range(max_value, min_value - 1, -1):
        if i % 11 == 0:
            j = max_value
            step = 1
        else:
            j = int(max_value / 11) * 11
            step = 11
        while j >= i:
            value = i * j
            if value <= ret:
                break
            if is_palindrome(value):
                a = i
                b = j
                ret = value

            j -= step

    return a, b, ret


if __name__ == '__main__':
    result = max_palindrome()
    print '%d * %d = %d' % result
