import pygame
import time

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.music.load("Theme.mp3")

    def play(self):
        pygame.mixer.music.play()

def play_music():
    music_player = Music()
    
    while True:
        if not pygame.mixer.music.get_busy():
            music_player.play()
        
        time.sleep(0.1)
