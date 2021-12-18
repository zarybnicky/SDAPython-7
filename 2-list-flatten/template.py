from typing import List


def flatten(xs: List) -> List[int]:
    return []


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_search_flat():
    assert flatten([1, 1, 1]) == [1, 1, 1]
    assert flatten([[1], [1], [1]]) == [1, 1, 1]
    assert flatten([1, [1, 1], 1]) == [1, 1, 1, 1]
# </editor-fold>
