import pygame
import random

class Candy(pygame.sprite.Sprite):
    
    def __init__(self, screen, game_screen, stats):
        super(Candy, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.candy = pygame.Surface((50, 50))
        self.candy.fill((0, 255, 255))
        self.rect = self.candy.get_rect()
        
        self.rect = self.candy.get_rect(
                center=(
                    random.randint(game_screen.screen_height + 20, game_screen.screen_width + 100),
                    random.randint(0, game_screen.screen_height),
                )
            )
        
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
        
        
    def blit_me(self):
        self.screen.blit(self.candy, self.rect)