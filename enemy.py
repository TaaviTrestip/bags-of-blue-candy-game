import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, screen, game_screen, stats):
        super(Enemy, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.enemy = pygame.Surface((75, 75))
        self.enemy.fill((255, 0, 0))
        self.rect = self.enemy.get_rect()
        
        self.rect = self.enemy.get_rect(
                center=(
                    random.randint(game_screen.screen_height + 20, game_screen.screen_width + 700),
                    random.randint(0, game_screen.screen_height),
                )
            )
        
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
        
        
    def blit_me(self):
        self.screen.blit(self.enemy, self.rect)