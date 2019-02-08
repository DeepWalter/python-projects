import numpy as np
from PIL import Image

# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
grayscale70 = ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!"
               "lI;:,\"^`'. ")

# 10 levels of gray
grayscale10 = "@%#*+=-:. "


def image_to_ascii(image_file, cols, scale, more):
    """Convert image to ascii."""
    # grayscale globals.
    global grayscale70, grayscale10

    # open image and convert to grayscale.
    image = Image.open(image_file).convert('L')

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

    # check if image is too small
    if cols > W or rows > H:
        print('Image too small to specified cols!')
        exit(0)

    # an ASCII image is a list of character strings.
    aimg = []
    for i in range(rows):
        y1 = int(i * height)
        y2 = int((i+1) * height)
        if i == rows-1:
            y2 = H

        aimg.append('')
        for j in range(cols):
            x_left = int(j * width)
            x_right = int((j+1) * width)
            if j == cols-1:
                x_right = W
            img = image.crop((x_left, y1, x_right, y2))
            # average grayscale
            avg = int(np.average(img))

            if more:
                gsval = grayscale70[int((avg*69)/255)]
            else:
                gsval = grayscale10[int((avg*9)/255)]

            aimg[i] += gsval

    return aimg


if __name__ == '__main__':
    aimg = image_to_ascii('./lal.jpg', 128, 0.5, True)
    f = open('out.txt', 'w')
    for row in aimg:
        f.write(row + '\n')
    f.close()
