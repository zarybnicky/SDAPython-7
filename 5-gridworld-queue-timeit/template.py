from typing import List
from pyamaze import Maze, COLOR
from pyamaze.bfs.pluggable import BFS, AbstractQueue
from collections import deque
from timeit import timeit


def BFSSet(Queue, maze, start=None):
    if start is None:
        start = (maze.rows, maze.cols)
    frontier = Queue.from_list([start])
    explored = set(start)
    bfs_path = {}
    agent_path = []

    while frontier:
        current_cell = frontier.dequeue()
        agent_path.append(current_cell)
        if current_cell == maze._goal:
            break

        # Finding neighbors
        for d in "ESNW":
            if not maze.maze_map[current_cell][d]:
                continue
            if d == "E":
                next_cell = (current_cell[0], current_cell[1] + 1)
            elif d == "W":
                next_cell = (current_cell[0], current_cell[1] - 1)
            elif d == "S":
                next_cell = (current_cell[0] + 1, current_cell[1])
            elif d == "N":
                next_cell = (current_cell[0] - 1, current_cell[1])
            if next_cell in explored:
                continue

            frontier.enqueue(next_cell)
            explored.add(next_cell)
            bfs_path[next_cell] = current_cell

    fwd_path = {}
    cell = maze._goal
    while cell != (maze.rows, maze.cols):
        fwd_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return agent_path, fwd_path


class QueueList(AbstractQueue):
    def __init__(self, list: List[str]):
        self.state = list

    @classmethod
    def from_list(cls, list: List[str]):
        return cls(list)

    def enqueue(self, item: str):
        self.state.append(item)

    def dequeue(self) -> str:
        return self.state.pop(0)


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


maze = Maze(30, 30)
maze.CreateMaze(loopPercent=10, theme=COLOR.light)
print("Maze was generated")
print(timeit(lambda: BFS(QueueList, maze), number=100))
print(timeit(lambda: BFS(QueueDeque, maze), number=100))
print(timeit(lambda: BFSSet(QueueList, maze), number=100))
print(timeit(lambda: BFSSet(QueueDeque, maze), number=100))
