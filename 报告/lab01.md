## ![img](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/logo.png)      计算机与人工智能学院《人工智能程序设计》实验报告📝

| 专业                 | 学号         | 姓名         |
| :------------------- | ------------ | ------------ |
| 数据科学与大数据技术 | 2302320122   | 胡文韬       |
| **课程名称**         | **实验名称** | **完成日期** |
| 人工智能程序设计A        | 实验1        | 2025.3.20    |



[TOC]

### 一 实验目标

1. **掌握基本运算和操作符**：熟练掌握 Python 中与除法相关的操作符（除、整数除、取模）的使用，理解它们之间的区别，并能运用取模操作符进行整除判断，如判断一个数是否为偶数。
2. **理解和运用函数**：理解函数的定义、参数、返回值等概念，学会将重复的代码抽象成函数以避免代码冗余。掌握函数的调用表达式的语法和计算规则，明确`return`和`print`的区别，能够正确使用`return`语句返回函数的计算结果，并合理运用`print`函数进行输出展示。
3. **掌握控制语句**：熟练掌握 Python 中的布尔运算符（`and`、`or`、`not`），理解其运算规则、优先级以及短路特性；掌握`if`语句和`while`循环的语法和使用方法，能够根据不同的条件和需求编写正确的控制逻辑。
4. **学会处理错误信息**：熟悉常见的 Python 错误类型（如`SyntaxError`、`IndentationError`、`TypeError`、`ZeroDivisionError`等），能够根据错误信息准确判断代码中存在的问题，并学会利用搜索引擎等工具进行错误调试。

### 二 实验要求



- 个人独立完成，积极动手编程；
- 鼓励与同学交流，但不能抄袭源码；
- 能完成实验说明文档的各个步骤并撰写此实验报告；
- 能演示实验过程并阐述功能的主要代码模块。
- 实验报告请突出自己的**想法**、**做法**、**心得体会**；

### 三 实验环境

我所使用的实验环境：

- 软件：Vscode
- 环境：python=3.10

### 四 实验内容

#### 1. 函数定义

- **`lambda_curry3`函数**：将一个三参数函数`FUNC`转换为柯里化版本。柯里化是把多参数函数转化为单参数函数链的过程，该函数接收一个三参数函数，返回一个经过柯里化处理的新函数。
- **`filter_cond`函数**：此函数接收一个双参数的谓词函数`Condition`，返回一个单参数函数。该单参数函数接收参数`L`（一个列表），返回列表`L`中满足`Condition`条件的元素组成的新列表，其中`Condition`的第一个参数为列表`L`，第二个参数为列表中的元素。
- **`function_equivalence`函数**：接受两个单参数函数`f`和`g`，返回一个布尔值。用于判断对于任意输入`x`，`f(x)`是否等于`g(x)`。
- **`alternate_cycle`函数**：接收四个函数`f1`、`f2`、`f3`、`f4`，返回一个高阶函数。这个高阶函数接受一个整数参数`n`，并再次返回一个函数，该最终返回的函数接受一个参数`x`，并根据`n`的值交替地将`f1`、`f2`、`f3`、`f4`应用到`x`上。

#### 2. 函数功能实现

- `lambda_curry3`函数
  - **实现步骤**：利用 lambda 表达式创建一个三层嵌套结构。最外层 lambda 接收第一个参数`x`，中间层 lambda 接收第二个参数`y`，最内层 lambda 接收第三个参数`z`，在最内层 lambda 中调用原始的三参数函数`func`，并传入`x`、`y`和`z`。
  - **实现方法**：借助 Python 中 lambda 表达式简洁的语法，通过函数嵌套实现柯里化。代码如下：

```python
def lambda_curry3(func):
    return lambda x: lambda y: lambda z: func(x, y, z)
```

- **测试说明**：通过从`operator`模块导入合适的三参数函数（如`pow`，表示幂运算）进行测试。例如，先对`pow`函数进行柯里化，得到`curried_pow`，再使用`curried_pow(2)(3)`得到一个新函数`pow_2_3`，最后调用`pow_2_3(4)`，预期结果为`pow(2, 3, 4)`的计算结果。对其他类似的三参数函数进行类似测试，验证柯里化的正确性。
- `filter_cond`函数
  - **实现步骤**：定义一个内部函数`filter_list`，在`filter_list`函数内部，使用`for`循环遍历列表`L`。在每次循环中，调用传入的条件函数`condition`，判断当前元素是否满足条件，若满足则将其添加到结果列表中。最后返回结果列表。
  - **实现方法**：运用闭包的特性，将条件函数`condition`保存在内部函数`filter_list`的作用域中。代码如下：

