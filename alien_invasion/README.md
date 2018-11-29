# Alien Invasion

[![Python-Version](https://img.shields.io/badge/python-3.6.7-blue.svg)](https://docs.python.org/3.6/)
[![Pygame-Version](https://img.shields.io/badge/pygame-1.9.4-blue.svg)](https://www.pygame.org/wiki/GettingStarted)

## Game Description

In Alien Invasion:
* The player controls a ship that appears at the bottom center of the screen.
* The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
* When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
* Player shoots and destroys the aliens.
* If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
* If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship.
* If the player loses three ships, the game ends.

## Code Design Details

### Main Logic

The main logic of the code is rather simple. After setting up the screen, we create an infinite loop for the interactive
game play. Inside the `while` loop, we

1. watch for keyboard and mouse events;
2. make changes accordingly;
3. update the screen.

Step 1 and 2 are closely related. In those steps, we watch for keyboard and mouse events, and then respond to them. In
the last step, we just draw all the updated objects, namely the bullets, ship, aliens, score board, and buttons, onto
the screen.