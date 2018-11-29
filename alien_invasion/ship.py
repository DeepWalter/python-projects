import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class used to represent the ship.

    Attributes
    ----------
    ai_settings: Settings
        All settings in alien invasion
    image: pygame.Surface
        The image of the ship
    rect: pygame.Rect
        Rectangular coordinates of the ship
    centerx: float
        Accurate x-coordinate of the center of the ship
    centery: float
        Accurate y-coordinate of the center of the ship
    moving_right: bool
        A flag indicating whether the ship moves right
    moving_left: bool
        A flag indicating whether the ship moves left
    moving_up: bool
        A flag indicating whether the ship moves up
    moving_down: bool
        A flag indicating whether the ship moves down

    Methods
    -------
    blitme()
        Draw the ship at its current location
    update()
        Update the ship's position according to the movement flag
    reset_ship()
        Reset ship to its birthplace and make it static
    """

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position.

        Parameters
        ----------
        ai_setttings: Settings
            All settings in alien invasion
        screen: pygame.Surface
            The screen on which the ship is drawn
        """
        super().__init__()
        self._screen = screen
        self.ai_settings = ai_settings

        # Load the ship and get its rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self._screen_rect = screen.get_rect()

        # Store the ship's birthplace: bottom center of the screen
        self._birth_centerx = self._screen_rect.centerx
        self._birth_centery = self._screen_rect.height - self.rect.centery

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self._birth_centerx
        self.rect.centery = self._birth_centery

        # Store decimal values for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship at its current location."""
        self._screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position according to the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self._screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        # not elif since moveing_left and the rest are not mutually exclusive
        if self.moving_left and self.rect.left > self._screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self._screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self._screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        # Always make sure that the whole ship is in the screen
        if self.rect.right > self._screen_rect.right:
            self.rect.right = self._screen_rect.right
        if self.rect.left < self._screen_rect.left:
            self.rect.left = self._screen_rect.left
        if self.rect.top < self._screen_rect.top:
            self.rect.top = self._screen_rect.top
        if self.rect.bottom > self._screen_rect.bottom:
            self.rect.bottom = self._screen_rect.bottom

    def reset_ship(self):
        """Reset ship to its birthplace and make it static."""
        self.centerx = self._birth_centerx
        self.centery = self._birth_centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
