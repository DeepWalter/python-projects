import math

import pygame

# Test
# from settings import Settings


class IShape:
    """A class represents the I-shaped tetromino.

    Attributes
    ----------
    moving_direction: int
        Moving direction. 1 represents right, -1 left, 0 static

    Methods
    -------
    drop()
        Move down the tetromino by one block
    move()
        Move the tetromino horizontally by one block
    draw(screen)
        Draw the current shape onto the screen
    """

    def __init__(self, settings):
        """Initialize the tetromino."""
        self._settings = settings
        self._color = self._settings.color['cyan']
        self._shapes = (Shape(settings, [0, 1, 2, 3], self._color),
                        Shape(settings, [-11, 1, 13, 25], self._color))
        self._shape_id = 1
        self._position = Coordinate(self._settings.matrix_width)
        # Set start position at top center
        self._position.x = 4
        # self._position.y = 1
        self.moving_direction = 0

    def drop(self):
        """Move down the tetromino by one block."""
        self._position.y += 1

    def move(self):
        """Move the tetromino horizontally by one block."""
        self._position.x += self.moving_direction

    def rotate(self):
        """Rotate right 90 degree."""
        self._shape_id = (self._shape_id + 1) % 2

    def draw(self, screen):
        """Draw the current shape onto the screen."""
        self._shapes[self._shape_id].draw(screen,
                                          self._position.x, self._position.y)


class Coordinate:
    """The coordinate system used in the matrix.

    TODO: Descriptions needed.

    Attributes
    ----------
    id: int
        The index of the block
    x: int
        The x coordinate of the block
    y: int
        The y coordinate of the block
    """

    def __init__(self, width, index=0):
        """Initialize the coordinate to the first block.

        Parameters
        ----------
        width: int
            Number of blocks in each row
        index: int, optional
            Index of the block. (default to 0)
        """
        self._width = width
        self.id = index

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, num):
        """Also update the x and y coordinates."""
        self._id = num
        self._y = math.floor(num / self._width)
        self._x = num - self._y * self._width

    @property
    def x(self):
        return self._x

    # TODO: check if x <= width
    @x.setter
    def x(self, num):
        """Also update the id coordinate."""
        self._x = num
        self._id = self._y * self._width + num

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, num):
        """Also update the id coordinate."""
        self._y = num
        self._id = num * self._width + self._x

    def show(self):
        """For test only."""
        print(f'id is {self._id}, x is {self._x}, y is {self._y}')


class Block:
    """A class used to represent a block in the matrix.

    Attributes
    ----------
    position: Coordinate
        The coordinate of the block

    Methods
    -------
    draw(screen, color, x=0, y=0)
        Draw the block on the screen
    """

    def __init__(self, settings, index=0):
        """Initialize the block.

        Parameters
        ----------
        settings: Settings
            All setting in tetris
        index: int
            Index of the block. (default to 0)
        """
        self._settings = settings
        self.position = Coordinate(self._settings.matrix_width, index)

    def draw(self, screen, color, x=0, y=0):
        """Draw the block on the screen.

        The optional arguments x and y specify the position where the
        block is drawn relative to the (0, 0) block.

        Parameters
        ----------
        screen: pygame.Surface
            The screen on which the block is drawn
        color: tuple of int
            RGB color of the block
        x: int
            x-shift from (0, 0). (default to 0)
        y: int
            y-shift from (0, 0). (default to 0)
        """
        block_size = self._settings.block_size
        block_rect = pygame.Rect((x + self.position.x) * block_size,
                                 (y + self.position.y) * block_size,
                                 block_size, block_size)
        pygame.draw.rect(screen, color, block_rect)


class Shape:
    """A class used to represents a single shape.

    Methods
    -------
    draw(screen, x=0, y=0)
        Draw the shape on the screen
    """

    def __init__(self, settings, id_list, color):
        """Initialize the shape."""
        self._settings = settings
        self._color = color
        self._blocks = tuple(Block(settings, i) for i in id_list)

    def draw(self, screen, x=0, y=0):
        """Draw the shape on the screen.

        Parameters
        ----------
        screen: pygame.Surface
            The screen on which the shape is drawn
        x: int
            x-shift from (0, 0). (default to 0)
        y: int
            y-shift from (0, 0). (default to 0)
        """
        for block in self._blocks:
            block.draw(screen, self._color, x, y)


if __name__ == '__main__':
    coord = Coordinate(12, -11)
    coord.show()
