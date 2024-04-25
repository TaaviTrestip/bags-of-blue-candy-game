import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.music = pygame.mixer.music.load('Theme.mp3')

    def play(self):
        pygame.mixer.music.play(-1)
