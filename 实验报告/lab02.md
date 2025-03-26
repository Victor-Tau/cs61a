## ![img](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/logo.png)      计算机与人工智能学院《人工智能程序设计》实验报告📝

| 专业                 | 学号         | 姓名         |
| :------------------- | ------------ | ------------ |
| 数据科学与大数据技术 | 2302320122   | 胡文韬       |
| **课程名称**         | **实验名称** | **完成日期** |
| 人工智能程序设计A        | lab02       | 2025.3.20    |



[TOC]

---



### 一 实验目标

1. **掌握lambda 表达式**
2. **理解和运用Currying**
3. **学会处理错误信息**：

---



### 二 实验要求

- 个人独立完成，积极动手编程；
- 鼓励与同学交流，但不能抄袭源码；
- 能完成实验说明文档的各个步骤并撰写此实验报告；
- 能演示实验过程并阐述功能的主要代码模块。
- 实验报告请突出自己的**想法**、**做法**、**心得体会**；

---



### 三 实验环境

- 软件：Vscode
- 环境：python=3.10

---

### 四 实验内容 

通过几个问题，掌握python的基本语句

### 1. **WWPD: Lambda the Free**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab02$ python3 ok --local -q lambda -u
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 1
(cases remaining: 7)

Q: Which of the following statements describes a difference between a def statement and a lambda expression?
Choose the number of the correct choice:
0) A def statement can only have one line in its body.
1) A lambda expression cannot have more than two parameters.
2) A lambda expression does not automatically bind the function object that it returns to any name.
3) A lambda expression cannot return another function.
? 2
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 2
(cases remaining: 6)

Q: How many parameters does the following lambda expression have?
lambda a, b: c + d
Choose the number of the correct choice:
0) Not enough information
1) two
2) three
3) one
? 1
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 3
(cases remaining: 5)

Q: When is the return expression of a lambda expression executed?
Choose the number of the correct choice:
0) When the lambda expression is evaluated.
1) When you pass the lambda expression into another function.
2) When the function returned by the lambda expression is called.
3) When you assign the lambda expression to a name.
? 2
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 1
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
>>> lambda x: x  # A lambda expression with one parameter x
? Function
-- OK! --

>>> a = lambda x: x  # Assigning a lambda function to the name a
>>> a(5)
? 5
-- OK! --

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
? 3
-- OK! --

>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
? Function
-- OK! --

>>> c()
? 88
-- OK! --

>>> d = lambda f: f(4)  # They can have functions as arguments as well
>>> def square(x):
...     return x * x
>>> d(square)
? 16
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 2
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = None # remember to review the rules of WWPD given above!
>>> x
>>> lambda x: x
? Function
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 3
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> #
>>> # Pay attention to the scope of variables
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
? 4
-- OK! --

>>> f = lambda z: x + z
>>> f(3)
? Error
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 4
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # Try drawing an environment diagram if you get stuck!
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
? Error
-- OK! --

>>> higher_order_lambda(g)(2)
? 4
-- OK! --

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
? 3
-- OK! --

>>> print_lambda = lambda z: print(z)
>>> print_lambda
? Function
-- OK! --

>>> one_thousand = print_lambda(1000)
? 1000
-- OK! --

>>> one_thousand
? Nothing
-- OK! --

---------------------------------------------------------------------
OK! All cases for Lambda the Free unlocked.
```

---

### 2. **WWPD: Higher Order Functions**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab02$ python3 ok --local -q hof-wwpd -u
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
? Function
-- OK! --

>>> stewart(61)
? 61
-- OK! --

>>> stewart(-4)
? 4
-- OK! --

---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? beets
-- OK! --

>>> chocolate
? Function
-- OK! --

>>> chocolate()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> more_chocolate, more_cake = chocolate(), cake
? Function
-- Not quite. Try again! --

? sweets
-- OK! --

>>> more_chocolate
? 'cake'
-- OK! --

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
? Function
-- OK! --

>>> snake(10, 20)()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> cake = 'cake'
>>> snake(10, 20)
? 30
-- OK! --

---------------------------------------------------------------------
OK! All cases for Higher Order Functions unlocked.
```

---

### 3. **A Hop, a Skip, and a Jump**

