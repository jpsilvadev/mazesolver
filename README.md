# Maze Solver

A maze generator and solver with a Tkinter GUI. The maze is generated using
randomized recursive backtracking and solved with a depth-first search,
animating each step as it happens.

## Features

- Procedural maze generation via recursive backtracking
- Depth-first search solver with live animation of forward moves and
  backtracking
- Configurable grid size, cell dimensions, animation speed, and colors
- Step and move counters reported once the maze is solved

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
git clone https://github.com/jpsilvadev/mazesolver.git
cd mazesolver
uv sync
```

## Usage

```bash
uv run main.py
```

This opens a window, generates a maze, and solves it. Forward moves are drawn
in red, backtracked moves in gray. Once solved, the window shows the number
of steps in the solution path and the total moves taken (including
backtracking).

## Configuration

Maze parameters live in [config.py](config.py):

| Variable | Description |
| --- | --- |
| `SCREEN_X`, `SCREEN_Y` | Window dimensions in pixels |
| `MAZE_MARGIN` | Margin between the maze and the window edges |
| `COLS`, `ROWS` | Grid dimensions |
| `ANIMATION_DELAY` | Delay in seconds between animation frames |
| `FORWARD_COLOR` | Line color for forward moves |
| `BACKTRACKING_COLOR` | Line color for backtracked moves |

## Project structure

```
mazesolver/
├── main.py     # Entry point
├── maze.py     # Maze generation and solving logic
├── cell.py     # A single maze cell, its walls, and how it draws itself
├── gui.py      # Tkinter window, canvas, and line drawing primitives
└── config.py   # Maze and rendering configuration
```

## License

[MIT](LICENSE)
