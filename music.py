import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    file_path = "Theme.mp3"
    play_audio(file_path)
    
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)