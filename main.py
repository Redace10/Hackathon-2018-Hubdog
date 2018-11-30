import pygame
import os
import random
import numpy as np

from hp import Hp
from player import Player
from display import Display
from box import Box
from homeBot import HomeBot

WIDTH = 800
HEIGHT = 600

BOX_WIDTH = 60
BOX_HEIGHT = 60
BOX_DIST = 10
NORMAL_DECREASING_RATE = 5

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    # initialize player
    player = Player(135, 115, 5, 0)

    # initialize Hp bar
    self.hp = Hp(760) # the full health is 760

    # initialize Home robot
    self.homeBot = HomeBot()

    # initialize display
    self.display = Display(pygame, 135, 115, WIDTH, HEIGHT, BOX_WIDTH, BOX_HEIGHT)

    self.initializeBoxes()

    self.clock = pygame.time.Clock()
    self.keepPlaying = True

  def spawnBox(self):
    for i in range(self.boxSpawnRate):
      size = np.random.choice(['B', 'S'], 1, replace=False, p=[self.bigBoxChance, self.smallBoxChance])[0]
      logo = random.randint(0, len(self.banks[size]) - 1)
      while True:
        randX = random.randint(10, WIDTH - 10 - BOX_WIDTH)
        randY = random.randint(10, HEIGHT - 10 - BOX_HEIGHT)
        rect = pygame.Rect(randX, randY, BOX_WIDTH, BOX_HEIGHT)
        box_rects = list(map(lambda b: b.getRect(), self.boxes))
        if (rect.collidelist(box_rects) < 0):
          self.boxes.append(Box(size, self.banks[size][logo], rect))
          break

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.keepPlaying = False
      if event.type == self.boxSpawnEvent:
        self.spawnBox()

  def initializeBoxes(self):
    bigBanks = ['amex', 'bmo', 'chase', 'td', 'wellsFargo']
    smallBanks = ['fido', 'tangerine', 'telstra']
    self.banks = {'B':bigBanks, 'S':smallBanks}
    self.boxes = []
    # i.e spawn {boxSpawnRate} boxes every {boxSpawnFrequency} seconds
    self.boxSpawnRate = 3
    self.boxSpawnFrequency = 5000
    self.boxSpawnEvent = pygame.USEREVENT + 1
    self.bigBoxChance = 0.2
    self.smallBoxChance = 0.8

    #self.boxes.append(Box('B', 'bmo', (40, 40, BOX_WIDTH, BOX_HEIGHT)))
    pygame.time.set_timer(self.boxSpawnEvent, self.boxSpawnFrequency)


  def __del__(self):
    pygame.quit()

game = Game()
while game.keepPlaying:
  game.display.drawBoxes(game.boxes)
  game.display.drawHp(game.hp, game.hp.health) # we going to have some function to decrease the health
  game.display.drawHomeBot(game.homeBot)
  game.hp.updateHealth(NORMAL_DECREASING_RATE)
  pygame.display.update()
  game.handleEvents()