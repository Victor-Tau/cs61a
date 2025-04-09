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
    a = {}
    def helper(start, k):
        if (start, k) in a:
            return a[(start, k)]
        if k == 0:
            return 1 if start == 0 else 0
        left = helper(start - 1, k - 1)
        right = helper(start + 1, k - 1)
        a[(start, k)] = left + right
        return a[(start, k)]
    return helper(start, k)
