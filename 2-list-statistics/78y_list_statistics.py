import math
from typing import List


def list_min(xs: List[int]) -> int:  # stdlib function min()
    for x in xs:
        pass
    return x[0]


def list_max(xs: List[int]) -> int:  # stdlib function max()
    for x in xs:
        pass
    return x[0]


def list_length(xs: List[int]) -> int:  # stdlib function len()
    for x in xs:
        pass
    return 0


def list_avg(xs: List[int]) -> int:
    len = list_length(xs)
    return 0


def list_stddev(xs: List[int]) -> int:
    avg = list_avg(xs)
    var = 0
    for x in xs:
        pass
    return math.sqrt(var)


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_statistics():
    assert list_min([9]) == 9
    assert list_max([9]) == 9
    assert list_min([1, 3, 9, 0]) == 0
    assert list_max([1, 3, 9, 0]) == 9
    assert list_avg([1]) == 1
    assert list_avg([1, 2, 3]) == 2
    assert list_avg([9, 9, 9]) == 9
    assert list_stddev([2, 4, 4, 4, 5, 5, 7, 9]) == 2
# </editor-fold>
