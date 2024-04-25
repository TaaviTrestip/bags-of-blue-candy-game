import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, screen, game_screen, stats):
        super(Enemy, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.enemy_orig = pygame.image.load("game_textures/Agent_hank.png").convert_alpha()
        self.enemy = pygame.transform.scale(self.enemy_orig, (60, 80))
        self.rect = self.enemy.get_rect()
        
        self.rect = self.enemy.get_rect(
                center=(
                    random.randint(game_screen.screen_height + 20, game_screen.screen_width + 500),
                    random.randint(0, game_screen.screen_height),
                )
            )
        
        self.speed = stats.enemy_speed
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
        
    def blit_me(self):
        self.screen.blit(self.enemy, self.rect)