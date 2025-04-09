## ![img](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/logo.png)      计算机与人工智能学院《人工智能程序设计》实验报告📝

| 专业                 | 学号         | 姓名         |
| :------------------- | ------------ | ------------ |
| 数据科学与大数据技术 | 2302320122   | 胡文韬       |
| **课程名称**         | **实验名称** | **完成日期** |
| 人工智能程序设计A        | lab04       | 2025.3.20    |



[TOC]

---



### 一 实验目标

1. **理解递归的思想**
2. **掌握递归和树递归的方法**
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

### 1. **Squared Virahanka Fibonacci**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab04$ python3 ok --local -q squared-virfib-wwpd -u
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Squared Virahanka Fibonacci > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def virfib_sq(n):
...     print(n)
...     if n <= 1:
...         return n
...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
>>> r0 = virfib_sq(0)
? 0
-- OK! --

>>> r1 = virfib_sq(1)
? 1
-- OK! --

>>> r2 = virfib_sq(2)
(line 1)? 2
(line 2)? 1
(line 3)? 0
-- OK! --

>>> r3 = virfib_sq(3)
(line 1)? 3
(line 2)? 2
(line 3)? 1
(line 4)? 0
(line 5)? 1
-- OK! --

>>> r3
? 4
-- OK! --

>>> (r1 + r2) ** 2
? 4
-- OK! --

>>> r4 = virfib_sq(4)
(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 2
(line 8)? 1
(line 9)? 
-- Not quite. Try again! --

(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 2
(line 8)? 1
(line 9)? 0
-- OK! --

>>> r4
? 25
-- OK! --

---------------------------------------------------------------------
OK! All cases for Squared Virahanka Fibonacci unlocked.
```

---

### 2. **Line Stepper**

完成函数 line_stepper ，该函数返回从 start 到 0 沿着数字线，每次走 k 步，到达 0 的路径数。注意每步 必须 要么向左或者向右，不能呆在原地！
![image-20220411181504953](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220411181504953.png)

例如，上面显示了从 `3` 开始走 `5`  步的所有可能路径。在每一步中，要么向左要么向右移动一步，并最终到达 0

测试结果：

![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab04/lab04-2.png?raw=True)

---

### 3. **Summation**

函数要求：编写递归函数` summation`,  接受一个正整数 `n` 和一个函数  `term` 。该函数将 `term` 应用到 `1` 到 `n` （包括 `n`）并返回和。

**注意**：使用递归；如果使用任何的循环（for， while），测试将失败。

代码实现：

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
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n - 1, term)
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab04/lab04-3.png?raw=True)

---

### 4. **`Insect Combinatorics`函数**

考虑一只在 *M* x *N* 网格中的昆虫。昆虫从左下角 *(1, 1)* 开始（start），并希望最终在右上角*(M, N)* 结束（goal）。昆虫只能向右或向上移动。编写一个函数，该函数接受网格的长度和宽度，并返回昆虫从 start 到 goal 可以采取的不同路径数。（此问题有一个  [closed-form solution](https://en.wikipedia.org/wiki/Closed-form_expression)，但请尝试使用递归回答。）

![image-20220415101731936](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220415101731936.png)

例如，2 x 2 网格总共有两种方式让昆虫从起点移动到目标。对于 3 x 3 网格，昆虫有 6 个不同的路径（上面只显示了 3 个）。

**提示**：如果碰到最顶端或最右边会发生什么？

代码实现：

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
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab04/lab04-4.png?raw=True)

---

### 5. **Yanghui's Triangle**
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

代码实现：

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
    if column < 0 or column > row:
        return 0
    if row == 0 or column == 0 or column == row:
        return 1
    return pascal(row - 1, column) + pascal(row - 1, column - 1)

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab04/lab04-5.png?raw=True)

### 五 实验心得

实验内容较多，较之前有一定难度提升，但编程中暂未遇到困难。在服务器上使用conda创建环境python=3.10，运行正常。实验报告使用vscode安装markdown插件编写。



