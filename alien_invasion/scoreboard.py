import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information.

    Methods
    -------
    prep_score()
        Turn score into a rendered image
    prep_highest_score()
        Turn the highest score into a rendered image
    prep_level()
        Turn level into a rendered image
    prep_ships()
        Show how many ships are available
    show_score()
        Draw score and available ships to the screen
    """

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes.

        Parameters
        ----------
        ai_settings: Settings
            All settings for alien invasion
        screen: pygame.Surface
            The screen on which scoring information will be drawn
        stats: GameStats
            The game statistics
        """
        self._screen = screen
        self._screen_rect = screen.get_rect()
        self._ai_settings = ai_settings
        self._stats = stats

        # Font setting for scoring information.
        self._text_color = (30, 30, 30)
        self._font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_highest_score()

    def prep_score(self):
        """Turn score into a rendered image."""
        rounded_score = int(round(self._stats.score, -1))
        score_str = f'{rounded_score:,}'
        self._score_image = self._font.render(score_str, True,
                                              self._text_color,
                                              self._ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self._score_rect = self._score_image.get_rect()
        self._score_rect.right = self._screen_rect.right - 20
        self._score_rect.top = 20

    def prep_level(self):
        """Turn level into a rendered image."""
        level_str = str(self._stats.level)
        self._level_image = self._font.render(level_str, True,
                                              self._text_color,
                                              self._ai_settings.bg_color)
        # Display the level below the score.
        self._level_rect = self._level_image.get_rect()
        self._level_rect.centerx = self._score_rect.centerx
        self._level_rect.top = self._score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are available."""
        self._ships = Group()
        for ship_number in range(self._stats.ships_left):
            ship = Ship(self._ai_settings, self._screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self._ships.add(ship)

    def prep_highest_score(self):
        """Turn the highest score into a rendered image."""
        highest_score = int(round(self._stats.highest_score, -1))
        highest_score_str = f'{highest_score:,}'
        self._highest_score_image = self._font.render(
            highest_score_str, True, self._text_color,
            self._ai_settings.bg_color)
        # Display the highest score at the top center of the screen.
        self._highest_score_rect = self._highest_score_image.get_rect()
        self._highest_score_rect.centerx = self._screen_rect.centerx
        self._highest_score_rect.top = self._screen_rect.top

    def show_score(self):
        """Draw score and available ships to the screen."""
        self._screen.blit(self._score_image, self._score_rect)
        self._screen.blit(self._highest_score_image, self._highest_score_rect)
        self._screen.blit(self._level_image, self._level_rect)
        self._ships.draw(self._screen)
