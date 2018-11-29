import pygame
import os

from display import Display
from player import Player

WIDTH = 800
HEIGHT = 600

class Game:
  def __init__(self):
    # sets basic game features

    # display screen in the middle
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    # initialize display
    self.display = Display(pygame, 135, 115, WIDTH, HEIGHT)
    
    # initialize player
    self.player = Player(135, 115, 5, 0)
    
    self.clock = pygame.time.Clock()
    self.keepPlaying = True


game = Game()

while game.keepPlaying:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game.keepPlaying = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.setDirectionX(0)
        moveLeft = True
      if event.key == pygame.K_RIGHT:
        player.setDirectionX(1)
        moveRight = True
      if event.key == pygame.K_UP:
        moveUp = True
      if event.key == pygame.K_DOWN:
        moveDown = True
      if event.key == pygame.K_SPACE:
        player.attack(game_border)
      
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        moveLeft = False
      if event.key == pygame.K_RIGHT:
        moveRight = False
      if event.key == pygame.K_UP:
        moveUp = False
      if event.key == pygame.K_DOWN:
        moveDown = False
  
  # Walking animation
  index = 0
  face = 0
  dog = game.display.dogImages[face][index//10]
  game.display.updateDog(dog, game.player.getRect())

  pygame.display.update()
  game.clock.tick(60)

pygame.quit()
quit()
