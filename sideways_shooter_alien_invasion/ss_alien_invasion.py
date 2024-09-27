import sys
from time import sleep

from pathlib import Path
import json

import pygame
 
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from button import Button
from alien import Alien

class AlienInvasion :
    """Overall class to manage game assets and behavior."""

    def __init__(self) :
        """Initialize the game, and create game resources."""
        pygame.init()
    
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.screen_rect = self.screen.get_rect()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Start Sideways Shooter in an active state.
        self.game_active = False

        # Make the play button.
        self.play_button = Button(self, "Play")

    def run_game(self) :
        """Start the main loop for the game."""
        while True :
            self._check_events()

            if self.game_active :
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) :
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                self._exit_game()
            elif event.type == pygame.KEYDOWN :
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP :
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos) :
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active :
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _start_game(self) :
        """Start a new game when the player presses p or cl  icks play."""
        # Reset the game statistics.
        self.stats.reset_stats()
        # Ensure the level image updates properly at the start of a new game.
        self.sb.prep_images()
        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event) :
        """Respond to keypresses."""
        if event.key == pygame.K_UP :
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN :
            self.ship.moving_down = True
        elif event.key == pygame.K_q :
            self._exit_game()
        elif event.key == pygame.K_p :
            self._start_game()
        elif event.key == pygame.K_SPACE :
            self._fire_bullet()

    def _check_keyup_events(self, event) :
        """Respond to key releases."""
        if event.key == pygame.K_UP :
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN :
            self.ship.moving_down = False

    def _exit_game(self) :
        """Save all time high score and exit the game."""
        # Load the all time high score from json path,
        #   check if current high score is greater than stored
        #   all time high score,
        #   if it is, write the new high score to json path,
        #   if it is not, exit the game.
        path = Path('high_score.json')
        if path.exists() :
            contents = path.read_text()
            ATH_score = json.loads(contents)
            if self.stats.high_score > ATH_score :
                new_high_score = json.dumps(self.stats.high_score)
                path.write_text(new_high_score)
        else :
            new_high_score = json.dumps(self.stats.high_score)
            path.write_text(new_high_score)

        sys.exit()
    
    def _fire_bullet(self) :
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) :
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy() :
            if bullet.rect.left >= self.screen_rect.right :
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self) :
        """Respond to bullet-alien collisions."""        
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        
        if collisions :
        # Loop through the values in the collisions dictionary to make sure we
        #   award points for each alien hit.
            for aliens in collisions.values() :
                self.stats.score += self.settings.alien_points * len(aliens)

            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens :
            self._start_new_level()

    def _start_new_level(self) :
        """Remove bullets, increase difficulty."""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self) :
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens) :
            self._ship_hit()

        # Look for aliens hitting the left of the screen.
        self._check_aliens_left()

    def _create_fleet(self) :
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = (self.settings.screen_width - alien_width), alien_height
        while current_x > (8 * alien_width) :
            while current_y <= (self.settings.screen_height - 1 * alien_height) :
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height

            # Finished a row; reset y value, and increment x value.
            current_x -= 2 * alien_width
            current_y = alien_height

    def _create_alien(self, x_position, y_position) :
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self) :
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites() :
            if alien.check_edges() :
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) :
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites() :
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self) :
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 1 :
            # Decrement ships left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens.
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(1)
        else :
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_left(self) :
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites() :
            if alien.rect.left <= 0 :
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_screen(self) :
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play buttom if the game is inactive.
        if not self.game_active :
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__' :
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()