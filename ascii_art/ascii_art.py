import argparse

import numpy as np
from PIL import Image

# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
grayscale70 = ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!"
               "lI;:,\"^`'. ")

# 10 levels of gray
grayscale10 = "@%#*+=-:. "


def image_to_ascii(filename, cols, scale, more=True):
    """Convert image to ASCII.

    Parameters
    ----------
    filename: str
        Name of the image file to be converted.
    cols: int
        Number of columns of the output ASCII art.
    scale: float
        Aspect ratio (ratio of width to height) of the output ASCII art.
    more: bool, optional
        Use grayscale 70 or 10 (default to True, using grayscale 70).

    Returns
    -------
    list[str]
        The converted ASCII art as a list of strings.
    """
    # grayscale globals.
    global grayscale70, grayscale10

    # open image and convert to grayscale.
    image = Image.open(filename).convert('L')

    # image dimensions.
    W, H = image.size[0], image.size[1]
    print(f'Input image dims: {W} x {H}')

    # compute tile width and height.
    width = W / cols
    height = width / scale
    # compute number of rows to use in the final grid.
    rows = int(H / height)

    print(f'cols: {cols}, rows: {rows}')
    print(f'tile dims: {width} x {height}')

    # check if image is too small.
    if cols > W or rows > H:
        print('Image too small to specified cols!')
        exit(0)

    # an ASCII image is a list of character strings.
    aimg = []
    for i in range(rows):
        upper = int(i * height)  # upper pixel coordinate of the tile
        lower = int((i+1) * height)  # lower pixel coordinate of the tile
        if i == rows-1:  # adjust the last tile in a column
            lower = H

        aimg.append('')
        for j in range(cols):
            left = int(j * width)  # left pixel coordinate of the tile
            right = int((j+1) * width)  # right pixel coordinate of the tile
            if j == cols-1:  # adjust the last tile in a row
                right = W

            img = image.crop((left, upper, right, lower))
            avg = int(np.average(img))  # average grayscale

            # convert the grayscale into char.
            if more:
                gsval = grayscale70[int((avg*69)/255)]
            else:
                gsval = grayscale10[int((avg*9)/255)]

            aimg[i] += gsval

    return aimg


if __name__ == '__main__':
    # provide the command line options.
    parser = argparse.ArgumentParser(
        prog='python ascii_art.py',
        description='Convert image into ASCII art.'
    )

    parser.add_argument(
        '--file',
        dest='filename',
        type=str,
        required=True,
        help='path to the image file'
    )

    parser.add_argument(
        '--scale',
        dest='scale',
        type=float,
        required=False,
        default=0.43,
        help='aspect ratio of the output. Optional, default to 0.43'
    )

    parser.add_argument(
        '--cols',
        dest='cols',
        type=int,
        required=False,
        default=80,
        help='number of columns of the output. Optional, default to 80'
    )

    parser.add_argument(
        '--more',
        dest='more',
        type=bool,
        required=False,
        default=True,
        help='use more levels of gray? Optional, default to True'
    )

    parser.add_argument(
        '--out',
        dest='out',
        type=str,
        required=False,
        default=None,
        help='name of the output file. Optional, default to None'
    )

    # Parse arguments.
    args = parser.parse_args()

    print('Generating ASCII art...')

    aimg = image_to_ascii(args.filename, args.cols, args.scale, args.more)

    if args.out is not None:
        with open(args.out, 'w') as f:
            for row in aimg:
                f.write(row + '\n')
        print(f'ASCII art written to {args.out}')
    else:
        print('\n')
        for row in aimg:
            print(row)
# Feb 10, 2019 TODO: make the comment style consistent.
