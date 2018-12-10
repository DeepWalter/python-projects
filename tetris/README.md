# Tetris

## Game Description

## Code Design Details

### Matrix

We treat the playing field, also called the matrix, as an one dimensional array with the first element being the top
left block of the matrix. Each shape contains 4 block.

## TODOs

* [x] Create a screen.
* [x] Draw grid for the matrix.
* [x] Ishape tetromino.
  * [x] Shape
  * [x] Drop
  * [x] Move horizontally
  * [x] Rotate
* [ ] Rethink how to represent a tetromino
  * [ ] Represent the matrix as a collections of blocks
  * [ ] Each block has a coordinate and a draw method.
  * [ ] Each shape consist of four blocks.