from timeit import timeit
from pyamaze import Maze, Agent, COLOR, TextLabel
from ..bfs.list import BFS
from ..dfs.list import DFS

m = Maze(20, 30)
# m.CreateMaze(loopPercent=100)
m.CreateMaze(1, 30, loopPercent=100)
# m.CreateMaze()
# m.CreateMaze(1,30)
searchPath, dfsPath, fwdDFSPath = DFS(m)
bSearch, bfsPath, fwdBFSPath = BFS(m)

TextLabel(m, "DFS Path Length", len(fwdDFSPath) + 1)
TextLabel(m, "BFS Path Length", len(fwdBFSPath) + 1)
TextLabel(m, "DFS Search Length", len(searchPath) + 1)
TextLabel(m, "BFS Search Length", len(bSearch) + 1)

a = Agent(m, footprints=True, color=COLOR.cyan, filled=True)
b = Agent(m, footprints=True, color=COLOR.yellow)
m.tracePath({a: fwdBFSPath}, delay=100)
m.tracePath({b: fwdDFSPath}, delay=100)


t1 = timeit(stmt="DFS(m)", number=1000, globals=globals())
t2 = timeit(stmt="BFS(m)", number=1000, globals=globals())

TextLabel(m, "DFS Time", t1)
TextLabel(m, "BFS Time", t2)


m.run()
