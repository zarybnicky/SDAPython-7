from tkinter import StringVar, Label, RIDGE, LEFT, NW


class TextLabel:
    """
    This class is to create Text Label to show different results on the window.
    """

    def __init__(self, parent_maze, title, value):
        """
        parentmaze-->   The maze on which Label will be displayed.
        title-->        The title of the value to be displayed
        value-->        The value to be displayed
        """
        self.title = title
        self._value = value
        self.parent_maze = parent_maze
        # self.parent_maze._labels.append(self)
        self._var = None
        self.drawLabel()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self._var.set(f"{self.title} : {v}")

    def drawLabel(self):
        self._var = StringVar()
        self.lab = Label(
            self.parent_maze.canvas,
            textvariable=self._var,
            bg="white",
            fg="black",
            font=("Helvetica bold", 12),
            relief=RIDGE,
        )
        self._var.set(f"{self.title} : {self.value}")
        self.lab.pack(expand=True, side=LEFT, anchor=NW)
