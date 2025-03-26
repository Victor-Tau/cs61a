

# 实验2 高阶函数、lambda表达式

> **练习完成方式：独立完成**
>
> **实验源码：仔细阅读此文档，编写程序完成指定功能，并运行测试通过，推荐Git管理项目文档 [Gitlab](https://10.177.76.140:1043/)** 
>
> **实验文档撰写：要求使用 markdown格式书写，推荐使用 [Typora](https://typora.io/)**
>
> **要求每个功能函数编写至少2-3个测试用例，一个常规例子，一到多个极端例子**

[TOC]

## 概述

### 提供的材料

下载 [lab02.zip](./lab02.zip)（或者见作业附件），你会发现这次实验问题的开始文件，还包括一个自动评分工具 Ok

### 需提交的材料

- .py 源程序文件
- .md 实验记录文档

## 话题

这个小节内容供你翻新一下实验所涉及的内容，你可以直接跳到 [问题](#问题)，卡住的时候再回来看。

### lambda 表达式

lambda 表达式是计算结果为函数得表达式，通过指定两件事情实现：参数和返回的表达式。

```
lambda <parameters>: <return expression>
```

虽然 `lambda` 表达式 和 `def` 语句都创建了函数对象，单存在一些明显的差异。`lambda` 表达式和其他的表达式一样；就像数学表达式只是计算为一个数字并且不改变当前环境一样，`lambda` 表达式在不更改当前环境的情况下计算为函数。让我们仔细看看。

|              | lambda                                                       | def                                                          |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 类别         | 计算结果为值的**表达式**                                     | 改变环境的**语句**                                           |
| 执行结果     | 创建没有内部名称的匿名 lambda 函数                           | 创建具有内部名的函数，并将其绑定到当前环境中的名             |
| 对环境的影响 | 计算 `lambda` 表达式**不会**创建或修改任何变量               | 执行 `def` 语句既会创建一个新的函数对象，又会将其绑定到当前环境中的名 |
| 用法         | `lambda` 表达式可以在任何需要表达式的地方使用，例如在赋值语句中，或者作为调用表达式的操纵符或操作数 | 执行 `def` 语句后，创建的函数将绑定到名。在需要表达式的任何位置，你应该使用此名引用此函数 |

对比例子：

```python
# A lambda expression by itself does not alter
# the environment
lambda x: x * x

# We can assign lambda functions to a name
# with an assignment statement
square = lambda x: x * x
square(3)

# Lambda expressions can be used as an operator
# or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)
```

和

```python
def square(x):
    return x * x

# A function created by a def statement
# can be referred to by its intrinsic name
square(3)
```

### Currying

我们可以将多参数函数转换成单参数链的高阶函数。例如，可以将函数 `f(x, y)` 编写为高阶函数 `g(x)(y)`。这被称为**咖喱**（currying）。

举个例子，要将函数 `add(x, y)` 转换为其 curry 形式，请执行以下操作：

```python
def curry_add(x):
    def add2(y):
        return x + y
    return add2
```

调用 `curry_add(1)` 将返回一个新函数，该函数仅当返回的带第二个加数的函数被调用时执行加法运算。

```python
>>> add_one = curry_add(1)
>>> add_one(2)
3
>>> add_one(4)
5
```

> 有关currying的更多详细信息，请参阅[参考书](http://composingprograms.com/pages/16-higher-order-functions.html#currying)。

## 问题 <a name ="问题"></a>

### What Would Python Display？（WWPD）

> 注意：对所有的 WWPD 问题，如果你认为答案是 `<function...>`,  就敲入 `Function` ;  是错误，就敲入 'Error'；是什么都不显示，就敲入 `Nothing`

#### 问题1：WWPD: Lambda the Free

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```shell
> python3 ok -q --local lambda -u
> ```
>
> 提示一下,下面的两行代码再Python解释器中执行时不会显示任何内容：
>
> ```python
> >>> x = None
> >>> x
> ```

```python
>>> lambda x: x  # A lambda expression with one parameter x
______

>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
______

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
______

>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
______

>>> c()
______

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
______
```

```python
>>> x = None # remember to review the rules of WWPD given above!
>>> x
>>> lambda x: x
______
```

```python
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
______

>>> f = lambda z: x + z
>>> f(3)
______
```

```python
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
______

>>> higher_order_lambda(g)(2)
______

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
______

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
______

>>> one_thousand = print_lambda(1000)
______

>>> one_thousand
______
```

#### 问题2: WWPD: Higher Order Functions

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```
> python3 ok -q --local hof-wwpd -u
> ```

```python
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
______

>>> stewart(61)
______

>>> stewart(-4)
______
```



```python
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
______

>>> chocolate
______

>>> chocolate()
______

>>> more_chocolate, more_cake = chocolate(), cake
______

>>> more_chocolate
______

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
______

>>> snake(10, 20)()
______

>>> cake = 'cake'
>>> snake(10, 20)
______
```

### Parsons 问题

#### 问题3：A Hop, a Skip, and a Jump

完成 `hop` ，它实现了函数  `f(x, y) = y`  的currying 版本

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
    "*** YOUR CODE HERE ***"
```

#### 问题4：  Digit Index Factory

完成函数  `digit_index_factory`，接受两个整数 `k` 和 `num` 并返回一个函数。返回函数没有参数，并输出 `k` 和 `num` 最右边数位的偏移量，两个数的偏移量是指两个数之间的步长。例如，`25` 中 `2` 和 `5` 的偏移量是 `1`。

注意 `0` 表示没有数位（即使是 `0` 本身）

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
    "*** YOUR CODE HERE ***"
```

###  编程问题

#### 问题5：Lambdas and Currying

编写函数` lambda_curry2`,  使用 lambda 对任意的双参数函数 currying。

**你的答案只能写在 return 行**。 你可以试着先写没有这个限制的答案，然后再重写到 return 行。

> 如果语法检查不能通过：确保你去掉了 "***YOUR CODE HERE***" 这一行，这样语法检查就不会认为其是函数的一部分

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
    return ______
```

使用 Ok 测试你的代码：

```
python3 ok --local -q lambda_curry2
```

#### 问题6： Count van Count

考虑下面的实现  `count_factors` 和 `count_primes`:

```python
def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n
```

实现看上去很相似！编写函数 `count_cond` 来泛化这个逻辑，接受双参数的 predicate 函数 `condition(n, i)` ， `count_cond` 返回一个参数 `n` 的函数，函数调用时统计从 1 到 `n` 所有满足条件 `condition` 的数字个数。 

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
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q count_cond
```

#### 选做问题



#### 问题7：Composite Identity Function

编写一个函数，接受两个单参数函数 `f` 和 `g`，并返回另一个单参数 `x` 的**函数**。如果 `f(g(x))`  等于  `g(f(x))`，则函数返回 True。你可以假定 `g(x)` 的输出是 `f` 的有效输入，反之亦然。尝试使用下面定义的函数 `composer` 来进行更多的 高阶函数练习。

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
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q composite_identity
```

#### 问题8： I Heard You Liked Functions...

定义函数 `cycle` ，接受三个参数 `f1` , `f2` , `f3` 。`cycle` 将返回另一个函数，该函数接受一个整型参数 `n` 并返回另外一个函数，而最后这个函数应该接受一个参数 `x` 并循环地将  `f1` , `f2` , `f3`  应用到 `x` 上。下面是 对于 `n` 的一些值，最终的函数应该对 `x` 做什么：

- `n = 0`, 返回 `x`
- `n = 1`, 应用 `f1` 到 `x`, 或者返回 `f1(x)`
- `n = 2`, 应用 `f1` 到 `x` 然后应用 `f2` 到刚才的结果上，或者返回 `f2(f1(x))`
- `n = 3`, 应用 `f1` 到 `x`, `f2` 到 应用 `f1` 的结果, 然后 `f3` 到 应用 `f2` 的结果, 或者 `f3(f2(f1(x)))`
- `n = 4`, 重新开始这个循环应用，应用 `f1`, 然后 `f2`, 然后 `f3`, 然后又 `f1` , 或者 `f1(f3(f2(f1(x))))`
- 继续下去.

> 提示：最多的工作在最里面嵌套的函数中。


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
    "*** YOUR CODE HERE ***"
```

使用Ok测试你的代码

```
python3 ok --local -q cycle
```


