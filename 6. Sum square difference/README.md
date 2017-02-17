>Sum square difference

>Problem 6

>The sum of the squares of the first ten natural numbers is,

>1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385

>The square of the sum of the first ten natural numbers is,

>(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025

>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


## 平方和
前10个自然数的平方和是  
1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385
 
前10个自然数的和的平方是
(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025
 
这两者之差是 3025 − 385 = 2640
### 问:

求前100个自然数的和的平方与平方和之差

### 答:
25164150

### 解答过程:

这道题可以简单暴力的用两行代码解决
```python
def resolve1(n):
    seq = range(1, n + 1)
    return sum(seq) ** 2 - sum([i ** 2 for i in seq])
```
以上算法的时间复杂度是O(n), 但是我想, 这不是出题者的目的. 我们应该用更简单, 更高效的方法来解决问题.

对于求和, 我们可以使用我们熟知的高斯求和公式, f(n)=n*(n+1) / 2

求平方和, 我们也可以使用平方和的公式  f(n) = 1/6 * (2n<sup>3</sup> + 3n<sup>2</sup> + n)= n*(2n+1)*(n+1)/6.

使用以上公式,  我们可以得到以下改进之后的算法
```python

def resolve2(n):
    _sum = n * (n + 1) / 2
    sum_square = n * (n + 1) * (2 * n + 1) / 6
    return _sum ** 2 - sum_square
```
时间复杂度将降低至O(1)

[示例代码](problem_2.py)

