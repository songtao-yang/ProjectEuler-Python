>Largest palindrome product 

>Problem 4

>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

>Find the largest palindrome made from the product of two 3-digit numbers.

## 最大回文数乘积

回文数是指反向排列后和原数字一样的数. 泪如1221这种.

最大的由两位数字的乘积得到的回文数是 9009 = 91 x 99
 
### 问:
求最大的由三位数字乘积得到的回文数

### 答:
906609

### 解答过程:

此题我附加了两个解法. 

[示例代码1](problem_4_1.py)

解法1是使用最简单的遍历求解方式

但是, 有没有更好的解法呢?

首先：999*999 = 998001并且100001 是一个回文数，这样就确定了我们所找的最大回文数一定是一个六位数。
然后有就有下面的数学推导：
```
abccba  
    = a*100000 + b*10000 + c*1000 + c*100 + b*10 +a*1
    = a*(100001) + b*(10010) + c*(1100)
    = 11*(9091*a + 910*b + 100*c)
```
可以看到, 这个数字一定是可以被11整除的

那么,  我们可以得到优化过之后的解法2

[示例代码2](problem_4_2.py)