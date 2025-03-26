## ![img](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/logo.png)      计算机与人工智能学院《人工智能程序设计》实验报告📝

| 专业                 | 学号         | 姓名         |
| :------------------- | ------------ | ------------ |
| 数据科学与大数据技术 | 2302320122   | 胡文韬       |
| **课程名称**         | **实验名称** | **完成日期** |
| 人工智能程序设计A        | lab01       | 2025.3.20    |



[TOC]

---



### 一 实验目标

1. **掌握基本运算和操作符**：熟练掌握 Python 中与除法相关的操作符（除、整数除、取模）的使用，理解它们之间的区别，并能运用取模操作符进行整除判断，如判断一个数是否为偶数。
2. **理解和运用函数**：理解函数的定义、参数、返回值等概念，学会将重复的代码抽象成函数以避免代码冗余。掌握函数的调用表达式的语法和计算规则，明确`return`和`print`的区别，能够正确使用`return`语句返回函数的计算结果，并合理运用`print`函数进行输出展示。
3. **掌握控制语句**：熟练掌握 Python 中的布尔运算符（`and`、`or`、`not`），理解其运算规则、优先级以及短路特性；掌握`if`语句和`while`循环的语法和使用方法，能够根据不同的条件和需求编写正确的控制逻辑。
4. **学会处理错误信息**：熟悉常见的 Python 错误类型（如`SyntaxError`、`IndentationError`、`TypeError`、`ZeroDivisionError`等），能够根据错误信息准确判断代码中存在的问题，并学会利用搜索引擎等工具进行错误调试。

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

### 1. **WWPD: Control**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab01$ python3 ok --local -q control -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Control > Suite 1 > Case 1
(cases remaining: 5)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
? 23
-- OK! --

>>> xk(10, 6)
? 23
-- OK! --

>>> xk(4, 6)
? 6
-- OK! --

>>> xk(0, 0)
? 25
-- OK! --

---------------------------------------------------------------------
Control > Suite 1 > Case 2
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")
>>> how_big(7)
? 'big'
-- OK! --

>>> how_big(12)
? huge
-- OK! --

>>> how_big(1)
? small
-- OK! --

>>> how_big(-1)
? nothing
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> n = 3
>>> while n >= 0:  # If this loops forever, just type Infinite Loop
...     n -= 1
...     print(n)
(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? -1
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = 28
>>> while positive: # If this loops forever, just type Infinite Loop
...    print("positive?")
...    positive -= 3
(line 1)? Infinite Loop
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = -9
>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
(line 1)? -12
(line 2)? -9
(line 3)? -6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Control unlocked.
```

---

### 2. **WWPD: Contro**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab01$ python3 ok --local -q debugging-quiz -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 13
? 13
-- OK! --

>>> False or 0
? 0
-- OK! --

>>> not 10
? False
-- OK! --

>>> not None
? True
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 1 / 0 and False  # If this errors, just type Error.
? Error
-- OK! --

>>> True or 1 / 0 or False  # If this errors, just type Error.
? True
-- OK! --

>>> True and 0  # If this errors, just type Error.
? 0
-- OK! --

>>> False or 1  # If this errors, just type Error.
? 1
-- OK! --

>>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
? 15
-- OK! --

>>> -1 and 1 > 0 # If this errors, just type Error.
? True
-- OK! --

>>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
? 2
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> not 0
? True
-- OK! --

>>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
? 1
-- OK! --

>>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
? Error
-- OK! --

>>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Veritasiness unlocked.
```

---

### 3. **调试小测验**

下面是不同调试技术的一个快速小测验，对本课程的学习非常有用

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab01$ python3 ok --local -q debugging-quiz -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 8)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 7)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) the code looped infinitely
1) there was a missing return statement
2) the code attempted to add a string to an integer
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 6)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
2) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
3) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 5)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 4)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 3)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits --trace
1) python3 -i lab01.py
2) python3 ok -q sum_digits -i
3) python3 ok -q sum_digits
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 2)

Q: What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits
1) python3 ok -q sum_digits --trace
2) python3 ok -q sum_digits -i
3) python3 -i lab01.py
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 8
(cases remaining: 1)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) It is generally bad practice to release code with debugging print statements left in
1) Debugging is not a substitute for testing
2) It is generally good practice to release code with assertion statements left in
3) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
4) Testing is very important to ensure robust code
? 3
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.
```

---

### 4. **`add_in_range`函数**

函数要求：完成 `add_in_range` ，返回 `start` 和 `stop` （包括）之间的所有整数和

代码实现：

```python
def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    sum = 0
    for i in range(start, stop + 1):
        sum += i
    return sum

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-4.png?raw=True)

---

### 5. **`digit_pos_match`函数**

函数要求：Digit Position Match 是指数字的倒数第 `i` 位的数就是 `i`，例如， `980` 有倒数第 `0` 位是 `0` ， `98276` 有 倒数第 `2` 位是 `2` 。编写函数来确定一个数字 `n` 是否有倒数第 `k` 位的数字/位置匹配。

代码实现：

```python
def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    while n > 0:
        x = n % 10
        if x == k:
            return True
        else:
            n = n // 10
    return False
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-5.png?raw=True)

---

### 6. **`falling`函数**

函数要求：编写函数 `falling`，接受两个参数 `n` 和 `k` ， 返回 从 `n` 开始的倒数 `k` 个连续数字之积。当 `k` 为 `0` 时，函数返回`1`

代码实现：

```python
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    res = 1
    while k > 0:
        res *= n
        n -= 1
        k -= 1
    return res
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-6.png?raw=True)

---

### 7. **`sum_digits`函数**

函数要求：编写函数接受非负整数，返回其数位之和。（提示：使用整数除和取模可能会有用！）

代码实现：

```python
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0
    while y > 0:
        sum, y = sum + y % 10, y // 10
    return sum
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-7.png?raw=True)

---

### 8. **WWPD： What If?**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab01$ python3 ok --local -q if-statements -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.
```

---

### 9. **`k_occurrence`函数**

函数要求：完成函数 `k-occurrence` ，返回 数位 `k` 在 `num` 中出现的次数， `0` 被当作没有数位。 

代码实现：

```python
def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    if num == 0:
        return 0
    count = 0
    while num:
        if num % 10 == k:
            count += 1
        num = num // 10
    return count

```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-9.png?raw=True)

---

### 10. **`double_eights`函数**

函数要求：编写函数，接受一个数字并确定其是否包括两个相邻的 `8`

代码实现：

```python
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n > 0:
        temp = n % 100
        if temp == 88:
            return True
        n = n // 10
    return False
```

测试结果：![img](https://github.com/Victor-Tau/cs61a/blob/master/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A/figs/lab01/lab1-10.png?raw=True)

---




### 五 实验心得

代码较为简易，但实验内容较多。在服务器上使用conda创建环境python=3.10，运行正常。实验报告使用vscode安装markdown插件编写。



