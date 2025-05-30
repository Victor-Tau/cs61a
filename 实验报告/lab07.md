## ![img](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/logo.png)      计算机与人工智能学院《人工智能程序设计》实验报告📝

| 专业                 | 学号         | 姓名         |
| :------------------- | ------------ | ------------ |
| 数据科学与大数据技术 | 2302320122   | 胡文韬       |
| **课程名称**         | **实验名称** | **完成日期** |
| 人工智能程序设计A        | lab07       | 2025.5.40    |



[TOC]

---



### 一 实验目标

1. **理解链表的思想**
2. **掌握面向对象编程的方法**
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

通过几个问题，掌握面向对象编程

### 1. **Squared Virahanka Fibonacci**

使用 Ok 测试你的知识，回答下面的“Python会显示什么”问题

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q wwpd-car -u --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Car > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
?  'Model S'
-- OK! --

>>> deneros_car.gas = 10
>>> deneros_car.drive()
?  'Tesla Model S goes vroom!'
-- OK! --

>>> deneros_car.drive()
? 'Cannot drive!'
-- OK! --

>>> deneros_car.fill_gas()
? 'Gas level: 20'
-- OK! --

>>> deneros_car.gas
? 20
-- OK! --

>>> Car.gas
? 30
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
? 2
-- OK! --

>>> Car.num_wheels
? 4
-- OK! --

>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

>>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Monster Batmobile goes vroom!'
-- OK! --

>>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

---------------------------------------------------------------------
OK! All cases for Car unlocked.
```

---

### 2. **账户**

假设我们想模拟一个银行账户，它可以处理诸如存款或根据当前资金赚取利息等交互。
在接下来的问题中，我们将基于 `Account` 类进行构建。
向 `Account` 类添加一个 `time_to_retire` 方法。
此方法接收一个 `amount` 参数，并返回持有人需要等待多少年才能使当前 `balance` 增长到至少 `amount`，假设银行在每年年底将 `balance` 乘以 `interest` 利率的金额加到总余额中。



代码实现：

```python
class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        years = 0
        current_balance = self.balance
        while current_balance < amount:
            current_balance *= (1 + self.interest)
            years += 1
        return years
```

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Account  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

---

### 3. **免费支票账户**

实现 `FreeChecking` 类，它与讲座中的 `Account` 类类似，不同之处在于它在两次取款后会收取取款费。
如果取款不成功，它仍然计入剩余的免费取款次数，但不会为此取款收取费用。

代码实现：

```python
class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    def __init__(self, holder):
        super().__init__(holder)
        self.withdrawals_made = 0

    def withdraw(self, amount):
        # Count this as an attempted withdrawal (even if it fails)
        self.withdrawals_made += 1

        if self.withdrawals_made <= self.free_withdrawals:
            fee = 0
        else:
            fee = self.withdraw_fee

        total = amount + fee
        if total > self.balance:
            return 'Insufficient funds'
        self.balance -= total
        return self.balance
```

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q FreeChecking  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.
```

---

## Magic: The Lambda-ing 纸牌游戏

在本实验的下一部分，我们将实现一个纸牌游戏！
这个游戏的灵感来源于同名游戏 [Magic: The Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering)。

实现游戏后，您可以通过键入以下命令来启动它：
```
python3 cardgame.py
```
在玩游戏时，您可以使用 `Ctrl-C` 或 `Ctrl-D` 退出游戏并返回命令行。

这个游戏使用了几个不同的文件。
*   本实验中所有问题的代码都可以在 `classes.py` 中找到。
*   游戏的一些实用功能可以在 `cardgame.py` 中找到，但您不需要打开或阅读此文件。此文件实际上不直接修改任何实例——相反，它调用不同类的方法，维持严格的抽象屏障。
*   如果您想稍后修改游戏以添加自己的自定义卡牌和牌组，可以查看 `cards.py` 以查看所有标准卡牌和默认牌组；在这里，您可以添加更多卡牌并更改您和对手使用的牌组。如果您熟悉原版游戏，您可能会注意到这些卡牌并非以平衡性为目标创建的，因此请随意修改属性并根据需要添加或删除卡牌。

### 游戏规则

这个游戏有点复杂，虽然远不及它的同名游戏。规则如下：

有两个玩家。
每个玩家都有一手牌和一个牌组，在每轮开始时，每个玩家从他们的牌组中随机抽取一张牌。如果玩家在尝试抽牌时牌组为空，他们将自动输掉游戏。
卡牌有名称、攻击值和防御值。
每轮，每个玩家从自己的手中选择一张牌打出。
*力量*值更高的卡牌赢得该轮。
每张打出卡牌的力量值计算如下：
```
(玩家卡牌的攻击力) - (对手卡牌的防御力) / 2
```
例如，假设玩家1打出一张攻击力为2000、防御力为1000的卡牌，玩家2打出一张攻击力为1500、防御力为3000的卡牌。
他们的卡牌力量计算如下：
```
P1: 2000 - 3000/2 = 2000 - 1500 = 500
P2: 1500 - 1000/2 = 1500 - 500 = 1000
```
所以玩家2将赢得这一轮。

