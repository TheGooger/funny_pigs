import sys
import pygame


def check_events():
    """Processes keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(game_settings, screen, pig):
    """Updates images on the screen and shows new screen."""
    # Draw screen.
    screen.fill(game_settings.bg_color)
    pig.blitme()
    # Shows last printed screen.
    pygame.display.flip()
