import pygame
import time

class Music:
    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()
        # Load the music file
        self.music = pygame.mixer.music.load("theme.mp3")

    def play(self):
        # Play the music
        pygame.mixer.music.play()

def play_music():
    # Create an instance of the Music class
    music_player = Music()
    
    # Main loop to keep music playing
    while True:
        # Check if the music has finished playing
        if not pygame.mixer.music.get_busy():
            # Replay the music
            music_player.play()
        
        # Add a small delay to avoid hogging the CPU
        time.sleep(0.1)
