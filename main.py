from graphics import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)

    cell = Cell(window)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(150, 50, 200, 100)

    cell = Cell(window)
    cell.has_top_wall = False
    cell.draw(250, 50, 300, 100)

    cell = Cell(window)
    cell.has_bottom_wall = False
    cell.draw(350, 50, 400, 100)

    cell = Cell(window)
    cell.draw(450, 50, 500, 100)

    window.wait_for_close()


if __name__ == "__main__":
    main()
