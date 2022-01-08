from abc import ABC, abstractmethod, abstractclassmethod


class AbstractQueue(ABC):
    @abstractclassmethod
    def from_list(cls, start):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass


# Q = [(12, 10)]
# pop from Q, searching neighbors of (12, 10)
# neighbors are (12, 9), (11, 10)
# push them to Q one-by-one

# Q = [(10, 8), (10, 9)]


def BFS(Queue, maze, start=None):
    if start is None:
        start = (maze.rows, maze.cols)
    frontier = Queue.from_list([start])
    explored = [start]
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
            explored.append(next_cell)
            bfs_path[next_cell] = current_cell

    fwd_path = {}
    cell = maze._goal
    while cell != (maze.rows, maze.cols):
        fwd_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return agent_path, fwd_path
