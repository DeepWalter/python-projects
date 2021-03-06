import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class used to represent a single alien.

    Attributes
    ----------
    ai_settings: Settings
        All settings in alien invasion
    image: pygame.Surface
        The image of the alien
    rect: pygame.Rect
        Rectangular coordinates of the alien
    x: float
        Accurate x-coordinate of the alien

    Methods
    -------
    blitme()
        Draw the alien at its current location
    check_edges()
        Check if alien is at the right or left edge of the screen
    update()
        Move the alien horizontally
    """

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its start position.

        Parameters
        ----------
        ai_settings: Settings
            All settings in alien invasion
        screen: pygame.Surface
            The screen on which the alien is drawn
        """
        super().__init__()
        self._screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self._screen.blit(self.image, self.rect)

    def check_edges(self):
        """Check if alien is at the right or left edge of the screen."""
        screen_rect = self._screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
        else:
            return False

    def update(self):
        """Move the alien horizontally."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
