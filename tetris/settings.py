# from tetrominos import Shape


class Settings:
    """A class to store all settings for tetris.

    Attributes
    ----------
    title: str
        Title of the game
    screen_width: int
        Width of the screen
    screen_height: int
        Height of the screen
    matrix_width: int
        Number of blocks in the row of the matrix
    matrix_height: int
        Number of blocks in the column of the matrix
    block_size: int
        Number of pixels in each side of the square block
    color: dict
        A dict containing various colors and their RGBs
    """

    def __init__(self):
        """Initialize game's settings."""
        self.title = 'Tetris'
        self.screen_width = 900
        self.screen_height = 600
        self.matrix_width = 12
        self.matrix_height = 24
        self.block_size = 25
        self.color = {'black': (0, 0, 0),
                      'gray': (128, 128, 128),
                      'white': (255, 255, 255),
                      'cyan': (0, 255, 255),
                      'floral': (255, 250, 240),
                      'antique': (250, 235, 215),
                      'oldlace': (253, 245, 230)
                      }
        # self.tetrominos = {
        #     'I': (
        #         Shape(self.matrix_width, [0, 1, 2, 3]),
        #         Shape(self.matrix_width, [-13, 1, 13, 25])
        #     )
        # }
