from pyamaze import Maze, Agent, COLOR
from .deque import BFS

def main():
    m = Maze(12, 10)
    m.CreateMaze(loopPercent=10, theme=COLOR.light)
    search_path, fwd_path = BFS(m)
    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    c = Agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape="square", filled=True, goal=(m.rows, m.cols))
    m.tracePath({b: fwd_path, c: search_path}, delay=100)

    m.run()

if __name__ == "__main__":
    main()
