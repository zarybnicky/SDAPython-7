from pyamaze import Maze, Agent, COLOR


def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfs_path = {}
    while frontier:
        current_cell = frontier.pop()
        if current_cell == m._goal:
            break
        poss = 0
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
            poss += 1
            explored.append(next_cell)
            frontier.append(next_cell)
            dfs_path[next_cell] = current_cell
        if poss > 1:
            m.mark_cells.append(current_cell)

    fwd_path = {}
    cell = m._goal
    while cell != start:
        fwd_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]
    return dfs_path, fwd_path


def main():
    m = Maze(10, 10)  # Change to any size
    m.CreateMaze(2, 4)  # (2,4) is Goal Cell, Change that to any other valid cell

    # (5,1) is Start Cell, Change that to any other valid cell
    dfs_path, fwd_path = DFS(m, (5, 1))

    a = Agent(m, 5, 1, goal=(2, 4), footprints=True, shape="square", color=COLOR.green)
    b = Agent(m, 2, 4, goal=(5, 1), footprints=True, filled=True)
    c = Agent(m, 5, 1, footprints=True, color=COLOR.yellow)
    m.tracePath({b: dfs_path})
    m.tracePath({c: fwd_path})
    m.run()

if __name__ == "__main__":
    main()
