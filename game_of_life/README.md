# Game of Life

[![Python-Version](https://img.shields.io/badge/python-3.6.7-blue.svg)](https://docs.python.org/3.6/)
![Numpy-Version](https://img.shields.io/badge/numpy-1.15.4-blue.svg)
![Matplotlib-Version](https://img.shields.io/badge/matplotlib-3.0.2-blue.svg)

## Description

### Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in
one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its
eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time,
the following transitions occur:

* Any live cell with fewer than two live neighbors dies, as if by underpopulation.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by overpopulation.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules
simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this
happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be
applied repeatedly to create further generations.

## Code Design Details

### Main Logic

Main logic of the code:

* Initialize the cells in the grid;
* At each timestep:
  * update the status of each cell based on its neighbours;
  * update the display of the grid.