import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font setting for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_level()
        self.prep_highest_score()

    def prep_score(self):
        """Turn score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Turn level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # Display the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.score_rect.centerx
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_highest_score(self):
        """Turn the highest score into a rendered image."""
        highest_score = int(round(self.stats.highest_score, -1))
        highest_score_str = f'{highest_score:,}'
        self.highest_score_image = self.font.render(highest_score_str, True,
                                                    self.text_color,
                                                    self.ai_settings.bg_color)
        # Display the highest score at the top center of the screen.
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.screen_rect.top

    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
