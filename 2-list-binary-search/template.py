import math
from typing import List

# 1. def binary_search(xs, x)
# 2.    midpoint = len(xs) // 2
# 3.    current_item = xs\[midpoint]
# 4.    if current_item > x: return binary_search(???)
# 5.    elif current_item < x: return binary_search(???)
# 6.    else: return midpoint
#
# xs = \[1, 2, 3, 4, 5, 8, 9]
# x = 8
#
# 1. midpoint_idx = 3, midpoint_item = 4
# 2. 8 > 4 => right sublist (start = 4, end = 6; xs = \[_, _, _, _, 5, 8, 9])
# 3. midpoint_idx = 5, midpoint_item = 8
# 4. 8 == 8 => return midpoint


def binary_search(xs: List[int], x: int, start: int, end: int) -> int:
    # [_, _, _, _, 5, 8, 9]
    #              |     |
    #           start   end
    if start <= end:
        midpoint_idx = start + (end - start) // 2
        midpoint_item = xs[midpoint_idx]
        if x > midpoint_item:
            return binary_search(xs, x, midpoint_idx + 1, end)
        elif x < midpoint_item:
            return binary_search(xs, x, start, midpoint_idx - 1)
        else:
            return midpoint_idx
    else:
        return None

# <editor-fold defaultstate="collapsed" desc="Tests">
def test_binary_search():
    xs = [1, 2, 3, 4, 5, 8, 9]
    assert binary_search(xs, 8, start=0, end=len(xs)) == 5
    xs = [1, 2, 3, 4, 5, 8, 9]
    assert binary_search(xs, 8, start=0, end=len(xs)) is None
# </editor-fold>
