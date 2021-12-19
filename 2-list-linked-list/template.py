
class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return "LinkedListNode(%s, %s)" % (self.data, self.next)

# LinkedList
# - None                                      = seznam o délce 0
# - LinkedListNode(data=1, next=None)         = seznam o délce 1
# - LinkedListNode(data=1, next=another_list) = seznam o délce 1 + délka seznamu another_list

# [] : list
# None : linked list

# [1] : list
# LinkedListNode(data=1, next=None) : linked list
#                             ||
#                         empty list

# [1, 2] : list
# LinkedListNode(data=1, next=LinkedListNode(data=2, next=None))
#                                ||                       ||
#                            nested list              empty list


# <editor-fold defaultstate="collapsed" desc="Recursive versions">
def print_linked_list_recursive(linked_list: LinkedListNode):
    if isinstance(linked_list, LinkedListNode):
        print(linked_list.data)
        print_linked_list_recursive(linked_list.next)


def length_of_linked_list_recursive(linkedList: LinkedListNode) -> int:
    if linkedList is None:
        return 0
    elif isinstance(linkedList, LinkedListNode):
        return 1 + length_of_linked_list_recursive(linkedList.next)
# </editor-fold>


def print_linked_list(linked_list: LinkedListNode):
    while linked_list is not None:
        print(linked_list.data)
        linked_list = linked_list.next


def length_of_linked_list(linked_list: LinkedListNode) -> int:
    length = 0
    while isinstance(linked_list, LinkedListNode):
        length += 1
        linked_list = linked_list.next
    return length


def create_list(n: int) -> LinkedListNode:
    return None


# <editor-fold defaultstate="collapsed" desc="Tests">
def test_length():
    assert length_of_linked_list(create_list(0)) == 0
    assert length_of_linked_list(create_list(1)) == 1
    assert length_of_linked_list(create_list(5)) == 5
# </editor-fold>
