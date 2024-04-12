import pygame
from screen import Screen

pygame.init()
game_screen = Screen()


screen = pygame.display.set_mode([game_screen.screen_width, game_screen.screen_height])
pygame.display.set_caption(game_screen.caption)

running = True
while running:
    screen.fill(game_screen.background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    
pygame.quit()