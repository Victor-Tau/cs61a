

# 作业1 变量&函数，表达式

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

下载 [lab01.zip](./lab01.zip)（或者见作业附件），你会发现这次实验问题的开始文件，还包括一个自动评分工具 Ok

### 需提交的材料

- .py 源程序文件
- .md 实验记录文档

## 话题

这个小节内容供你翻新一下实验所涉及的内容，你可以直接跳到 [问题](#问题)，卡住的时候再回来看。

### 除，整数除，取模

> Division, Floor Div, and Modulo

对比一下Python3中与除法相关的操作符：

![image-20220316144357745](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220316144357745.png)

注意再某些情况下Python会输出 `ZeroDivisionError` ,这小结后面会复习 [错误信息](#错误信息) 。

操作符 `%` 一个有用的技术是用来检查一个数 `x` 能被另一个数 `y` 整除：

```
x % y == 0
```

例如，为了检查 `x` 是否为偶数：

```
x % 2 == 0
```

### 函数

如果我们想一遍又一遍地执行某个语句序列，可以把它们抽象成一个函数，来避免重复代码。

例如，假设我们想知道数字 1 到 3 ，乘以 3 然后再加上2 的结果，一种做法是：

```
>>> 1 * 3 + 2
5
>>> 2 * 3 + 2
8
>>> 3 * 3 + 2
11
```

如果我们想对一组更多的数字这样做，那将是大量的重复代码！让我们编写一个函数接收任意给定的输入数字来执行这个操作。

```python
def foo(x):
    return x * 3 + 2
```

这个名为 `foo` 的函数接受一个**参数**，并将**返回**将该参数乘以 3 并加 2 的结果。

现在每当我们希望执行此操作时，都可以**调用**此函数：

```
>>> foo(1)
5
>>> foo(2)
8
>>> foo(1000)
3002
```

将函数应用于某些参数是通过**调用表达式**完成的。

#### 调用表达式

调用表达式应用一个函数，该函数可能接受也可能不接受参数。调用表达式的计算结果为函数的返回值。

函数调用的语法：

```
  add   (    2   ,    3   )
   |         |        |
operator  operand  operand
```

每个调用表达式都需要一对小括号来分隔操作符与操作数，操作数之间用逗号分隔。

计算函数调用：

1. 计算操作符，然后计算操作数（从左到右）。
2. 将操作符应用于操作数（操作数的值）。

如果操作数是嵌套的调用表达式，则首先将这两个步骤应用于该内部操作数，以便计算外部操作数。

#### `return` 和 `print` 

大多数自定义的函数都有 `return` 语句。该语句会将一些计算结果反馈给函数的调用者并退出该自定义函数。例如，下面的函数 `square` 接收一个数字 `x` 并返回其平方。

```
def square(x):
    """
    >>> square(4)
    16
    """
    return x * x
```

当 Python 执行 `return` 语句时，该函数会立即终止。如果Python在没有执行 `return` 语句的情况下到达函数体的末尾，它将自动返回 `None` 。

而 `print` 函数则是用于在终端中显示值。`return`  容易和 `print` 弄混淆，因为在Python解释器中调用函数将打印出函数的返回值。

但是，与 `return` 语句不同，当 Python 计算 `print` 表达式时，函数*不会*立即终止。

```python
def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('61A is awesome!')

>>> what_prints()
Hello World!
'Exiting this function.'
```

> 也要注意， `print` 显示的文本没有引号， 但是 `return` 保留了引号

### 控制

#### 布尔运算符

Python 支持三个布尔运算符 : `and` `or` `not`

```python
>>> a = 4
>>> a < 2 and a > 0
False
>>> a < 2 or a > 0
True
>>> not (a > 0)
False
```

- 只有两个运算对象都计算为 `True` ， `and` 才计算为 `True`，只要有一个计算为 `False` ，则 `and` 计算为 `False`
- 只要有一个运算对象计算为 `True` ， `or` 就计算为 `True` ， 只有两个都计算为 `False` ， `or`  才计算为 `False`
- 如果运算对象计算为 `True` ， `not` 就计算为 `False` ， 如果 运算对象计算为 `False` ， `not` 就计算为 `True`  

你认为下面的表达式会计算为？在Python解释器中试试

```python
True and not False or not True and False
```

很难阅读复杂的表达式（如上面的表达式），并理解程序的行为方式。使用小括号可以使代码更易于理解。Python通过以下方式解释该表达式：

```
(True and (not False)) or ((not True) and False)
```

这是因为布尔运算符（和算术运算符类似）也有运算顺序：

- `not`具有最高优先级
- `and`
- `or`具有最低优先级

**真值和假值**：`and` 和 `or` 不仅仅只支持布尔值（`True`， `False`）的计算，事实上， `0` `None`  ` `（空字符串）和 `[]`（空列表）等Python 值被视为假值, 所有其他值都被视为真值。

##### 短路

如果在Python中敲入下面表达式会发生什么：

```
1 / 0
```

自己试一下！你会看到 `ZeroDivisionError` 。但是如果是这个表达式呢：

```python
True or 1 / 0
```

计算为 `True` ，因为Python 的 `and` 和 `or` 运算符有 短路 （short-circuit）特性，即它们不必计算每一个运算对象。

| 运算符 | 检查           | 从左到右计算直到 | 例子                             |
| ------ | -------------- | ---------------- | -------------------------------- |
| AND    | 所有的值为真   | 第一个为假的值   | `False and 1 / 0` 计算为 `False` |
| OR     | 至少一个值为真 | 第一个为真的值   | `True or 1 / 0` 计算为 `True`    |

当运算符遇到能够得出表达式结果的运算对象时就会发生短路。例如，`and` 一旦遇到第一个假值就会短路，因为它知道并非所有值都为真。如果 `and` 和 `or` 不发生*短路*，则返回最后一个值。

#### if 语句

你可以查看 [1.5.4节](http://composingprograms.com/pages/15-control.html#conditional-statements) 的 `if` 语句的语法。

> 提示：有时候代码是这样：
>
> ```
> if x > 3:
>     return True
> else:
>     return False
> ```
>
> 这也可以写成紧凑的形式： `return x > 3` 

#### while 循环

你可以查看 [1.5.5节](http://composingprograms.com/pages/15-control.html#iteration) 的 `while` 循环的语法。

### 错误信息 <a name ="错误信息"></a>

目前为止，你可能见了一些错误信息，它们可能看起来很吓人，但错误消息对调试代码非常有帮助。以下是一些常见的错误类型：

| 错误类型          | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| SyntaxError       | 包含不正确的语法（例如，在 `if` 语句后缺少冒号或忘记关闭括号/引号） |
| IndentationError  | 包含不正确的缩进（例如，函数体的缩进不一致）                 |
| TypeError         | 尝试对不兼容类型（例如，尝试将函数和数字相加）或错误参数个数的函数调用执行操作 |
| ZeroDivisionError | 尝试除以零                                                   |

使用这些错误消息的描述，你应该能够更好地了解代码出了什么问题。**如果遇到错误消息，请尝试在寻求帮助之前确定问题。**你通常可以在Bing中搜索不熟悉的错误消息，查看其他人是否犯了类似的错误，来帮你进行调试。

例如：

```
>>> square(3, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: square() takes 1 positional argument but 2 were given
```

注意：

- 错误信息的最后一行告诉我们错误的类型。在上面的示例中，我们有一个 `TypeError` 。

- 错误信息告诉我们我们做错了什么 ---- 我们给了 `square` 2个参数，而它只能接受1个参数。通常，最后一行是最有帮助的。

- 错误消息的倒数第二行告诉我们错误发生在哪一行。这有助于我们跟踪错误。在上面的示例中，`TypeError` 发生在 `line 1` 。

  

## 问题 <a name ="问题"></a>

### What Would Python Display？（WWPD）

#### 问题1：WWPD: Control

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```
> python3 ok -q --local control -u
> ```

```python
>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
______

>>> xk(10, 6)
______

>>> xk(4, 6)
______

>>> xk(0, 0)
______
```

```python
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
______

>>> how_big(12)
______

>>> how_big(1)
______

>>> how_big(-1)
______
```

```python
>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)
______
```

> 提示：确保你的 `while` 循环条件最终会计算为 `false` 值，否则循环就停不下来了！ 敲入 `Ctrl + C` 会将解释器中的无限循环停下来。

```python
>>> positive = 28
>>> while positive:
...    print("positive?")
...    positive -= 3
______
```

```
>>> positive = -9
>>> negative = -12
>>> while negative:
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
______
```

#### 问题2: WWPD: Veritasiness

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```
> python3 ok -q --local short-circuit -u
> ```

```python
>>> True and 13
______

>>> False or 0
______

>>> not 10
______

>>> not None
______
```



```python
>>> True and 1 / 0 and False
______
>>> True or 1 / 0 or False
______
>>> True and 0
______
>>> False or 1
______
>>> 1 and 3 and 6 and 10 and 15
______
>>> -1 and 1 > 0
______
>>> 0 or False or 2 or 1 / 0
______
```

```python
>>> not 0
______
>>> (1 + 1) and 1
______
>>> 1/0 or True
______
>>> (True or False) and False
______
```

#### 问题3: 调试小测验

下面是不同调试技术的一个快速小测验，对本课程的学习非常有用，回答问题你可以参考 [调试文章](https://cs61a.org/articles/debugging/)

使用 Ok 测试你的理解：

```
python3 ok --local -q debugging-quiz -u
```

### Parsons 问题

#### 问题4：Add in Range

完成 `add_in_range` ，返回 `start` 和 `stop` （包括）之间的所有整数和

> add_in_range.py源代码文件在 parsons_probs 文件夹中，进入该文件夹目录，终端输入命令进行验证：
>
> ```
> python3 -m doctest add_in_range.py
> ```

```python
def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    "*** YOUR CODE HERE ***"
```

#### 问题5： Digit Position Match

Digit Position Match 是指数字的倒数第 `i` 位的数就是 `i`，例如， `980` 有倒数第 `0` 位是 `0` ， `98276` 有 倒数第 `2` 位是 `2` 。编写函数来确定一个数字 `n` 是否有倒数第 `k` 位的数字/位置匹配。

> digit_pos_match.py源代码文件在 parsons_probs 文件夹中，进入该文件夹目录，终端输入命令进行验证：
>
> ```
> python3 -m doctest digit_pos_match.py
> ```

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
    "*** YOUR CODE HERE ***"
```

###  编程问题

#### 问题6：Falling Factorial

编写函数 `falling`，接受两个参数 `n` 和 `k` ， 返回 从 `n` 开始的倒数 `k` 个连续数字之积。当 `k` 为 `0` 时，函数返回`1`

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
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q falling
```

#### 问题7： Sum Digits

编写函数接受非负整数，返回其数位之和。（提示：使用整数除和取模可能会有用！）

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
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q sum_digits
```

#### 额外的实践

> 问题选做，不过，这些问题对后面的任务是很好的训练，尝试这些问题对于巩固课程的概念知识很有帮助
> 

#### 问题8：WWPD： What If?

> 使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题：
>
> ```
> python3 ok -q --local if-statements -u
> ```
>  
>提示： `print` （和 `return` 不同）不会退出函数

```python
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
______
```

```python
>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)
______

>>> bake(1, "mashed potatoes")
______
```

#### 问题9： K-Occurrence

完成函数 `k-occurrence` ，返回 数位 `k` 在 `num` 中出现的次数， `0` 被当作没有数位。

> k_occurrence.py源代码文件在 parsons_probs 文件夹中，进入该文件夹目录，终端输入命令进行验证：
>
> ```
> python3 -m doctest k_occurrence.py
> ```


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
    "*** YOUR CODE HERE ***"
```

#### 问题10：Double Eights

编写函数，接受一个数字并确定其是否包括两个相邻的 `8`

```
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
    "*** YOUR CODE HERE ***"
```

使用Ok测试你的代码

```
python3 ok --local -q double_eights
```





​	

