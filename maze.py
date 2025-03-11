import time
import random
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._window)
                row.append(cell)
            self._cells.append(row)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # check if no window was provided
        # allows unittests to run
        if self._window is None:
            return
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        # check if no window was provided
        # allows unittests to run
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[-1][-1]
        first_cell.has_top_wall = False
        last_cell.has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            neighbors = []

            # check valid cell up
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))

            # check valid cell down
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))

            # check valid cell left
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))

            # check valid cell right
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))

            # no directions to go
            if not neighbors:
                self._draw_cell(i, j)
                return
            else:
                next_i, next_j = random.choice(neighbors)
                next_cell = self._cells[next_i][next_j]

                # cell on top
                if next_i == i - 1:
                    cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                # cell on bottom
                elif next_i == i + 1:
                    cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                # cell on left
                elif next_j == j - 1:
                    cell.has_left_wall = False
                    next_cell.has_right_wall = False
                # cell on right
                elif next_j == j + 1:
                    cell.has_right_wall = False
                    next_cell.has_left_wall = False

                self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        cell = self._cells[i][j]
        cell.visited = True

        # check if we are at the end
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for di, dj in directions:
            next_i = i + di
            next_j = j + dj

            # check if next cell is valid
            if (0 <= next_i < self._num_rows) and (0 <= next_j < self._num_cols):
                next_cell = self._cells[next_i][next_j]
                if not next_cell.visited:
                    # moving right
                    if (di, dj) == (0, 1) and not cell.has_right_wall:
                        cell.draw_move(next_cell)
                        if self._solve_r(next_i, next_j):
                            return True
                        # undo move
                        cell.draw_move(next_cell, True)
                    # moving left
                    elif (di, dj) == (0, -1) and not cell.has_left_wall:
                        cell.draw_move(next_cell)
                        if self._solve_r(next_i, next_j):
                            return True
                        cell.draw_move(next_cell, True)
                    # moving down
                    elif (di, dj) == (1, 0) and not cell.has_bottom_wall:
                        cell.draw_move(next_cell)
                        if self._solve_r(next_i, next_j):
                            return True
                        cell.draw_move(next_cell, True)
                    # moving up
                    elif (di, dj) == (-1, 0) and not cell.has_top_wall:
                        cell.draw_move(next_cell)
                        if self._solve_r(next_i, next_j):
                            return True
                        cell.draw_move(next_cell, True)

        # no valid moves
        return False
