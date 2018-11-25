class Settings:
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Bullet settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_max_num = 3

        # Alien settings.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction: 1 represents right; -1 left.
        self.fleet_direction = 1
