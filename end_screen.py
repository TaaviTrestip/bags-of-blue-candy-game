import pygame
import os

class EndScreen:
    def __init__(self, screen, stats, play_button):
        self.screen = screen
        self.stats = stats
        self.play_button = play_button

        self.end_screen_image = pygame.image.load("game_textures/End_screen.png").convert_alpha()
        self.end_screen_image = pygame.transform.scale(self.end_screen_image, (screen.get_width(), screen.get_height()))
        self.end_screen_rect = self.end_screen_image.get_rect()

        self.font = pygame.font.SysFont(None, 48)
        self.score_text = self.font.render("Your Score: " + str(stats.score), True, (255, 255, 255))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = self.screen.get_rect().center

        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0
        return high_score

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def draw(self, stats):
        self.screen.blit(self.end_screen_image, self.end_screen_rect)

        if stats.score > self.high_score:
            self.high_score = stats.score
            self.save_high_score()

        score_text = "Your Score: " + str(stats.score)
        high_score_text = "Highest Score: " + str(self.high_score)
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        high_score_surface = self.font.render(high_score_text, True, (255, 255, 255))

        score_rect = score_surface.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 100 ))
        high_score_rect = high_score_surface.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 150 ))

        self.screen.blit(score_surface, score_rect)
        self.screen.blit(high_score_surface, high_score_rect)
