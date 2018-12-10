import sys
from time import sleep

import pygame

from settings import Settings
import game_functions as gf
# from tetrominos import IShape
from tetrominos import IShape


def run_game():
    pygame.init()
    # Load game settings.
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # ishape = IShape(settings, 'I')
    ishape = IShape(settings)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        screen.fill(settings.color['white'])
        # Draw the grid lines.
        gf.show_grid(settings, screen)

        ishape.draw(screen)

        # ishape.draw(screen)
        # ishape.drop()
        # # ishape.move()
        ishape.rotate()
        sleep(1)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
