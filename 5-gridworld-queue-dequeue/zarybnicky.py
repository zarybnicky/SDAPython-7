from typing import List
from pyamaze.bfs.pluggable import BFS, AbstractQueue
from pyamaze import Maze, COLOR, Agent
from collections import deque


class QueueDeque(AbstractQueue):
    def __init__(self, queue: deque):
        self.state = queue

    @classmethod
    def from_list(cls, list: List[str]):
        return cls(deque(list))

    def enqueue(self, item: str):
        self.state.append(item)

    def dequeue(self) -> str:
        return self.state.popleft()


def test_queue_list():
    queue = QueueDeque.from_list([])
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
    maze_demo()
