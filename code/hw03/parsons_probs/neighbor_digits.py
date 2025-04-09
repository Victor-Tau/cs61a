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
    s = str(num)
    count = 0
    for i in range(len(s)):
        if (i > 0 and s[i] == s[i-1]) or (i < len(s)-1 and s[i] == s[i+1]):
            count += 1
    return count
