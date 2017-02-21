>10001st prime

>Problem 7

>By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

>What is the 10 001st prime number?


##  第10001个质数
列出前6个质数, 它们分别是2, 3, 5, 7, 11, 和 13. 第六个质数是13

 
### 问:
第10001个质数是多少?

### 答:
104743

### 解答过程:

此题我们使用较为简单的方法, 来判断一个数是否为质数.
```python
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
```

然后, 逐个判定是否质数
```python
def calc_prime(limit):
    count = 1  # we know that 2 is prime
    candidate = 3
    while count < limit:
        if is_prime(candidate):
            count += 1
        candidate += 2
    return candidate
```

[示例代码](problem_7.py)