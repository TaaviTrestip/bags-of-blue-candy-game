import pygame
import random

class Candy(pygame.sprite.Sprite):
    def __init__(self, screen, game_screen, stats):
        super(Bubble, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.player = pygame.Surface((100, 100))
        self.player.fill((0, 255, 255))
        self.rect = self.player.get_rect()
        
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
        
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)