import sys
import pygame
from candy import Candy

pygame.init()
ADDCANDY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCANDY, 250)

def check_events(game_screen, screen, player, candies, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDCANDY:
            create_candy(game_screen, screen, candies, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


def create_candy(game_screen, screen, candies, stats):
    new_candy = Candy(screen, game_screen, stats)
    candies.add(new_candy)


def update_candies(player, candies, stats, game_screen):
    hitted_candy = pygame.sprite.spritecollideany(player, candies)
    if hitted_candy != None:
        hitted_candy.kill()

        
def update_screen(game_screen, screen, player, candies, clock, stats, play_button):
    screen.fill(game_screen.background)
    player.blit_me()
    if len(candies) > 0:
        for candy in candies:
            candy.blit_me()
    clock.tick(30)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()