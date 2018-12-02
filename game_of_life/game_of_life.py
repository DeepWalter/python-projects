import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife:
    """A class used to simulate Conway's game of life.

    Methods
    -------
    set_grid(style='random')
        Set up the grid.
    add_glider(pos=(0, 0))
        Add a glider with top-left at position pos.
    update_grid()
        Update the grid once.
    show_grid()
        Show the current status of all cells.
    show(filename=None, interval=100)
        Show and save the animation of game of life.
    """
    ON = 1
    OFF = 0
    VALUES = (ON, OFF)

    def __init__(self, N=100):
        """Initialize game of life.

        Parameters
        ----------
        N : int, optional
            Size of the grid (default is 100).
        """
        self._N = N

        self.set_grid()

    def set_grid(self, style='random'):
        """Set up the grid.

        Parameters
        ----------
        style : str
            Style of the grid (default is 'random').
        """
        self._grid = np.random.choice(
            type(self).VALUES, (self._N, self._N), (0.2, 0.8)
        ).reshape((self._N, self._N))

    def add_glider(self, pos=(0, 0)):
        """Add a glider with top-left at position pos.

        Parameters
        ----------
        pos: tuple of int, optional
            (row, col)-coordinate of the top-left of the glider to be
            placed (default is (0, 0)).
        """
        row, col = pos
        self._grid[row:row+3, col:col+3] = np.array([[0, 0, 1],
                                                     [1, 0, 1],
                                                     [0, 1, 1]])

    def update_grid(self):
        """Update the grid once."""
        old_grid = self._grid.copy()
        N = self._N
        for i in range(N):
            for j in range(N):
                total = (old_grid[i, (j-1) % N]  # up
                         + old_grid[i, (j+1) % N]  # down
                         + old_grid[(i-1) % N, j]  # left
                         + old_grid[(i+1) % N, j]  # right
                         + old_grid[(i-1) % N, (j-1) % N]  # top-left
                         + old_grid[(i+1) % N, (j-1) % N]  # top-right
                         + old_grid[(i-1) % N, (j+1) % N]  # bottom-left
                         + old_grid[(i+1) % N, (j+1) % N])  # bottom-right

                # Apply the rule
                if old_grid[i, j] == type(self).ON:
                    if (total < 2) or (total > 3):
                        self._grid[i, j] = type(self).OFF
                else:
                    if total == 3:
                        self._grid[i, j] = type(self).ON

    def show_grid(self):
        """Show the current status of all cells."""
        plt.imshow(self._grid, interpolation='nearest')
        plt.show()

    def _update(self, frame, img):
        # Update grid
        self.update_grid()
        img.set_data(self._grid)
        return img

    def show(self, filename=None, interval=100):
        """Show and save the animation of game of life.

        Parameters
        ----------
        filename : str, optional
            Name of the file in which the animation is saved using the
            ImageMagick writer (default is None, which means not saved).
        interval : int, optional
            Delay between frames in milliseconds (default is 100).
        """
        # Set up animation.
        fig, ax = plt.subplots()
        plt.axis('off')
        img = ax.imshow(self._grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self._update, fargs=(img,),
                                      frames=50,
                                      interval=interval,
                                      save_count=50)
        # Save the animation.
        if filename is not None:
            ani.save(filename, fps=10, writer='imagemagick')
        plt.show()


def main():
    """Main function."""
    # Parse the command line arguments
    # sys.argv[0] is the script name
    # Command line arguments are in sys.argv[1], sys.argv[2], ...
    parser = argparse.ArgumentParser(
        prog='python game_of_life.py',
        description="Run Conway's game of life simulation."
    )
    # Add arguments
    parser.add_argument(
        '--grid-size',  # name of the option
        dest='N',  # name of attr returned by parse_args()
        type=int,  # type of attr
        default=100,  # default value
        required=False,  # this option is optional
        help='Size of the squared grid. (default to 100)'  # help info
    )

    args = parser.parse_args()

    print(args.N)


if __name__ == '__main__':
    game = GameOfLife()
    game.show('./gof.gif')
