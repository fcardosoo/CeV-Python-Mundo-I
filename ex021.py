# Abrir e reproduzir um audio mp3

import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("ex021.wav")
pygame.mixer.music.play()
time.sleep(360)

