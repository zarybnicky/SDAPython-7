from enum import Enum


class COLOR(Enum):
    """
    This class is created to use the Tkinter colors easily.
    Each COLOR object has two color values.
    The first two objects (dark and light) are for theme and the two color
    values represent the Canvas color and the Maze Line color respectively.
    The rest of the colors are for Agents.
    The first value is the color of the Agent and the second is the color of
    its footprint
    """

    dark = ("gray11", "white")
    light = ("white", "black")
    black = ("black", "dim gray")
    red = ("red3", "tomato")
    cyan = ("cyan4", "cyan4")
    green = ("green4", "pale green")
    blue = ("DeepSkyBlue4", "DeepSkyBlue2")
    yellow = ("yellow2", "yellow2")
