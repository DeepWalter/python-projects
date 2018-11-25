import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
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
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if maximum bullets number not reached yet."""
    # Create a new bullet and add it to bullets group.
    if len(bullets) < ai_settings.bullet_max_num:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
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

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and delete old bullets."""
    # Update position of bullets.
    bullets.update()

    # Delete bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens. If so, delete both the
    # bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet.
        bullets.empty()
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


def update_aliens(ai_settings, aliens):
    """Update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


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
