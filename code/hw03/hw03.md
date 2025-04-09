

# 作业2 递归、树递归

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

下载 [hw03.zip](./hw03.zip)，你会发现这次作业问题的开始文件 hw03.py，还包括一个自动评分工具 Ok

可以阅读 [1.7 节](http://composingprograms.com/pages/17-recursive-functions.html)

### 需提交的材料

- .py 源程序文件
- .md 实验记录文档



## 问题

### Parsons 问题

#### 问题1：Neighbor Digits

实现函数 `neighbor_digits` , 该函数接受一个正整数 `num` ，和一个可选参数 `prev_digits` ，输出 `num` 中左边或者右边相同数位（digit）的数量。

> neighbor_digits.py源代码文件在 parsons_probs 文件夹中，在终端通过 `cd` 命令进入该文件夹，并输入命令进行验证：
>
> ```
> python3 -m doctest neighbor_digits.py
> ```

```python
def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
```

#### 问题2：Has Subsequence

实现函数 `has_subseq` ，该函数接受一个数字 `n` 和 一个 “序列” 的数位 `seq` ，返回 `n` 是否包含 `seq` 子序列，并**不要求连续**。

例如，`141` 包含序列 `11` ，因为序列的第一个数位 `1` 是 `141` 的第一个数位，序列中的第二个数位 `1` 也在 `141` 后面出现了。

> has_subseq.py源代码文件在 parsons_probs 文件夹中，在终端通过 `cd` 命令进入该文件夹，并输入命令进行验证：
>
> ```
> python3 -m doctest has_subseq.py
> ```

```python
def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
```

###  编程问题

#### 问题3：Num eights

编写递归函数 `num_eights` ，该函数接受一个正整数 `pos`，返回 `pos` 中数位 8出现的次数。

**注意**：使用递归；如果你使用任何的赋值语句测试将失败。（但你可以尽管使用函数定义）

```python
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q num_eights
```

#### 问题4：  Ping-pong

乒乓序列从 1 开始向上计数，并且总是向上或者向下计数。在索引 `k` 处，如果 `k` 是 8 的倍数或者包含数位 8 则切换方向。 下面列出了乒乓序列的前 30 个元素，在第 8、16、18、24 和 28 个元素处使用中括号标记了方向切换。

| Index          | 1    | 2    | 3    | 4    | 5    | 6    | 7    | [8]  | 9    | 10   | 11   | 12   | 13   | 14   | 15   | [16] | 17   | [18] | 19   | 20   | 21   | 22   | 23   |
| :------------- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PingPong Value | 1    | 2    | 3    | 4    | 5    | 6    | 7    | [8]  | 7    | 6    | 5    | 4    | 3    | 2    | 1    | [0]  | 1    | [2]  | 1    | 0    | -1   | -2   | -3   |

| Index (cont.)  | [24] | 25   | 26   | 27   | [28] | 29   | 30   |
| :------------- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PingPong Value | [-4] | -3   | -2   | -1   | [0]  | -1   | -2   |

实现函数 `pingpong`，该函数返回乒乓序列的第 n 个元素，并且不使用任何赋值语句。

你可以使用上一个问题中定义的 `num_eights` 函数

**注意：** 使用递归；如果使用任何赋值语句，则测试将失败。（但你可以尽管使用函数定义）

> **提示：**如果遇到困难，请首先尝试使用赋值语句和 `while` 语句实现 `pingpong`。然后将其转换为递归，编写一个帮助函数（helper function），该函数对于在 while 循环体改变了值得每个变量都对应有一个参数。
>
> **提示：**我们需要跟踪一些信息。其中一个细节是前进的方向（增加或者减少）。基于上面的提示，考虑如何在对帮助函数的调用过程中跟踪方向。

```python
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 测试你的代码：

```
python3 ok --local -q pingpong
```

#### 问题5： Count coins

给定一个正整数 `change`，一组硬币如果它们的和是 `change` 就可以用于换钱找零。这里使用标准的美分：1， 5， 10， 25。例如，`15` 可以换成：

- 15 个 1 美分硬币
- 10 个 1 美分，1个 5 美分硬币
- 5 个 1 美分， 2 个 5 美分硬币
- 5 个 1 美分， 1 个 10 美分硬币
- 3 个 5 美分硬币
- 1 个 5 美分， 1 个 10 美分硬币

因此，有 6 种方法可以对 `15`  换钱找零。编写一个**递归**函数，该函数接受一个正整数 `change` ，并返回使用硬币进行换钱找零的方法数量。

你可以直接使用下面供你使用的函数：

- `get_larger_coin` 将根据输入返回下一个较大的硬币面额，即 `get_larger_coin(5)`是 `10`。
- `get_smaller_coin` 将根据输入返回下一个较小的硬币面额，即 `get_smaller_coin(5)` 是 `1`。

解决问题的途径有两种。一种是使用 `get_larger_coin`，一种是使用 `get_smaller_coin`。

**注意**：使用递归；如果使用循环，测试将失败。

> **提示：**参考划分计数 `count_partitions` 的[实现](http://composingprograms.com/pages/17-recursive-functions.html#example-partitions) ，作为一个例子，将一个值分成多个更小值的和，可能的划分方法计数。如果需要在递归调用中跟踪多个值，请考虑编写一个帮助函数。

```python
def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(change, get_larger_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)

    # Alternate solution: using get_smaller_coin
    def constrained_count_small(change, largest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if largest_coin == None:
            return 0
        without_coin = constrained_count_small(change, get_smaller_coin(largest_coin))
        with_coin = constrained_count_small(change - largest_coin, largest_coin)
        return without_coin + with_coin
    return constrained_count_small(change, 25)
```

使用 Ok 测试你的代码：

```
python3 ok --local -q count_coins
```



#### 可选问题

课后作业中也会包括之前的考试问题，你可以看看。这些问题不做要求，尽管尝试挑战一下。

1. Fall 2017 MT1 Q4a: [Digital](./61a-fa17-mt1.pdf) （第5页第4题）
2. Summer 2018 MT1 Q5a: [Won't You Be My Neighbor?](./61a-su18-mt.pdf) （第5页第5题）

3. Fall 2019 Final Q6b: [Palindromes](./61a-fa19-final.pdf) （第6页第6题）

