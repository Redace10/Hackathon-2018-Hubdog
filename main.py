import pygame
import os

from display import Display

WIDTH = 800
HEIGHT = 600

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    # initialize player
    # player = Player(135, 115, 5, 0)

    # initialize display
    self.display = Display(pygame, 135, 115, WIDTH, HEIGHT)

    
    self.clock = pygame.time.Clock()
    self.keepPlaying = True

game = Game()
while game.keepPlaying: