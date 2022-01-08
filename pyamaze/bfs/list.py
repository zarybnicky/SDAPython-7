from pyamaze import Maze, Agent, COLOR, TextLabel


def BFS(maze, start=None):
    if start is None:
        start = (maze.rows, maze.cols)
    frontier = [start]
    explored = [start]
    bfs_path = {}
    agent_path = []

    while frontier:
        current_cell = frontier.pop(0)
        agent_path.append(current_cell)
        if current_cell == maze._goal:
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

            if next_cell in explored:
                continue
            frontier.append(next_cell)
            explored.append(next_cell)
            bfs_path[next_cell] = current_cell

    fwd_path = {}
    cell = maze._goal
    while cell != start:
        fwd_path[bfs_path[cell]] = cell
        cell = bfs_path[cell]
    return fwd_path


if __name__ == "__main__":
    m = Maze(5, 7)
    m.CreateMaze(loopPercent=40)
    search_path, path = BFS(m)

    a = Agent(m, footprints=True, filled=True)
    m.tracePath({a: path})
    m.tracePath({b: search_path})
    l = TextLabel(m, "Length of Shortest Path", len(path) + 1)

    m.run()
