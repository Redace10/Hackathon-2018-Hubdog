import pygame
import os

from display import Display
from player import Player
from box import Box

WIDTH = 800
HEIGHT = 600

BOX_WIDTH = 70
BOX_HEIGHT = 70

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    

    # initialize display
    self.display = Display(pygame, 135, 115, WIDTH, HEIGHT, BOX_WIDTH, BOX_HEIGHT)

    self.initializeBoxes()

    # initialize player
    self.player = Player(135, 115, 5, 0)
    self.player.setRect(self.display.dogImages[0][0].get_rect())

    self.clock = pygame.time.Clock()
    self.keepPlaying = True

  def spawnBox(self):
    for i in range(self.boxSpawnRate):
      print('spawnBox')

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.keepPlaying = False
      # if event.type == self.boxSpawnEvent:
      #   self.spawnBox()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          game.player.moveX(-1)
          game.player.setMoveLeft = True
        if event.key == pygame.K_RIGHT:
          game.player.moveX(1)
          game.player.setMoveRight = True
        if event.key == pygame.K_UP:
          game.player.moveY(-1)
          game.player.setMoveUp = True
        if event.key == pygame.K_DOWN:
          game.player.moveY(1)
          game.player.setMoveDown = True
        
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          game.player.resetMoveX()
          game.player.setMoveLeft = False
        if event.key == pygame.K_RIGHT:
          game.player.resetMoveX()
          game.player.setMoveRight = False
        if event.key == pygame.K_UP:
          game.player.resetMoveY()
          game.player.setMoveUp = False
        if event.key == pygame.K_DOWN:
          game.player.resetMoveY()
          game.player.setMoveDown = False

  def initializeBoxes(self):
     # initialize boxes
    bigBanks = ['amex', 'bmo', 'chase', 'td', 'wellsFargo']
    smallBanks = ['fido', 'tangerine', 'telstra']
    self.banks = {'B':bigBanks, 'S':smallBanks}
    self.boxes = []
    # i.e spawn {boxSpawnRate} boxes every {boxSpawnFrequency} seconds
    self.boxSpawnRate = 3
    self.boxSpawnFrequency = 5000
    self.boxSpawnEvent = pygame.USEREVENT + 1
    self.boxes.append(Box('B', 'bmo', (200, 50, BOX_WIDTH, BOX_HEIGHT)))
    pygame.time.set_timer(self.boxSpawnEvent, self.boxSpawnFrequency)

  def __del__(self):
    pygame.quit()

game = Game()
while game.keepPlaying:
  game.handleEvents()
  # game.display.drawBoxes(game.boxes)


  # # Player movement
  # if (game.player.getMoveRight):
  #   game.player.moveX(1)
  # if (game.player.getMoveLeft):
  #   game.player.moveX(-1)
  # if (game.player.getMoveUp):
  #   game.player.moveY(-1)
  # if (game.player.getMoveDown):
  #   game.player.moveY(1)
  game.player.move()
  game.display.drawDog(game.player)
  pygame.display.update()