from typing import List
from pyamaze.bfs.pluggable import BFS, AbstractQueue
from pyamaze import Maze, COLOR, Agent
from collections import deque

#          list([1, 2, 3])   array
# (8b size=3)(8b item 1)(8b item 2)(8b item 3)
#  00000011   00000001   00000010   00000011

#  list.pop()
# (8b size=2)(8b item 1)(8b item 2)(8b item 3)
#  00000010   00000001

#  list.pop(0)
# (8b size=3)(8b item 1)(8b item 2)(8b item 3)
#  00000011   00000010   00000011   00000000
# ===>
# (8b size=2)(8b item 1)(8b item 2)(8b item 3)
#  00000010   00000001   00000010   00000011

# 8b  = 00000000
# 16b = 0000000000000000
# 32b = 00000000000000000000000000000000
# 64b = 0000000000000000000000000000000000000000000000000000000000000000

# bit  0/1
# byte = 8b
# word = 16b
# double word = 32b
#   quad word = 64b

# 0b000 = 0
# 0b001 = 1
# 0b010 = 2
# 0b011 = 3
# 0b100 = 4
# 0b101 = 5
# 0b110 = 6
# 0b111 = 7

# 0b0000 ... binary number, binární číslo                číslice: 0, 1
# 0o0000 ... octal number, osmičková soustava            číslice: 0, 1, 2, 3, 4, 5, 6, 7
# 0d0000 ... decimal number, desítkové číslo             číslice: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0x0000 ... heXacedimal number, šestnáctková soustava   číslice: 0123456789ABCDEF

# linked list, spojový seznam, seznam
# cell = (data, pointer to the next cell)
# cells chained together
# cell => cell => NULL

# doubly linked list, oboustranný spojový seznam
# "deque", Double-Ended QUEue
# cell = (data, previous pointer, next pointer)
#         (    ) => (    ) => NULL
# NULL <= (cell) <= (cell)

# array, pole
# "spojitý blok paměti"
#
# Data:  (capacity, current size, [ data | data | ... | | | ])


#          deque([ 1, 2, 3 ])
# appendleft ->            <- append
#    popleft <-            -> pop
#
# instance = deque()
# instance.append(item)
# instance.appendleft(item)
# item = instance.pop()
# item = instance.popleft()


class QueueDeque(AbstractQueue):
    def __init__(self, queue: deque):
        self.state = queue

    @classmethod
    def from_list(cls, list: List[str]):
        return cls(deque(list))

    def enqueue(self, item: str):
        # TODO
        pass

    def dequeue(self) -> str:
        # TODO
        pass


def test_queue_list():
    queue = QueueDeque.from_list([])
    deque(["1st"]) != ["1st"]

    assert list(queue.state) == []
    queue.enqueue("1st")
    assert list(queue.state) == ["1st"]
    queue.enqueue("2nd")
    assert list(queue.state) == ["1st", "2nd"]
    assert queue.dequeue() == "1st"
    assert queue.dequeue() == "2nd"


def maze_demo():
    m = Maze(12, 10)
    m.CreateMaze(loopPercent=10, theme=COLOR.light)

    search_path, fwd_path = BFS(QueueDeque, m)

    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    c = Agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape="square", filled=True, goal=(m.rows, m.cols))
    m.tracePath({b: fwd_path, c: search_path}, delay=100)
    m.run()

if __name__ == "__main__":
    maze_test()
