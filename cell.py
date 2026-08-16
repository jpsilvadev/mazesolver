from __future__ import annotations

from gui import Line, Point, Window


class Cell:
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = window

    def draw(self, x1, y1, x2, y2) -> None:
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        fill_color = "gray" if undo else "red"
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2

        to_center_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_center_y = (to_cell.__y1 + to_cell.__y2) / 2

        line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))
        self.__win.draw_line(line, fill_color=fill_color)
