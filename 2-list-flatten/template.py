from typing import List

# [1] => [1]
# [[1]] => [1]
# [1, [1]] => [1, 1]


def is_list(xs) -> bool:
    return isinstance(xs, list)


def flatten(xs: List) -> List[int]:
    result = []
    for item in xs:
        result.append(item)
    return result


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_search_flat():
    assert flatten([1, 1, 1]) == [1, 1, 1]
    assert flatten([[1], [1], [1]]) == [1, 1, 1]
    assert flatten([1, [1, 1], 1]) == [1, 1, 1, 1]
# </editor-fold>
