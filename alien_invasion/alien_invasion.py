import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make the Play button.
    play_button = Button(ai_settings, screen, 'Play')
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a bullet group, and an alien group.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # count_bullets = gf.counter(bullets) # for DEBUG only
    aliens = Group()

    # Create a row of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, stats, score_board, screen, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score_board, ship,
                              aliens, bullets)
            # count_bullets() # for DEBUG only
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens,
                         bullets, play_button)


if __name__ == '__main__':
    run_game()
