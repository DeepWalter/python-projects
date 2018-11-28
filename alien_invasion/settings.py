class Settings:
    """A class to store all settings for alien invasion.

    Attributes
    ----------
    screen_width: int
        Width of the screen
    screen_height: int
        Height of the screen
    bg_color: tuple
        RGB color of the background of the screen
    ship_limit: int
        Maximum number of the ships
    bullet_width: int
        Width of the bullet
    bullet_height: int
        Height of the bullet
    bullet_color: tuple
        RGB color of the bullet
    bullet_max_num: int
        Maximum number of bullets on the screen
    fleet_drop_speed: float
        Speed of the fleet dropping down
    speedup_scale: float
        Game speedup scale
    score_scale: float
        Score speedup scale
    ship_speed_factor: float
        Speed of the ship
    bullet_speed_factor: float
        Speed of the bullet
    alien_speed_factor: float
        Speed of the bullet
    fleet_direction: int
        Direction of the fleet movement. 1 represents right; -1 left
    alien_points: int
        Points rewarded for each alien being shot

    Methods
    -------
    initialize_dynamic_settings()
        Initialize settings that change throughout the game
    increase_speed()
        Increase speed settings and alien point values
    """

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_max_num = 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.3

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 5.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Fleet movement direction: 1 represents right; -1 left.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
