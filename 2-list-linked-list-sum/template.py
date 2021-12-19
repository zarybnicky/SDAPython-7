
class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "LinkedListNode(%s, %s)" % (self.data, self.next)


def sum_linked_list(n: LinkedListNode) -> int:
    return None


# <editor-fold defaultstate="collapsed" desc="Tests">
def create_list(n: int) -> LinkedListNode:
    list = None
    while n > 0:
        n -= 1
        list = LinkedListNode(1, list)
    return list


def test_length():
    assert sum_linked_list(create_list(0)) == 0
    assert sum_linked_list(create_list(5)) == 5
    assert sum_linked_list(create_list(10)) == 10
# </editor-fold>
