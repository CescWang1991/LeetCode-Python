# 比较x^y与y^x的大小
# 假定函数中x < y，则x^y / y^x = (x/y)^x * x^(y-x)

import unittest


def powComp(x, y):
    """
    :type x: int
    :type y: int
    :rtype: str
    """
    res = 1.0
    z = float(x) / float(y)
    m = x
    n = y - x
    while m > 0 and n > 0:
        res = res * z * x
        m -= 1
        n -= 1
    while m > 0:
        res = res * z
        # 由于z < 0，所以在res < 1.0时直接输出"<"
        m -= 1
        if res < 1.0:
            return "<"
    while n > 0:
        res = res * x
        n -= 1
        if res > 1.0:
            return ">"
    if res > 1.0:
        return ">"
    elif res < 1.0:
        return "<"
    else:
        return "="
