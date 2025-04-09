

# 实验4 递归、树递归

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

下载 [lab04.zip](./lab04.zip)，你会发现这次实验问题的开始文件，还包括一个自动评分工具 Ok

### 需提交的材料

- .py 源程序文件
- .md 实验记录文档

## 话题

这个小节内容供你翻新一下实验所涉及的内容，你可以直接跳到 [问题](#问题)，卡住的时候再回来看。

### 递归

递归函数是函数体中直接或者间接调用自身的函数。

以 `factorial` 为例。

> factorial, 用 `!` 运算符表示，定义为：
>
> ```
> n! = n * (n-1) * ... * 1
> ```
>
> 例如，`5! = 5 * 4 * 3 * 2 * 1 = 120`

factorial 的递归实现如下：

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

从定义中可知 0！是 1，既然 `n==0` 是能计算阶乘的最小数字，可以用它当 基本情况（base case），递归部分也按照阶乘定义来，即，`n! = n * (n-1)!`

递归函数有3个重要部分：

1. **base case**。基本情况可以看作最简单的函数输入情况，或者当作递归停止条件。在上面的例子中，` factorial(1)`  是 `factorial` 的基本情况。

2. **Recursive call on a smaller problem**。你可以把这一步想成，对于当前问题所依赖的，在较小问题上的函数调用。并且假定这个较小问题上的递归调用会给我们预想的结果，称之为“递归的信仰之跃” （recursive leap of faith）。
3. **Solve the larger problem**。在第2步，我们找到了较小问题的解。我们现在想使用这个结果来弄清楚我们当前问题的解应该是什么，这就是我们想要从当前函数调用中返回的结果。在上面的例子中，我们可以通过将较小问题的解 `factorial(n-1)`（表示 `(n-1)!`）乘以 `n` 来计算 `factorial(n)` （因为 `n! = n * (n-1)!` ）。

本次实验中的问题将要求你编写递归函数。下面是一些通用提示：

- 比较矛盾的是，在函数编写完成之前，你需要假定该函数的功能已经完成；即所说的”递归的信仰之跃“。
- 思考如何利用更简单问题的解来解决当前问题。递归函数看似做的工作很少：记住要信仰之跃，要 **相信递归** 可以解决稍微小一点的问题，而不必担心它是如何解决的。
- 考虑最简单情况下的解是什么，这些就是基本情况 - 递归调用的停止点。请务必考虑是否遗漏了基本情况（这是递归失败的常见原因）。
- 首先编写迭代的版本可能会有所帮助。

### 树递归

树递归是不止调用一次自身的递归函数，产生一系列类似于树的调用。

例如，假设要递归计算 斐波那契数列的第 `n` 项，定义如下：

```python
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

 `fib(6)` 的调用结构看起来像一个倒置的树（ `f` 是  `fib`）：

![维拉汉卡-斐波那契树](https://cs61a.org/lab/lab04/assets/f6-call-tree.png)

每个 `f(i)`节点表示 表示对 `fib`的一次递归调用。每个 `f(i)` 递归调用都会再进行两个递归调用，即 `f(i-1)` 和 `f(i-2)`。每当到达 `f(0)` 或者 `f(1)`节点时，可以直接返回 `0` 或者 `1 `，不再有更多的递归调用，因为这些是基本情况。

换句话说，基本情况可以直接返回答案所需的信息，而不依赖于其他递归调用的结果。一旦到达一个基本情况，就可以开始从递归到基本情况的递归调用返回。

一般来讲，树递归对于在当前状态下存在多种可能或者选择的问题比较有效。在这类问题中，你可以为每个选择或每组选择进行递归调用。

## 问题 <a name ="问题"></a>

### What Would Python Display？（WWPD）

#### 问题1：Squared Virahanka Fibonacci

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```shell
> python3 ok -q --local squared-virfib-wwpd -u
> ```
>
> **提示**：如果你卡住了，试着画一下递归调用树：

```python
>>> def virfib_sq(n):
>>>     print(n)
>>>     if n <= 1:
>>>         return n
>>>     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
>>> r0 = virfib_sq(0)
______

>>> r1 = virfib_sq(1)
______

>>> r2 = virfib_sq(2)
______

>>> r3 = virfib_sq(3)
______

>>> r3
______

>>> (r1 + r2) ** 2
______

>>> r4 = virfib_sq(4)
______

>>> r4
______
```

### Parsons 问题

#### 问题2：Line Stepper

完成函数 `line_stepper` ，该函数返回从 `start` 到 `0` 沿着数字线，每次走 `k` 步，到达 0 的路径数。注意每步 **必须** 要么向左或者向右，不能呆在原地！

![image-20220411181504953](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220411181504953.png)

例如，上面显示了从 `3` 开始走 `5`  步的所有可能路径。在每一步中，要么向左要么向右移动一步，并最终到达 0

> line_stepper.py源代码文件在 parsons_probs 文件夹中，在终端通过 `cd` 命令进入该文件夹，并输入命令进行验证：
>
> ```
> python3 -m doctest line_stepper.py
> ```

```python
def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"
```

###  编程问题

#### 问题3：Summation

编写递归函数` summation`,  接受一个正整数 `n` 和一个函数  `term` 。该函数将 `term` 应用到 `1` 到 `n` （包括 `n`）并返回和。

**注意**：使用递归；如果使用任何的循环（for， while），测试将失败。

```python
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q summation
```

#### 问题4： Insect Combinatorics

考虑一只在 *M* x *N* 网格中的昆虫。昆虫从左下角 *(1, 1)* 开始（start），并希望最终在右上角*(M, N)* 结束（goal）。昆虫只能向右或向上移动。编写一个函数，该函数接受网格的长度和宽度，并返回昆虫从 start 到 goal 可以采取的不同路径数。（此问题有一个  [closed-form solution](https://en.wikipedia.org/wiki/Closed-form_expression)，但请尝试使用递归回答。）

![image-20220415101731936](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220415101731936.png)

例如，2 x 2 网格总共有两种方式让昆虫从起点移动到目标。对于 3 x 3 网格，昆虫有 6 个不同的路径（上面只显示了 3 个）。

**提示**：如果碰到最顶端或最右边会发生什么？

```python
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q paths
```

### 选做问题

#### 问题5：Yanghui's Triangle

杨辉三角给出了二项式展开的系数；如果展开表达式 `(a + b) ** n`，则所有系数都将在三角的第 `n` 行上找到，第 `i` 项的系数位于第 `i` 列。

一部分的杨辉三角：

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

杨辉三角中的每一个数都被定义为其上方和左上方这两项之和。行和列是从零索引的；也就是说，第一行是row 0 而不是row 1，第一列是column 0 而不是column 1。例如，杨辉三角中第 2 行第 1 列的项为 2。

现在，请定义一个过程 `pascal(row, column)` ，接受行 `row` 和列 `column`，找出杨辉三角中此位置的值。注意杨辉三角仅在某些区域定义；如果该项不存在，则使用 `0`。同时，也可以假定 `row >= 0` 和 `column >= 0`。

```python
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q pascal
```


