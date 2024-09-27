from pathlib import Path
import json

class GameStats :
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) :
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
#        self.high_score = 0

        # Initialize the stored high score from high_score.json path.
        path = Path('high_score.json')
        if path.exists() :
            contents = path.read_text()
            self.high_score = json.loads(contents)
        else :
            self.high_score = 0

    def reset_stats(self) :
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1