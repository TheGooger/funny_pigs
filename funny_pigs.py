import pygame
from settings import Settings
from pig import Pig
import game_functions as gf


def run_game():
    # Initialization of pygame, settings and screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Funny pigs!")
    # Pig creation.
    pig = Pig(screen)

    # Starting of main game cycle.
    while True:
        gf.check_events()
        gf.update_screen(game_settings, screen, pig)


run_game()
