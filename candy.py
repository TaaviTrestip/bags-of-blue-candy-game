import pygame
import random

class Candy(pygame.sprite.Sprite):
    
    def __init__(self, screen, game_screen, stats):
        super(Candy, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.candy_orig = pygame.image.load("game_textures/Blue_crystal_candy.png").convert_alpha()
        self.candy = pygame.transform.scale(self.candy_orig, (50, 60))
        self.rect = self.candy.get_rect()
        
        self.rect = self.candy.get_rect(
                center=(
                    random.randint(game_screen.screen_height + 20, game_screen.screen_width + 250),
                    random.randint(0, game_screen.screen_height),
                )
            )
        
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
        
        
    def blit_me(self):
        self.screen.blit(self.candy, self.rect)