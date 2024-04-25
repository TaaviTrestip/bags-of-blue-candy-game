import pygame
import sys
import threading
import game_functions as functions
import os
from music import Music
from math import *
from game_window import GameWindow
from button import Button
from player import Player
from candy import Candy
from enemy import Enemy
from game_stats import GameStats
from end_screen import EndScreen



def run_game():
    pygame.init()
    game_screen = GameWindow()

    screen = pygame.display.set_mode([game_screen.screen_width, game_screen.screen_height])
    pygame.display.set_caption(game_screen.caption)
    play_button = Button(game_screen, screen, "Play")
    
    stats = GameStats()
    clock = pygame.time.Clock()
    player = Player(screen)
    
    candies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    end_screen = EndScreen(screen, stats, play_button)

    my_music = Music()
    my_music.play()

    while True:
        functions.check_events(game_screen, screen, player, candies, stats, play_button, enemies, )
        if stats.game_active:
            player.update()
            functions.update_candies(player, candies, stats, game_screen)
            candies.update()
            functions.update_enemies(player, enemies, stats, game_screen, screen, play_button)
            enemies.update()
        else:
            functions.update_enemies(player, enemies, stats, game_screen, screen, play_button)
        functions.update_screen(game_screen, screen, player, candies, clock, stats, play_button, enemies)


        if stats.game_end:
            end_screen.draw(stats)
        
run_game()