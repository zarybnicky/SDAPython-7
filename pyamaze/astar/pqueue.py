from pyamaze import Maze, Agent, COLOR, TextLabel
from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    search_path = [start]
    while not open.empty():
        current_cell = open.get()[2]
        search_path.append(current_cell)
        if current_cell == m._goal:
            break
        for d in "ESNW":
            if not m.maze_map[current_cell][d]:
                continue

            if d == "E":
                next_cell = (current_cell[0], current_cell[1] + 1)
            elif d == "W":
                next_cell = (current_cell[0], current_cell[1] - 1)
            elif d == "N":
                next_cell = (current_cell[0] - 1, current_cell[1])
            elif d == "S":
                next_cell = (current_cell[0] + 1, current_cell[1])

            temp_g_score = g_score[current_cell] + 1
            temp_f_score = temp_g_score + h(next_cell, m._goal)
            if temp_f_score < f_score[next_cell]:
                aPath[next_cell] = current_cell
                g_score[next_cell] = temp_g_score
                f_score[next_cell] = temp_g_score + h(next_cell, m._goal)
                open.put((f_score[next_cell], h(next_cell, m._goal), next_cell))

    fwd_path = {}
    cell = m._goal
    while cell != start:
        fwd_path[aPath[cell]] = cell
        cell = aPath[cell]
    return search_path, fwd_path


if __name__ == "__main__":
    m = Maze(4, 4)
    m.CreateMaze(loadMaze="aStardemo.csv")

    search_path, fwd_path = aStar(m)
    a = Agent(m, footprints=True, color=COLOR.blue, filled=True)
    c = Agent(m, footprints=True, color=COLOR.red)

    m.tracePath({a: search_path}, delay=300)
    m.tracePath({c: fwd_path}, delay=300)

    l = TextLabel(m, "A Star Path Length", len(fwd_path) + 1)
    l = TextLabel(m, "A Star Search Length", len(search_path))
    m.run()
