"""A collection of game utility functions.

Functions exported:
* create_fleet
* check_events
* update_aliens
* update_bullets
* update_screen
"""
import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_event(event, ai_settings, stats, score_board, screen, ship,
                        aliens, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_q:  # both active and inactive.
        sys.exit()
    elif stats.game_active:  # update game event only when game is active.
        if event.key == pygame.K_RETURN:
            stats.game_paused = not stats.game_paused
        elif not stats.game_paused:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        restart_game(ai_settings, stats, score_board, screen, ship, aliens,
                     bullets)


def restart_game(ai_settings, stats, score_board, screen, ship, aliens,
                 bullets):
    """Reset game statistics and start a new game."""
    stats.reset_stats()
    stats.game_active = True
    # Reset game speed.
    ai_settings.initialize_dynamic_settings()
    # Reset the scoreboard.
    score_board.prep_score()
    score_board.prep_level()
    score_board.prep_ships()
    score_board.prep_highest_score()

    start_new_game(ai_settings, screen, ship, aliens, bullets)


def check_highest_score(stats, score_board):
    """Check if there is a new highest score."""
    if stats.highest_score < stats.score:
        stats.highest_score = stats.score
        score_board.prep_highest_score()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if maximum bullets number not reached yet."""
    # Create a new bullet and add it to bullets group.
    if len(bullets) < ai_settings.bullet_max_num:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, stats, ship):
    """Respond to key releases."""
    if stats.game_active:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False


def check_events(ai_settings, stats, score_board, screen, play_button, ship,
                 aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, stats, score_board, screen,
                                ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, stats, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_board,
                              play_button, ship, aliens, bullets,
                              mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, score_board, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new play when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Restart the game.
        restart_game(ai_settings, stats, score_board, screen, ship, aliens,
                     bullets)


def start_new_game(ai_settings, screen, ship, aliens, bullets):
    """Start a new game."""
    # Empty the group of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet of aliens and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.reset_ship()


def update_screen(ai_settings, screen, stats, score_board, ship, aliens,
                  bullets, play_button, pause_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Redraw the ship.
    ship.blitme()
    # Redraw the alien.
    aliens.draw(screen)

    # Draw the score information.
    score_board.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    if stats.game_paused:
        pause_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, score_board, ship, aliens,
                   bullets):
    """Update position of bullets and delete old bullets."""
    # Update position of bullets.
    bullets.update()

    # Delete bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, score_board,
                                  ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, score_board,
                                  ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Check for any bullets that have hit aliens. If so, delete both the
    # bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        score_board.prep_score()
        check_highest_score(stats, score_board)

    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        # Increase a level.
        stats.level += 1
        score_board.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def get_num_aliens_x(ai_settings, alien_width):
    """Compute the number of aliens that fit in a row."""
    available_spacex = ai_settings.screen_width - 2 * alien_width
    num_aliens_x = int(available_spacex / (2 * alien_width))
    return num_aliens_x


def get_num_rows(ai_settings, alien_height, ship_height):
    """Compute the number of rows of aliens that fit on the screen."""
    available_spacey = (ai_settings.screen_height -
                        3 * alien_height - ship_height)
    num_rows = int(available_spacey / (2 * alien_height))
    return num_rows


def create_alien(ai_settings, screen, aliens, alien_id, row_id):
    """Create an alien and put it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_id
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_id
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    num_aliens_x = get_num_aliens_x(ai_settings, alien.rect.width)
    num_rows = get_num_rows(ai_settings, alien.rect.height, ship.rect.height)

    # Create a fleet of aliens.
    for row_id in range(num_rows):
        for alien_id in range(num_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_id, row_id)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any alien has reached the edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, score_board, screen, ship, aliens, bullets):
    """Respond to ship being hit by aliens."""
    # Decrement ships_left.
    stats.ships_left -= 1
    score_board.prep_ships()

    if stats.ships_left > 0:
        start_new_game(ai_settings, screen, ship, aliens, bullets)
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, stats, score_board, screen, ship, aliens,
                  bullets):
    """Update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score_board, screen, ship, aliens,
                 bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, score_board, screen, ship, aliens,
                        bullets)


def check_aliens_bottom(ai_settings, stats, score_board, screen, ship, aliens,
                        bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as the ship being hit.
            ship_hit(ai_settings, stats, score_board, screen, ship, aliens,
                     bullets)
            break


def counter(collection, last_count=0):
    """Generate a counter printing the number of elements in collection.

    The returned counter takes no argument. The counter prints out the
    length of collection only when it changes.
    """
    print(f'Initial bullets number: {last_count}')

    def count():
        """Print number of elements in collectioin if it changes."""
        nonlocal last_count
        if len(collection) != last_count:
            last_count = len(collection)
            print(last_count)
    return count
