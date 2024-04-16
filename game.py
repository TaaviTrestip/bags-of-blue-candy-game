import pygame
import sys
from game_window import GameWindow
from button import Button
from player import Player
from game_stats import GameStats
import game_functions as functions


def run_game():
    pygame.init()
    game_screen = GameWindow()

    screen = pygame.display.set_mode([game_screen.screen_width, game_screen.screen_height])
    pygame.display.set_caption(game_screen.caption)
    play_button = Button(game_screen, screen, "Play")
    
    stats = GameStats()
    clock = pygame.time.Clock()
    player = Player(screen)
    
    while True:
        functions.check_events(game_screen, screen, player, stats, play_button)
        if stats.game_active:
            player.update()
        else:
            sys.exit()
            
        functions.update_screen(game_screen, screen, player, clock, stats, play_button)
        
run_game()