```python
def filter_cond(condition):
    def filter_list(L):
        result = []
        for element in L:
            if condition(L, element):
                result.append(element)
        return result
    return filter_list
```

- **测试说明**：定义不同的条件函数进行测试。如定义`filter_even`用于筛选列表中的偶数，通过`filter_even([1, 2, 3, 4, 5])`等测试用例，验证筛选结果是否正确。再定义`filter_greater_than_3`条件函数用于筛选列表中大于 3 的元素，通过`filter_greater_than_3([1, 2, 3, 4, 5])`等测试用例，检验筛选功能是否准确。
- `function_equivalence`函数
  - **实现步骤**：定义一个内部函数`check_equivalence`，在`check_equivalence`函数内部，使用一个循环（可以设定一个合理的测试范围，如从 - 10 到 10），对每个测试值`x`，分别调用`f(x)`和`g(x)`，比较它们的结果是否相等。如果在整个测试范围内都相等，则返回`True`，否则返回`False`。
  - **实现方法**：通过遍历测试值并比较函数输出的方式来判断函数等价性。代码如下：

```python
def function_equivalence(f, g):
    def check_equivalence():
        for x in range(-10, 11):
            if f(x) != g(x):
                return False
        return True
    return check_equivalence()
```

- **测试说明**：定义`add_one`和`subtract_minus_one`等函数（`add_one = lambda x: x + 1`，`subtract_minus_one = lambda x: x - (-1)`），通过`function_equivalence(add_one, subtract_minus_one)`等测试用例，验证函数是否能正确判断两个函数的等价性。
- `alternate_cycle`函数
  - **实现步骤**：定义一个外层函数`outer`，接收参数`n`。在`outer`函数内部，再定义一个内层函数`inner`，接收参数`x`。在`inner`函数中，使用`for`循环`n`次，根据循环次数`i`对 4 取模的结果，依次应用`f1`、`f2`、`f3`、`f4`到`x`上。最后返回`inner`函数。
  - **实现方法**：通过多层函数嵌套和循环控制，实现函数的交替循环应用。代码如下：

```python
def alternate_cycle(f1, f2, f3, f4):
    def outer(n):
        def inner(x):
            for i in range(n):
                if i % 4 == 0:
                    x = f1(x)
                elif i % 4 == 1:
                    x = f2(x)
                elif i % 4 == 2:
                    x = f3(x)
                else:
                    x = f4(x)
            return x
        return inner
    return outer
```

- **测试说明**：定义`add1`、`times2`、`subtract3`、`divide4`等函数（`add1 = lambda x: x + 1`，`times2 = lambda x: x * 2`，`subtract3 = lambda x: x - 3`，`divide4 = lambda x: x / 4`），通过`alternate_cycle(add1, times2, subtract3, divide4)(0)(5)`、`alternate_cycle(add1, times2, subtract3, divide4)(2)(1)`等测试用例，验证函数在不同循环次数下对输入值的处理是否符合预期。

#### 3. 函数语法检查

- **`lambda_curry3_syntax_check`函数**：此函数运用`inspect`和`ast`模块，检查`lambda_curry3`函数的源代码。通过解析源代码的抽象语法树，确认函数主体仅包含一个表达式和一个返回语句，以此保证函数定义的语法结构符合要求，防止因语法错误导致函数功能异常。代码示例（假设`inspect`和`ast`模块已正确导入）：

```python
def lambda_curry3_syntax_check():
    import inspect, ast
    source = inspect.getsource(lambda_curry3)
    tree = ast.parse(source)
    body = tree.body[0].body
    assert len(body) == 1 and isinstance(body[0], ast.Return), "函数主体应仅包含一个表达式和一个返回语句"
```

#### 4. 测试用例验证

针对每个函数，精心设计了丰富多样的测试用例，涵盖了各种可能的输入情况，包括正常输入、边界值输入和特殊情况输入。通过运行这些测试用例，全面检查函数的输出是否与预期结果相符，从而验证函数的正确性和稳定性。在测试过程中，详细记录每个测试用例的输入、预期输出和实际输出，对于出现的错误结果，仔细分析原因并进行调试，确保函数在各种情况下都能可靠运行。同时，不断优化测试用例，提高测试的覆盖率和有效性，以保障函数的质量满足实际应用的需求。

### 五 实验心得

本次实验中，我在理解 lambda 表达式与闭包时遭遇难题，致使函数编写出错。编写测试用例时，又因覆盖不全面，未能察觉特殊输入的问题。此外，部分函数性能欠佳。通过重新学习概念、全面分析输入以及优化算法，我成功解决这些问题，也提升了编程能力 。