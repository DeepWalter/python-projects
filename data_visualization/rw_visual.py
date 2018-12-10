import matplotlib.pyplot as plt

from random_walk import RandomWalk


if __name__ == '__main__':
    while True:
        rw = RandomWalk()
        rw.fill_walk()

        plt.figure(figsize=(10, 6))
        point_numbers = list(range(len(rw.x_values)))

        plt.scatter(rw.x_values, rw.y_values, s=4, c=point_numbers,
                    cmap=plt.cm.Blues, edgecolors='none')
        # Emphasize the first and last points.
        plt.scatter(0, 0, c='green', s=25, edgecolors='none')
        plt.scatter(rw.x_values[-1], rw.y_values[-1],
                    c='red', s=25, edgecolors='none')
        plt.axis('off')
        plt.show()

        keep_running = input("Make another walk? (y/n)")
        if keep_running == 'n':
            break
