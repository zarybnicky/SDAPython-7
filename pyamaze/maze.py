import random
import datetime
import csv
from tkinter import Tk, Canvas, YES, BOTH

from .color import COLOR
from .agent import Agent
from .bfs.deque import BFS


class Maze:
    """
    This is the main class to create maze.
    """

    def __init__(self, rows=10, cols=10):
        """
        rows--> No. of rows of the maze
        cols--> No. of columns of the maze
        Need to pass just the two arguments. The rest will be assigned automatically
        maze_map--> Will be set to a Dicationary. Keys will be cells and
                    values will be another dictionary with keys=['E','W','N','S'] for
                    East West North South and values will be 0 or 1. 0 means that
                    direction(EWNS) is blocked. 1 means that direction is open.
        grid--> A list of all cells
        path--> Shortest path from start(bottom right) to goal(by default top left)
                It will be a dictionary
        win,cell_width,canvas -->    win and )canvas are for Tkinter window and canvas
                                        cell_width is cell width calculated automatically
        agents-->  A list of aganets on the maze
        markedCells-->  Will be used to mark some particular cell during
                        path trace by the agent.
        _
        """
        self.win: Tk
        self.canvas: Canvas

        self.size = (rows, cols)
        self.rows = rows
        self.cols = cols
        self.maze_map = {}
        self.grid = []
        self.path = {}
        self.cell_width = 50
        self.agents = []
        self.mark_cells = []
        self.trace_path_list = []
        self.label_width = 26  # Space from the top for Labels

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, n):
        self._grid = []
        y = 0
        for n in range(self.cols):
            x = 1
            y = 1 + y
            for m in range(self.rows):
                self._grid.append((x, y))
                self.maze_map[x, y] = {"E": 0, "W": 0, "N": 0, "S": 0}
                x = x + 1

    def _Open_East(self, x, y):
        """
        To remove the East Wall of the cell
        """
        self.maze_map[x, y]["E"] = 1
        if y + 1 <= self.cols:
            self.maze_map[x, y + 1]["W"] = 1

    def _Open_West(self, x, y):
        self.maze_map[x, y]["W"] = 1
        if y - 1 > 0:
            self.maze_map[x, y - 1]["E"] = 1

    def _Open_North(self, x, y):
        self.maze_map[x, y]["N"] = 1
        if x - 1 > 0:
            self.maze_map[x - 1, y]["S"] = 1

    def _Open_South(self, x, y):
        self.maze_map[x, y]["S"] = 1
        if x + 1 <= self.rows:
            self.maze_map[x + 1, y]["N"] = 1

    def CreateMaze(
        self,
        x=1,
        y=1,
        pattern=None,
        loopPercent=0,
        theme: COLOR = COLOR.dark,
    ):
        """
        One very important function to create a Random Maze
        pattern-->  It can be 'v' for vertical or 'h' for horizontal
                    Just the visual look of the maze will be more vertical/horizontal
                    passages will be there.
        loopPercent-->  0 means there will be just one path from start to goal (perfect maze)
                        Higher value means there will be multiple paths (loops)
                        Higher the value (max 100) more will be the loops
        theme--> Dark or Light
        """
        _stack = []
        _closed = []
        self.theme = theme
        self._goal = (x, y)

        def blockedNeighbours(cell):
            n = []
            for d in self.maze_map[cell].keys():
                if self.maze_map[cell][d] == 0:
                    if d == "E" and (cell[0], cell[1] + 1) in self.grid:
                        n.append((cell[0], cell[1] + 1))
                    elif d == "W" and (cell[0], cell[1] - 1) in self.grid:
                        n.append((cell[0], cell[1] - 1))
                    elif d == "N" and (cell[0] - 1, cell[1]) in self.grid:
                        n.append((cell[0] - 1, cell[1]))
                    elif d == "S" and (cell[0] + 1, cell[1]) in self.grid:
                        n.append((cell[0] + 1, cell[1]))
            return n

        def removeWallinBetween(cell1, cell2):
            """
            To remove wall in between two cells
            """
            if cell1[0] == cell2[0]:
                if cell1[1] == cell2[1] + 1:
                    self.maze_map[cell1]["W"] = 1
                    self.maze_map[cell2]["E"] = 1
                else:
                    self.maze_map[cell1]["E"] = 1
                    self.maze_map[cell2]["W"] = 1
            else:
                if cell1[0] == cell2[0] + 1:
                    self.maze_map[cell1]["N"] = 1
                    self.maze_map[cell2]["S"] = 1
                else:
                    self.maze_map[cell1]["S"] = 1
                    self.maze_map[cell2]["N"] = 1

        def isCyclic(cell1, cell2):
            """
            To avoid too much blank(clear) path.
            """
            ans = False
            if cell1[0] == cell2[0]:
                if cell1[1] > cell2[1]:
                    cell1, cell2 = cell2, cell1
                if self.maze_map[cell1]["S"] == 1 and self.maze_map[cell2]["S"] == 1:
                    if (cell1[0] + 1, cell1[1]) in self.grid and self.maze_map[
                        (cell1[0] + 1, cell1[1])
                    ]["E"] == 1:
                        ans = True
                if self.maze_map[cell1]["N"] == 1 and self.maze_map[cell2]["N"] == 1:
                    if (cell1[0] - 1, cell1[1]) in self.grid and self.maze_map[
                        (cell1[0] - 1, cell1[1])
                    ]["E"] == 1:
                        ans = True
            else:
                if cell1[0] > cell2[0]:
                    cell1, cell2 = cell2, cell1
                if self.maze_map[cell1]["E"] == 1 and self.maze_map[cell2]["E"] == 1:
                    if (cell1[0], cell1[1] + 1) in self.grid and self.maze_map[
                        (cell1[0], cell1[1] + 1)
                    ]["S"] == 1:
                        ans = True
                if self.maze_map[cell1]["W"] == 1 and self.maze_map[cell2]["W"] == 1:
                    if (cell1[0], cell1[1] - 1) in self.grid and self.maze_map[
                        (cell1[0], cell1[1] - 1)
                    ]["S"] == 1:
                        ans = True
            return ans

        _stack.append((x, y))
        _closed.append((x, y))
        biasLength = 2  # if pattern is 'v' or 'h'
        if pattern is not None and pattern.lower() == "h":
            biasLength = max(self.cols // 10, 2)
        if pattern is not None and pattern.lower() == "v":
            biasLength = max(self.rows // 10, 2)
        bias = 0

        while _stack:
            cell = []
            bias += 1
            if (x, y + 1) not in _closed and (x, y + 1) in self.grid:
                cell.append("E")
            if (x, y - 1) not in _closed and (x, y - 1) in self.grid:
                cell.append("W")
            if (x + 1, y) not in _closed and (x + 1, y) in self.grid:
                cell.append("S")
            if (x - 1, y) not in _closed and (x - 1, y) in self.grid:
                cell.append("N")
            if len(cell) > 0:
                if pattern is not None and pattern.lower() == "h" and bias <= biasLength:
                    if "E" in cell or "W" in cell:
                        if "S" in cell:
                            cell.remove("S")
                        if "N" in cell:
                            cell.remove("N")
                elif pattern is not None and pattern.lower() == "v" and bias <= biasLength:
                    if "N" in cell or "S" in cell:
                        if "E" in cell:
                            cell.remove("E")
                        if "W" in cell:
                            cell.remove("W")
                else:
                    bias = 0

                current_cell = random.choice(cell)

                if current_cell == "E":
                    self._Open_East(x, y)
                    self.path[x, y + 1] = x, y
                    y = y + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "W":
                    self._Open_West(x, y)
                    self.path[x, y - 1] = x, y
                    y = y - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "N":
                    self._Open_North(x, y)
                    self.path[(x - 1, y)] = x, y
                    x = x - 1
                    _closed.append((x, y))
                    _stack.append((x, y))

                elif current_cell == "S":
                    self._Open_South(x, y)
                    self.path[(x + 1, y)] = x, y
                    x = x + 1
                    _closed.append((x, y))
                    _stack.append((x, y))

            else:
                x, y = _stack.pop()

        ## Multiple Path Loops
        if loopPercent != 0:

            x, y = self.rows, self.cols
            pathCells = [(x, y)]
            while x != self.rows or y != self.cols:
                x, y = self.path[(x, y)]
                pathCells.append((x, y))
            notPathCells = [i for i in self.grid if i not in pathCells]
            random.shuffle(pathCells)
            random.shuffle(notPathCells)

            count1 = len(pathCells) / 3 * loopPercent / 100
            count2 = len(notPathCells) / 3 * loopPercent / 100

            # remove blocks from shortest path cells
            count = 0
            i = 0
            while count < count1:  # these many blocks to remove
                if blockedNeighbours(pathCells[i]):
                    cell = random.choice(blockedNeighbours(pathCells[i]))
                    if not isCyclic(cell, pathCells[i]):
                        removeWallinBetween(cell, pathCells[i])
                        count += 1
                    i += 1

                else:
                    i += 1
                if i == len(pathCells):
                    break
            # remove blocks from outside shortest path cells
            if notPathCells:
                count = 0
                i = 0
                while count < count2:  # these many blocks to remove
                    if len(blockedNeighbours(notPathCells[i])) > 0:
                        cell = random.choice(blockedNeighbours(notPathCells[i]))
                        if not isCyclic(cell, notPathCells[i]):
                            removeWallinBetween(cell, notPathCells[i])
                            count += 1
                        i += 1

                    else:
                        i += 1
                    if i == len(notPathCells):
                        break
            _, self.path = BFS(self, self.size)
        self._drawMaze(self.theme)
        Agent(self, *self._goal, shape="square", filled=True, color=COLOR.green)

    def _drawMaze(self, theme):
        """
        Creation of Tkinter window and maze lines
        """

        self.win = Tk()
        self.win.title("Maze World")

        scr_width = self.win.winfo_screenwidth()
        scr_height = self.win.winfo_screenheight()
        self.win.geometry(f"{scr_width}x{scr_height}+0+0")
        self.canvas = Canvas(width=scr_width, height=scr_height, bg=theme.value[0])
        # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)
        # Some calculations for calculating the width of the maze cell
        k = 3.25
        if self.rows >= 95 and self.cols >= 95:
            k = 0
        elif self.rows >= 80 and self.cols >= 80:
            k = 1
        elif self.rows >= 70 and self.cols >= 70:
            k = 1.5
        elif self.rows >= 50 and self.cols >= 50:
            k = 2
        elif self.rows >= 35 and self.cols >= 35:
            k = 2.5
        elif self.rows >= 22 and self.cols >= 22:
            k = 3
        self.cell_width = round(
            min(
                ((scr_height - self.rows - k * self.label_width) / self.rows),
                ((scr_width - self.cols - k * self.label_width) / self.cols),
                90,
            ),
            3,
        )

        # Creating Maze lines
        for cell in self.grid:
            self.redraw_cell(cell)

    def redraw_cell(self, cell):
        """
        To redraw a cell.
        With Full sized square agent, it can overlap with maze lines
        So the cell is redrawn so that cell lines are on top
        """
        if self.win is None or self.grid is None:
            return
        fill = self.theme.value[1]
        (x, y) = cell
        w = self.cell_width
        x = x * w - w + self.label_width
        y = y * w - w + self.label_width
        if not self.maze_map[cell]["E"]:
            self.canvas.create_line(y + w, x, y + w, x + w, width=2, fill=fill)
        if not self.maze_map[cell]["W"]:
            self.canvas.create_line(y, x, y, x + w, width=2, fill=fill)
        if not self.maze_map[cell]["N"]:
            self.canvas.create_line(y, x, y + w, x, width=2, fill=fill)
        if not self.maze_map[cell]["S"]:
            self.canvas.create_line(y, x + w, y + w, x + w, width=2, fill=fill)

    def enableArrowKey(self, a):
        """
        To control an agent a with Arrow Keys
        """
        self.win.bind("<Left>", a.move_left)
        self.win.bind("<Right>", a.move_right)
        self.win.bind("<Up>", a.move_up)
        self.win.bind("<Down>", a.move_down)

    def enableWASD(self, a):
        """
        To control an agent a with keys W,A,S,D
        """
        self.win.bind("<a>", a.move_left)
        self.win.bind("<d>", a.move_right)
        self.win.bind("<w>", a.move_up)
        self.win.bind("<s>", a.move_down)

    def _tracePathSingle(self, a, p, kill, showMarked, delay):
        """
        An interal method to help tracePath method for tracing a path by agent.
        """

        w = self.cell_width
        if a.position in self.mark_cells and showMarked:
            w = self.cell_width
            x = a.x * w - w + self.label_width
            y = a.y * w - w + self.label_width
            self.canvas.create_oval(
                y + w / 2.5 + w / 20,
                x + w / 2.5 + w / 20,
                y + w / 2.5 + w / 4 - w / 20,
                x + w / 2.5 + w / 4 - w / 20,
                fill="red",
                outline="red",
                tag="ov",
            )
            self.canvas.tag_raise("ov")

        if a.position == a.goal:
            del self.trace_path_list[0][0][a]
            if not self.trace_path_list[0][0]:
                del self.trace_path_list[0]
                if self.trace_path_list:
                    self.tracePath(
                        self.trace_path_list[0][0],
                        kill=self.trace_path_list[0][1],
                        delay=self.trace_path_list[0][2],
                    )
            if kill:
                self.win.after(300, a.kill)
            return

        # If path is provided as Dictionary
        if type(p) == dict:
            if not p:
                del self.trace_path_list[0][0][a]
                return
            if a.shape == "arrow":
                old = a.position
                new = p[a.position]
                o = a._orient

                if old != new:
                    if old[0] == new[0]:
                        if old[1] > new[1]:
                            mov = 3  #'W' #3
                        else:
                            mov = 1  #'E' #1
                    else:
                        if old[0] > new[0]:
                            mov = 0  #'N' #0

                        else:
                            mov = 2  #'S' #2
                    if mov - o == 2:
                        a._RCW()

                    if mov - o == -2:
                        a._RCW()
                    if mov - o == 1:
                        a._RCW()
                    if mov - o == -1:
                        a._RCCW()
                    if mov - o == 3:
                        a._RCCW()
                    if mov - o == -3:
                        a._RCW()
                    if mov == o:
                        a.position = p[a.position]
                else:
                    del p[a.position]
            else:
                a.position = p[a.position]

        # If path is provided as String
        if type(p) == str:
            if not p:
                del self.trace_path_list[0][0][a]
                if not self.trace_path_list[0][0]:
                    del self.trace_path_list[0]
                    if self.trace_path_list:
                        self.tracePath(
                            self.trace_path_list[0][0],
                            kill=self.trace_path_list[0][1],
                            delay=self.trace_path_list[0][2],
                        )
                if kill:
                    self.win.after(300, a.kill)
                return

            if a.shape == "arrow":
                old = a.position
                new = p[0]
                o = a._orient
                if new == "N":
                    mov = 0
                elif new == "E":
                    mov = 1
                elif new == "S":
                    mov = 2
                else:
                    mov = 3

                if mov - o == 2:
                    a._RCW()

                if mov - o == -2:
                    a._RCW()
                if mov - o == 1:
                    a._RCW()
                if mov - o == -1:
                    a._RCCW()
                if mov - o == 3:
                    a._RCCW()
                if mov - o == -3:
                    a._RCW()
            if a.shape == "square" or mov == o:
                move = p[0]
                if move == "E":
                    if a.y + 1 <= self.cols:
                        a.position = (a.x, a.y + 1)
                elif move == "W":
                    if a.y - 1 > 0:
                        a.position = (a.x, a.y - 1)
                elif move == "N":
                    if a.x - 1 > 0:
                        a.position = (a.x - 1, a.y)
                elif move == "S":
                    if a.x + 1 <= self.rows:
                        a.position = (a.x + 1, a.y)
                elif move == "C":
                    a._RCW()
                elif move == "A":
                    a._RCCW()
                p = p[1:]

        # If path is provided as List
        if type(p) == list:
            if not p:
                del self.trace_path_list[0][0][a]
                if not self.trace_path_list[0][0]:
                    del self.trace_path_list[0]
                    if self.trace_path_list:
                        self.tracePath(
                            self.trace_path_list[0][0],
                            kill=self.trace_path_list[0][1],
                            delay=self.trace_path_list[0][2],
                        )
                if kill:
                    self.win.after(300, a.kill)
                return

            if a.shape == "arrow":
                old = a.position
                new = p[0]
                o = a._orient

                if old != new:
                    if old[0] == new[0]:
                        if old[1] > new[1]:
                            mov = 3  #'W' #3
                        else:
                            mov = 1  #'E' #1
                    else:
                        if old[0] > new[0]:
                            mov = 0  #'N' #0

                        else:
                            mov = 2  #'S' #2
                    if mov - o == 2:
                        a._RCW()

                    elif mov - o == -2:
                        a._RCW()
                    elif mov - o == 1:
                        a._RCW()
                    elif mov - o == -1:
                        a._RCCW()
                    elif mov - o == 3:
                        a._RCCW()
                    elif mov - o == -3:
                        a._RCW()
                    elif mov == o:
                        a.position = p[0]
                        del p[0]
                else:
                    del p[0]
            else:
                a.position = p[0]
                del p[0]

        self.win.after(delay, self._tracePathSingle, a, p, kill, showMarked, delay)

    def tracePath(self, d, kill=False, delay=300, showMarked=False):
        """
        A method to trace path by agent
        You can provide more than one agent/path details
        """
        self.trace_path_list.append((d, kill, delay))
        if self.trace_path_list[0][0] == d:
            for a, p in d.items():
                if a.goal != a.position and p:
                    self._tracePathSingle(a, p, kill, showMarked, delay)

    def run(self):
        """
        Finally to run the Tkinter Main Loop
        """
        self.win.mainloop()

    @classmethod
    def load(cls, filename, size):
        maze = cls(*size)

        with open(filename, "r") as f:
            last = list(f.readlines())[-1]
            c = last.split(",")
            c[0] = int(c[0].lstrip('"('))
            c[1] = int(c[1].rstrip(')"'))
            maze.rows = c[0]
            maze.cols = c[1]
            maze.grid = []

        with open(filename, "r") as f:
            r = csv.reader(f)
            next(r)
            for i in r:
                c = i[0].split(",")
                c[0] = int(c[0].lstrip("("))
                c[1] = int(c[1].rstrip(")"))
                maze.maze_map[tuple(c)] = {
                    "E": int(i[1]),
                    "W": int(i[2]),
                    "N": int(i[3]),
                    "S": int(i[4]),
                }

        _, maze.path = BFS(size)


    def save(self, filename=None):
        if filename is None:
            dt_string = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
            filename = f"maze--{dt_string}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["  cell  ", "E", "W", "N", "S"])
            for k, v in self.maze_map.items():
                writer.writerow([k] + v.values())
