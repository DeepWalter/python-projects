import pygame
import pygame.font


class Button:
    """A class represents a button as filled rectangle with a label.

    Attributes
    ----------
    rect: pygame.Rect
        Rectangular coordinates of the button

    Methods
    -------
    draw_button()
        Draw the button and its message on the screen
    """

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes.

        Parameters
        ----------
        ai_settings: Settings
            All settings for alien invasion
        screen: pygame.Surface
            The screen on which the button will be drawn
        msg: str
            The message displayed on the button
        """
        self._screen = screen
        self._screen_rect = self._screen.get_rect()

        # Set the dimensions and properties of the button.
        self._width, self._height = 200, 50
        self._button_color = (169, 169, 169)
        self._text_color = (255, 255, 255)
        self._font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self._width, self._height)
        self.rect.center = self._screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self._msg_image = self._font.render(msg, True, self._text_color,
                                            self._button_color)
        self._msg_image_rect = self._msg_image.get_rect()
        self._msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and its message on the screen."""
        self._screen.fill(self._button_color, self.rect)
        self._screen.blit(self._msg_image, self._msg_image_rect)