函数要求：完成 `hop` ，它实现了函数  `f(x, y) = y`  的currying 版本

代码实现：

```python
def hop():
    """
    Calling hop returns a curried version of the function f(x, y) = y.
    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    return lambda x: lambda y: y
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-3.png?raw=True)

---

### 4. **`Digit Index Factory`函数**

函数要求：完成函数  `digit_index_factory`，接受两个整数 `k` 和 `num` 并返回一个函数。返回函数没有参数，并输出 `k` 和 `num` 最右边数位的偏移量，两个数的偏移量是指两个数之间的步长。例如，`25` 中 `2` 和 `5` 的偏移量是 `1`。

注意 `0` 表示没有数位（即使是 `0` 本身）

代码实现：

```python
def digit_index_factory(num, k):
    """
    Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).
    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    index = 0
    while num:
        if num % 10 == k:
            return lambda: index
        index += 1
        num //= 10
    return lambda: -1

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-4.png?raw=True)

---

### 5. **Lambdas and Currying**

函数要求：编写函数`lambda_curry2`,  使用 lambda 对任意的双参数函数 currying。

**你的答案只能写在 return 行**。 你可以试着先写没有这个限制的答案，然后再重写到 return 行。

代码实现：

```python
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-5.png?raw=True)

---

### 6. **Count van Count**

函数要求：编写函数 `count_cond` 来泛化这个逻辑，接受双参数的 predicate 函数 `condition(n, i)` ， `count_cond` 返回一个参数 `n` 的函数，函数调用时统计从 1 到 `n` 所有满足条件 `condition` 的数字个数。 

代码实现：

```python
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def counter(n):
        count = 0
        for i in range(1, n + 1):
            if condition(n, i):
                count += 1
        return count
    return counter
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-6.png?raw=True)

---

### 7. **Composite Identity Function**

函数要求：编写一个函数，接受两个单参数函数 `f` 和 `g`，并返回另一个单参数 `x` 的**函数**。如果 `f(g(x))`  等于  `g(f(x))`，则函数返回 True。你可以假定 `g(x)` 的输出是 `f` 的有效输入，反之亦然。尝试使用下面定义的函数 `composer` 来进行更多的 高阶函数练习。

代码实现：

```python
def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))


def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    return lambda x: f(g(x)) == g(f(x))

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-7.png?raw=True)

---

### 8. **I Heard You Liked Functions...**

函数要求：定义函数 `cycle` ，接受三个参数 `f1` , `f2` , `f3` 。`cycle` 将返回另一个函数，该函数接受一个整型参数 `n` 并返回另外一个函数，而最后这个函数应该接受一个参数 `x` 并循环地将  `f1` , `f2` , `f3`  应用到 `x` 上。下面是 对于 `n` 的一些值，最终的函数应该对 `x` 做什么：

- `n = 0`, 返回 `x`
- `n = 1`, 应用 `f1` 到 `x`, 或者返回 `f1(x)`
- `n = 2`, 应用 `f1` 到 `x` 然后应用 `f2` 到刚才的结果上，或者返回 `f2(f1(x))`
- `n = 3`, 应用 `f1` 到 `x`, `f2` 到 应用 `f1` 的结果, 然后 `f3` 到 应用 `f2` 的结果, 或者 `f3(f2(f1(x)))`
- `n = 4`, 重新开始这个循环应用，应用 `f1`, 然后 `f2`, 然后 `f3`, 然后又 `f1` , 或者 `f1(f3(f2(f1(x))))`
- 继续下去.

> 提示：最多的工作在最里面嵌套的函数中。

代码实现：

```python
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def get_cycled_function(n):
        def apply_cycle(x):
            current = x
            for i in range(n):
                if i % 3 == 0:
                    current = f1(current)
                elif i % 3 == 1:
                    current = f2(current)
                else:
                    current = f3(current)
            return current
        return apply_cycle
    return get_cycled_function

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab02/lab2-8.png?raw=True)

---




### 五 实验心得

实验内容较多，较之前有一定难度提升，但编程中暂未遇到困难。在服务器上使用conda创建环境python=3.10，运行正常。实验报告使用vscode安装markdown插件编写。



