from gui_elements import Window, Line, Point


def main():
    window = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    line = Line(point1, point2)
    window.draw_line(line, "red")

    window.wait_for_close()


if __name__ == "__main__":
    main()
