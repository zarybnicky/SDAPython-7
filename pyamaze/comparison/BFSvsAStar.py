from pyamaze.bfs.list import BFS
from pyamaze.astar.pqueue import aStar
from pyamaze import Maze, Agent, COLOR, TextLabel
from timeit import timeit

###########################
## Comparison One by One ##

# First Run this for BFS:
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# bSearch,fwdPath=BFS(m)


# l=TextLabel(m,'BFS Path Length',len(fwdPath)+1)
# l=TextLabel(m,'BFS Search Length',len(bSearch)+1)


# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:bSearch},delay=50)
# m.tracePath({c:fwdPath},delay=100)

# m.run()


# Then run this for A-Star
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# aSearch,fwdPath=aStar(m)

# l=TextLabel(m,'A-Star Path Length',len(fwdPath)+1)
# l=TextLabel(m,'A-Star Search Length',len(aSearch)+1)

# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:aSearch},delay=50)
# m.tracePath({c:fwdPath},delay=100)


# m.run()


###########################
## Combined Comparison ##

myMaze = Maze(50, 70)
myMaze.CreateMaze(loopPercent=100)
# myMaze.CreateMaze()
searchPath, fwdPath = aStar(myMaze)
bSearch, fwdBFSPath = BFS(myMaze)

l = TextLabel(myMaze, "A-Star Path Length", len(fwdPath) + 1)
l = TextLabel(myMaze, "BFS Path Length", len(fwdBFSPath) + 1)
l = TextLabel(myMaze, "A-Star Search Length", len(searchPath) + 1)
l = TextLabel(myMaze, "BFS Search Length", len(bSearch) + 1)

a = Agent(myMaze, footprints=True, color=COLOR.cyan, filled=True)
b = Agent(myMaze, footprints=True, color=COLOR.yellow)
myMaze.tracePath({a: fwdBFSPath}, delay=50)
myMaze.tracePath({b: fwdPath}, delay=50)

t1 = timeit(stmt="aStar(myMaze)", number=10, globals=globals())
t2 = timeit(stmt="BFS(myMaze)", number=10, globals=globals())

TextLabel(myMaze, "A-Star Time", t1)
TextLabel(myMaze, "BFS Time", t2)


myMaze.run()