第一个赢得8轮的玩家赢得比赛！

然而，我们可以添加一些效果（在可选问题部分）使这个游戏更有趣。
卡牌可以是 AI、Tutor、TA 或 Instructor 类型，每种类型在被打出时都有不同的*效果*。
所有效果在该轮计算力量之前应用：

*   AI 卡牌会使对手卡牌的攻击力降低其防御力的数值，然后使对手卡牌的防御力翻倍。
*   Tutor 卡牌会导致对手弃掉并重新抽取其手中的前3张牌。
*   TA 卡牌会交换对手卡牌的攻击力和防御力。
*   Instructor 卡牌会将对手卡牌的攻击力和防御力加到玩家牌组中所有卡牌上，然后移除对手牌组中所有与其攻击力*或*防御力相同的卡牌！

请随时回顾这些规则，让我们开始制作游戏吧！

### 问题4：制作卡牌

要玩纸牌游戏，我们需要有卡牌，所以让我们来制作一些！
我们首先要实现 `Card` 类的基础功能。

首先，在 `classes.py` 中实现 `Card` 类的构造函数。此构造函数接收三个参数：
*   一个字符串作为卡牌的 `name`
*   一个整数作为卡牌的 `attack` 值
*   一个整数作为卡牌的 `defense` 值

每个 `Card` 实例都应使用名为 `name`、`attack` 和 `defense` 的实例属性来跟踪这些值。

您还应该在 `Card` 中实现 `power` 方法，该方法接收另一张卡牌作为输入，并计算当前卡牌的力量。如果您想回顾力量是如何计算的，请参阅[游戏规则](#游戏规则)。

代码实现：

```python
class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        >>> staff_member = Card('staff', 400, 300)
        >>> staff_member.name
        'staff'
        >>> staff_member.attack
        400
        >>> staff_member.defense
        300
        >>> other_staff = Card('other', 300, 500)
        >>> other_staff.attack
        300
        >>> other_staff.defense
        500
        """
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, opponent_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense)/2
        >>> staff_member = Card('staff', 400, 300)
        >>> other_staff = Card('other', 300, 500)
        >>> staff_member.power(other_staff)
        150.0
        >>> other_staff.power(staff_member)
        150.0
        >>> third_card = Card('third', 200, 400)
        >>> staff_member.power(third_card)
        200.0
        >>> third_card.power(staff_member)
        50.0
        """
        return self.attack - (opponent_card.defense / 2)
```

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Card.__init__  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Card.power  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

---

### 问题5：创建玩家

现在我们有了卡牌，我们可以制作牌组了，但我们仍然需要玩家来实际使用它们。我们现在将填写 `Player` 类的实现。

一个 `Player` 实例有三个实例属性：
*   `name` 是玩家的姓名。当您玩游戏时，可以输入您的姓名，它将被转换为字符串传递给构造函数。
*   `deck` 是 `Deck` 类的一个实例。您可以使用其 `.draw()` 方法从中抽牌。
*   `hand` 是一个 `Card` 实例的列表。每个玩家开始时应从其 `deck` 中抽取5张牌放入手中。手牌中的每张牌都可以在游戏中通过其在列表中的索引来选择。当玩家从牌组中抽取一张新牌时，它会被添加到此列表的末尾。

完成 `Player` 构造函数的实现，以便 `self.hand` 设置为一个包含从玩家 `deck` 中抽取的5张牌的列表。

接下来，在 `Player` 类中实现 `draw` 和 `play` 方法。`draw` 方法从牌组中抽一张牌并将其添加到玩家的手中。`play` 方法从玩家手中移除并返回给定索引处的牌。

> 在实现 `Player.__init__` 和 `Player.draw` 时调用 `deck.draw()`。
> 不用担心这个函数是如何工作的——把它全部交给抽象层！

代码实现：

```python
class Player:
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> len(test_deck.cards)
        1
        >>> len(test_player.hand)
        5
        """
        self.deck = deck
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]

    def draw(self):
        """Draw a card from the player's deck and add it to their hand.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> test_player.draw()
        >>> len(test_deck.cards)
        0
        >>> len(test_player.hand)
        6
        """
        assert not self.deck.is_empty(), 'Deck is empty!'
        self.hand.append(self.deck.draw())

    def play(self, card_index):
        """Remove and return a card from the player's hand at the given index.
        >>> from cards import *
        >>> test_player = Player(standard_deck, 'tester')
        >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
        >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
        >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
        >>> test_player.play(0) is ta1
        True
        >>> test_player.play(2) is tutor2
        True
        >>> len(test_player.hand)
        2
        """
        return self.hand.pop(card_index)
```

测试结果：

```python
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Player.__init__  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Player.draw  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
(cs61a) huwentao@a-SYS-740GP-TNRT:/data1/tao/cs61a/code/lab07-OOP/lab07$ python3 ok -q Player.play  --local
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
```

---

### 五 实验心得

实验内容较多，较之前有一定难度提升，但编程中暂未遇到困难。在服务器上使用conda创建环境python=3.10，运行正常。实验报告使用vscode安装markdown插件编写。



