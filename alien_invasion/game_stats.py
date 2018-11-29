class GameStats:
    """A class used to track statistics for alien invasion.

    Attributes
    ----------
    ai_settings: Settings
        All settings for alien invasion
    game_active: bool
        The status of the game
    highest_score: int
        The highest score in the game
    ship_left: int
        The number of available ships
    score: int
        Current score
    level: int
        Current level

    Methods
    -------
    reset_stats()
        Reset statistics when replay the game
    """

    def __init__(self, ai_settings):
        """Initialize statistics.

        Parameters
        ----------
        ai_settings: Settings
            All settings for alien invasion
        """
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # Highest score should never be reset.
        self.game_paused = False
        self.highest_score = 0

    def reset_stats(self):
        """Reset statistics when replay the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
