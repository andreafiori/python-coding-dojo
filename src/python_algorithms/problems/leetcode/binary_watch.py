def read_binary_watch(self, num):
    """
    Read Binary Watch
    :type num: int
    :rtype: List[str]
    """
    return ['%d:%02d' % (h, m)
        for h in range(12) for m in range(60)
        if (bin(h) + bin(m)).count('1') == num]
