from tkinter import FIRST
from .color import COLOR


class Agent:
    """
    The agents can be placed on the maze.
    They can represent the virtual object just to indcate the cell selected in Maze.
    Or they can be the physical agents (like robots)
    They can have two shapes (square or arrow)
    """

    def __init__(
        self,
        parent_maze,
        x=None,
        y=None,
        shape="square",
        goal=None,
        filled=False,
        footprints=False,
        color: COLOR = COLOR.blue,
    ):
        """
        parentmaze-->  The maze on which agent is placed.
        x,y-->  Position of the agent i.e. cell inside which agent will be placed
                Default value is the lower right corner of the Maze
        shape-->    square or arrow (as string)
        goal-->     Default value is the goal of the Maze
        filled-->   For square shape, filled=False is a smaller square
                    While filled =True is a biiger square filled in complete Cell
                    This option doesn't matter for arrow shape.
        footprints-->   When the aganet will move to some other cell, its footprints
                        on the previous cell can be placed by making this True
        color-->    Color of the agent.

        _orient-->  You don't need to pass this
                    It is used with arrow shape agent to shows it turning
        position--> You don't need to pass this
                    This is the cell (x,y)
        _head-->    You don't need to pass this
                    It is actually the agent.
        _body-->    You don't need to pass this
                    Tracks the body of the agent (the previous positions of it)
        """
        self.parent_maze = parent_maze
        self.color = color
        self.filled = filled
        self.shape = shape
        self._orient = 0
        self._head = None
        self._body = []
        self.footprints = footprints
        self.goal = goal if goal else self.parent_maze._goal
        self.parent_maze.agents.append(self)
        self._position = (x if x else parent_maze.rows, y if y else parent_maze.cols)
        self.coordinates = self.calculate_coords()
        self.draw_agent()

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def position(self):
        return self._position

    def calculate_coords(self):
        w = self.parent_maze.cell_width
        x = self.x * w - w + self.parent_maze.label_width
        y = self.y * w - w + self.parent_maze.label_width
        if self.shape == "square" and self.filled:
            return (y, x, y + w, x + w)
        elif self.shape == "square":
            return (y + w / 2.5, x + w / 2.5, y + w / 2.5 + w / 4, x + w / 2.5 + w / 4)
        else:
            return (y + w / 2, x + 3 * w / 9, y + w / 2, x + 3 * w / 9 + w / 4)

    @position.setter
    def position(self, newpos):
        self._position = newpos
        self.coordinates = self.calculate_coords()
        self.draw_agent()

    def draw_agent(self):
        if self._head is not None and not self.footprints:
            self.parent_maze.canvas.delete(self._head)

        if self._head is not None and self.footprints:
            fill = self.color.value[1]
            self.parent_maze.canvas.itemconfig(self._head, fill=fill)
            self.parent_maze.canvas.tag_raise(self._head)
            try:
                self.parent_maze.canvas.tag_lower(self._head, "ov")
            except:
                pass
            if self.shape == "square" and self.filled:
                lll = self.parent_maze.canvas.coords(self._head)
                oldcell = (
                    round(((lll[1] - 26) / self.parent_maze.cell_width) + 1),
                    round(((lll[0] - 26) / self.parent_maze.cell_width) + 1),
                )
                self.parent_maze.redraw_cell(oldcell)
            self._body.append(self._head)

        if self.shape == "square":
            self._head = self.draw_square_head()
        else:
            self._head = self.draw_arrow_head()
            o = self._orient % 4
            if o == 1:
                self._RCW()
                self._orient -= 1
            elif o == 3:
                self._RCCW()
                self._orient += 1
            elif o == 2:
                self._RCCW()
                self._RCCW()
                self._orient += 2

    def draw_arrow_head(self):
        w = self.parent_maze.cell_width
        head = self.parent_maze.canvas.create_line(
            *self.coordinates,
            fill=self.color.value[0],
            arrow=FIRST,
            arrowshape=(3 / 10 * w, 4 / 10 * w, 4 / 10 * w)
        )
        try:
            self.parent_maze.canvas.tag_lower(head, "ov")
        except:
            pass
        return head

    def draw_square_head(self):
        fill = self.color.value[0]
        head = self.parent_maze.canvas.create_rectangle(*self.coordinates, fill=fill, outline="")
        try:
            self.parent_maze.canvas.tag_lower(head, "ov")
        except:
            pass
        self.parent_maze.redraw_cell(self.position)
        return head

    def _RCCW(self):
        """
        To Rotate the agent in Counter Clock Wise direction
        """

        w = self.parent_maze.cell_width
        x = (self.x - .5) * w + self.parent_maze.label_width
        y = (self.y - .5) * w + self.parent_maze.label_width
        self.coordinates = (
            self.coordinates[1] - x + y, x + y - self.coordinates[0],
            self.coordinates[3] - x + y, x + y - self.coordinates[2]
        )
        self.parent_maze.canvas.coords(self._head, *self.coordinates)
        self._orient = (self._orient - 1) % 4

    def _RCW(self):
        """Rotate the agent in Clock Wise direction"""

        w = self.parent_maze.cell_width
        x = (self.x - .5) * w + self.parent_maze.label_width
        y = (self.y - .5) * w + self.parent_maze.label_width
        self.coordinates = (
            x + y - self.coordinates[1], x - y + self.coordinates[0],
            x + y - self.coordinates[3], x - y + self.coordinates[2]
        )
        self.parent_maze.canvas.coords(self._head, *self.coordinates)
        self._orient = (self._orient + 1) % 4

    def move_right(self, event):
        if self.parent_maze.maze_map[self.position]["E"]:
            self.position = (self.x, self.y + 1)

    def move_left(self, event):
        if self.parent_maze.maze_map[self.position]["W"]:
            self.position = (self.x, self.y - 1)

    def move_up(self, event):
        if self.parent_maze.maze_map[self.position]["N"]:
            self.position = (self.x - 1, self.y)

    def move_down(self, event):
        if self.parent_maze.maze_map[self.position]["S"]:
            self.position = (self.x + 1, self.y)

    def kill(self):
        for item in self._body:
            self.parent_maze.canvas.delete(item)
        self.parent_maze.canvas.delete(self._head)
