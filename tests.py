import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        m1 = Maze(x1=0, y1=0, num_rows=10, num_cols=12, cell_size_x=10, cell_size_y=10)
        self.assertEqual(len(m1._cells), 10)
        self.assertEqual(len(m1._cells[0]), 12)

    def test_maze_create_cells_margin(self):
        m2 = Maze(
            x1=50, y1=50, num_rows=12, num_cols=16, cell_size_x=40, cell_size_y=40
        )
        self.assertEqual(len(m2._cells), 12)
        self.assertEqual(len(m2._cells[0]), 16)


if __name__ == "__main__":
    unittest.main()
