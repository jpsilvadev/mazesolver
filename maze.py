import random
import time

from cell import Cell
from config import ANIMATION_DELAY
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
        window: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window
        self.__cells: list[list[Cell]] = []

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_recursive(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self) -> None:
        for _ in range(self.__num_columns):
            cols = []
            for _ in range(self.__num_rows):
                cell = Cell(self.__win)
                cols.append(cell)
            self.__cells.append(cols)

        if self.__win is None:
            return

        # draw cells
        for i in range(self.__num_columns):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int) -> None:
        cell_x1 = self.__x1 + (i * self.__cell_size_x)
        cell_y1 = self.__y1 + (j * self.__cell_size_y)

        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y2 = cell_y1 + self.__cell_size_y

        self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # can't access with -1 indexing
        # because __draw_cell uses i and j directly in calculations
        # would shift cell to top left of maze
        last_col = self.__num_columns - 1
        last_row = self.__num_rows - 1
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_recursive(self, i: int, j: int):
        current = self.__cells[i][j]
        current.visited = True

        while True:
            # check adjacent cells
            to_visit = []

            # boundary checks
            # left check -> boundary: i > 0
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right check -> boundary: i < num_cols < 1
            if i < self.__num_columns - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up check -> boundary: j > 0
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down check -> boundary: j < num_rows - 1
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            else:
                new_direction = random.randrange(len(to_visit))
                next_i, next_j = to_visit[new_direction]
                neighbor = self.__cells[next_i][next_j]
                # break down walls based on random direction
                # left
                if next_i == i - 1:
                    current.has_left_wall = False
                    neighbor.has_right_wall = False
                # right
                if next_i == i + 1:
                    current.has_right_wall = False
                    neighbor.has_left_wall = False
                # up
                if next_j == j - 1:
                    current.has_top_wall = False
                    neighbor.has_bottom_wall = False
                # down
                if next_j == j + 1:
                    current.has_bottom_wall = False
                    neighbor.has_top_wall = False

                self.__break_walls_recursive(next_i, next_j)

    def __reset_cells_visited(self) -> None:
        # reset visited props so we can solve maze after generating paths
        for i in range(self.__num_columns):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def _solve_r(self, i: int, j: int) -> bool:
        self.__animate()
        current = self.__cells[i][j]
        current.visited = True

        last_col = self.__num_columns - 1
        last_row = self.__num_rows - 1
        goal = self.__cells[last_col][last_row]
        if current == goal:
            return True

        # check neighbouring cells
        # left
        if i - 1 >= 0:
            left_cell = self.__cells[i - 1][j]
            if not current.has_left_wall and not left_cell.visited:
                current.draw_move(left_cell, undo=False)
                if self._solve_r(i - 1, j):
                    return True
                left_cell.draw_move(current, undo=True)
        # right
        if i + 1 < self.__num_columns:
            right_cell = self.__cells[i + 1][j]
            if not current.has_right_wall and not right_cell.visited:
                current.draw_move(right_cell, undo=False)
                if self._solve_r(i + 1, j):
                    return True
                right_cell.draw_move(current, undo=True)
        # up
        if j - 1 >= 0:
            top_cell = self.__cells[i][j - 1]
            if not current.has_top_wall and not top_cell.visited:
                current.draw_move(top_cell, undo=False)
                if self._solve_r(i, j - 1):
                    return True
                top_cell.draw_move(current, undo=True)
        # down
        if j + 1 < self.__num_rows:
            bottom_cell = self.__cells[i][j + 1]
            if not current.has_bottom_wall and not bottom_cell.visited:
                current.draw_move(bottom_cell, undo=False)
                if self._solve_r(i, j + 1):
                    return True
                bottom_cell.draw_move(current, undo=True)
        return False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def __animate(self) -> None:
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(ANIMATION_DELAY)
