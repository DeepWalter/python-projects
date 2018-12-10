import pygame


def show_grid(settings, screen):
    """Show the grid of the matrix."""
    matrix_left, matrix_top = 0, 0
    matrix_right = settings.matrix_width * settings.block_size
    matrix_bottom = settings.matrix_height * settings.block_size
    for i in range(settings.matrix_height + 1):
        pygame.draw.line(screen, settings.color['gray'],
                         (matrix_left, i * settings.block_size),
                         (matrix_right, i * settings.block_size))
    for i in range(settings.matrix_width + 1):
        pygame.draw.line(screen, settings.color['gray'],
                         (i * settings.block_size, matrix_top),
                         (i * settings.block_size, matrix_bottom))

#     for i in range(1, settings.matrix_width + 1, 2):
#         column = pygame.Rect(i * settings.block_size,
#                              0,
#                              settings.block_size,
#                              settings.matrix_height * settings.block_size)
#         pygame.draw.rect(screen, settings.color['oldlace'], column)
