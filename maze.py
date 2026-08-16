import time

from cell import Cell
from gui import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_columns: int,
        cell_size_x: float,
        cell_size_y: float,
        window: Window,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window
        self.__cells: list[list[Cell]] = []

        self.__create_cells()

    def __create_cells(self) -> None:
        # create cells
        for _ in range(self.__num_columns):
            cols = []
            for _ in range(self.__num_rows):
                cell = Cell(self.__win)
                cols.append(cell)
            self.__cells.append(cols)

        # draw cells
        for i in range(self.__num_columns):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j) -> None:
        cell_x1 = self.__x1 + (i * self.__cell_size_x)
        cell_y1 = self.__y1 + (j * self.__cell_size_y)

        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y2 = cell_y1 + self.__cell_size_y

        self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __animate(self) -> None:
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
