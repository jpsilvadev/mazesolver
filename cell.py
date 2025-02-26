from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        # check if no window was provided
        # allows unittests to run
        if self._window is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(left_line)

        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(right_line)

        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(top_line)

        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(bottom_line)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        # center of cells
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(x1, y1), Point(x2, y2))
        self._window.draw_line(line, fill_color)
