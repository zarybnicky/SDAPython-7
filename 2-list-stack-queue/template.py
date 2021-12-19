from typing import List

# STACK:
# push()
#     stack ABCDE  <- push()  F
# new stack ABCDEF

# pop()
#     stack ABCDE  -> pop()
# new stack ABCD            E

def new_stack():
    return []

def stack_push(stack: List[int], item: int):
    stack.append(item)

def stack_pop(stack: List[int]) -> int:
    return stack.pop()

# ((()()))


from queue import Queue

def new_queue():
    return Queue()

def queue_put(queue: Queue, item: int):
    queue.put(item)

def queue_get(queue: Queue) -> int:
    return queue.get()

