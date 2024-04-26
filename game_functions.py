import sys
import pygame
from candy import Candy
from enemy import Enemy
from game_stats import GameStats
from end_screen import EndScreen

spawn_rates = GameStats()

pygame.init()
ADDCANDY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCANDY, spawn_rates.candy_spawn_rate)

ADDENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, spawn_rates.enemy_spawn_rate)

def check_events(game_screen, screen, player, candies, stats, play_button, enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(stats)
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
        elif event.type == ADDENEMY:
            create_enemy(game_screen, screen, enemies, stats)
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
        stats.score += 1
        if stats.score > stats.highscore:
            stats.highscore = stats.score
            
        if (int(stats.score / stats.checker_idk)) > stats.counter:
            stats.level += 1
            stats.counter += 1
            if stats.enemy_spawn_rate > 100:
                stats.enemy_spawn_rate -= 100
                pygame.time.set_timer(ADDENEMY, stats.enemy_spawn_rate)
            if stats.enemy_speed < 15:
                stats.enemy_speed += 0.25
        hitted_candy.kill()


def create_enemy(game_screen, screen, enemies, stats):
    new_enemy = Enemy(screen, game_screen, stats)
    enemies.add(new_enemy)


import pygame

def update_enemies(player, enemies, stats, game_screen, screen, play_button):
    hitted_enemy = pygame.sprite.spritecollideany(player, enemies)
    if hitted_enemy is not None and not stats.game_end:
        pygame.mixer.music.stop()
        
        stats.game_active = False
        stats.game_end = True

        pygame.mixer.Sound("End.mp3").play()
        save_score(stats)
        
def update_screen(game_screen, screen, player, candies, clock, stats, play_button, enemies):
    screen.fill(game_screen.background)
    player.blit_me()
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Score: " + str(stats.score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    if len(candies) > 0:
        for candy in candies:
            candy.blit_me()
            
    if len(enemies) > 0:
        for enemy in enemies:
            enemy.blit_me()
            
    clock.tick(30)
    if not stats.game_active:
        if not stats.game_end:
            picture = pygame.image.load("game_textures/Start_screen.jpg").convert_alpha()
            picture = pygame.transform.scale(picture, (game_screen.screen_width, game_screen.screen_height))
            screen.blit(picture, (0, 0))
            play_button.draw_button()
        else:
            screen.fill(game_screen.background)
            end_screen = EndScreen(screen, stats, play_button)
            end_screen.draw(stats)
            pygame.display.flip()

    pygame.display.flip()

def save_score(stats):
    stats.highscore_update(stats.score)