import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship.

    Attributes
    ----------
    rect: pygame.Rect
        Rectangular coordinates of the bullet

    Methods
    -------
    update()
        Move the bullet up the screen
    draw_bullet()
        Draw the bullet to the screen
    """

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current location.

        Parameters
        ----------
        ai_settings: Settings
            All settings for alien invasion
        screen: pygame.Surface
            The screen on which the bullet will be drawn
        ship: Ship
            The ship that fires the bullet
        """
        super().__init__()
        self._screen = screen

        # Create a bullet rect at (0, 0) and set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        # Store the bullet's position as a decimal value.
        self._y = float(self.rect.y)

        self._color = ai_settings.bullet_color
        self._speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self._y -= self._speed_factor
        self.rect.y = self._y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self._screen, self._color, self.rect)
