import pygame
from pygame import mixer
def play_sound(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

play_sound(Users/Fuso/Music.mp3,stop)