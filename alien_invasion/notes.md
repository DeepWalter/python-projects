# Alien Invasion Project Notes

## `Pygame` Basics

**Points:**
* `pygame.init()`: initialize background settings.
* `pygame.display.set_mode()`: create a display windown --- a *surface*.
* A **surface** is part of the screen where you display a game element.
* `pygame.display.set_mode()` returns a surface that represents the entire game window.
* An *event* is an action that user perform while playing the game, e.g. key stroke or mouse movement.
* `pygame.display.flip()`: make the most recent drawn screen visible.
* In `Pygame`, each event[^1] is picked up by `pygame.event.get()` method.
* Key press is registered as a `KEYDOWN` event; key release is registered as a `KEYUP` event.
* When calling a method on a group object, the method is called on each element of the object.
* When calling `draw()` on a group of surfaces, `Pygame` automatically draws each element at the position defined by
  its `rect`.

## Programming Tips

**Points:**
* Start out writing code as simple as possible, and refactor it as your project becomes more complex.
* Examine the code and determine if it needs to be refactored before implementing new features.
* When a function grows too long, it may be a good time to refactor it.
* Write decent docstring when coding. Don't rush!!!

---
[^1]: For example, a keypress or a mouse movement.