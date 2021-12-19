
class LinkedList:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def length_of_linked_list(lst: LinkedList) -> int:
    return 0


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_length():
    assert length_of_linked_list(None) == 0
    assert length_of_linked_list(LinkedList(1, None)) == 1
    assert length_of_linked_list(LinkedList(1, LinkedList(2, LinkedList(3, None)))) == 3
# </editor-fold>


# while list is not None:
#     print(list.data)
#     list = list.next