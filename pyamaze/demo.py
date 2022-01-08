from pyamaze import Maze, COLOR, Agent, TextLabel

def main():
    m = Maze()
    m.CreateMaze(loopPercent=0)

    # a=agent(m,5,4)
    # print(a.x)
    # print(a.y)
    # print(a.position)

    a = Agent(m, footprints=True, filled=True)
    b = Agent(m, 5, 5, footprints=True, color=COLOR.red)
    c = Agent(m, 4, 1, footprints=True, color=COLOR.green, shape='arrow')

    m.enableArrowKey(a)

    path2 = [(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
    path3 = 'WWNNES'

    TextLabel(m,'Total Cells',m.rows*m.cols)

    m.tracePath({a:m.path,b:path2,c:path3}, delay=200, kill=True)
    m.run()


if __name__ == "__main__":
    main()
