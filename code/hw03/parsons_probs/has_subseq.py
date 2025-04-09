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
    n_str = str(n)
    seq_str = str(seq)
    seq_index = 0
    for char in n_str:
        if seq_index < len(seq_str) and char == seq_str[seq_index]:
            seq_index += 1
    return seq_index == len(seq_str)
