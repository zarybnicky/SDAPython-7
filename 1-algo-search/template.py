from typing import List


def search(n: int, xs: List[int]) -> List[int]:
    return []


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_search():
    assert search(1, [1, 2, 3]) == 0
    assert search(1, [0, 1, 2, 3]) == 1
    assert search(0, [1, 2, 3]) is None
    assert search(5, []) is None
    assert search(1, [0, 1, 0, 1]) == 1
# </editor-fold>
