from config import CELL_SIZE_X, CELL_SIZE_Y, COLS, MAZE_MARGIN, ROWS, SCREEN_X, SCREEN_Y
from gui import Window
from maze import Maze


def main() -> None:
    win = Window(SCREEN_X, SCREEN_Y)
    maze = Maze(MAZE_MARGIN, MAZE_MARGIN, ROWS, COLS, CELL_SIZE_X, CELL_SIZE_Y, win, 1)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
