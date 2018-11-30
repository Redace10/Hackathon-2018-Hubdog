import pygame
import os
import random
import numpy as np
import GLOBAL

from hp import Hp
from player import Player
from display import Display
from player import Player
from box import Box
from homeBot import HomeBot

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    # initialize Hp bar
    self.hp = Hp(GLOBAL.HOMEBOT_HEALTH) # the full health is 760

    # initialize Home robot
    self.homeBot = HomeBot()

    # initialize display
    self.display = Display(pygame)

    self.initializeBoxes()
    self.docs = []
    self.docDuration = 7000

    # initialize player
    self.player = Player(GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT, GLOBAL.PLAYER_SPEED, 0)
    self.player.setRect(self.display.dogImages[0][0].get_rect())

    self.clock = pygame.time.Clock()
    self.keepPlaying = True

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.keepPlaying = False

      if event.type == self.boxSpawnEvent:
        self.spawnBox()

      if event.type == pygame.KEYDOWN and game.player.getAttack() == False:
        if event.key == pygame.K_LEFT:
          game.player.setMoveLeft(True)
        if event.key == pygame.K_RIGHT:
          game.player.setMoveRight(True)
        if event.key == pygame.K_UP:
          game.player.setMoveUp(True)
        if event.key == pygame.K_DOWN:
          game.player.setMoveDown(True)
        if event.key == pygame.K_SPACE:
          game.player.setAttack(True)
        
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          game.player.resetMoveX()
          game.player.setMoveLeft(False)
        if event.key == pygame.K_RIGHT:
          game.player.resetMoveX()
          game.player.setMoveRight(False)
        if event.key == pygame.K_UP:
          game.player.resetMoveY()
          game.player.setMoveUp(False)
        if event.key == pygame.K_DOWN:
          game.player.resetMoveY()
          game.player.setMoveDown(False)

    if (game.player.getMoveLeft()):
      game.player.moveX(-1)
    if (game.player.getMoveRight()):
      game.player.moveX(1)
    if (game.player.getMoveUp()):
      game.player.moveY(-1)
    if (game.player.getMoveDown()):
      game.player.moveY(1)

  def updateBoxes(self):
    for b in self.boxes:
      if b.shouldHide(pygame.time.get_ticks()):
        self.boxes.remove(b)
      if self.player.getAttack() and self.player.getRect().colliderect(b.getRect()):
        docs = b.openBox()
        for d in docs:
          d.setDuration(pygame.time.get_ticks(), self.docDuration)
          self.docs.append(d)

  def updateDocuments(self):
    for d in self.docs:
      docCollected = False
      if d.getSpread() == True:
        d.spread()
      elif self.player.getRect().colliderect(d.getRect()) and docCollected == False:
        self.player.collectDoc()
        self.docs.remove(d)
        docCollected = True
      if d.shouldHide(pygame.time.get_ticks()):
        self.docs.remove(d)

  def spawnBox(self):
    for i in range(self.boxSpawnRate):
      size = np.random.choice(['B', 'S'], 1, replace=False, p=[self.bigBoxChance, self.smallBoxChance])[0]
      logo = random.randint(0, len(self.banks[size]) - 1)
      while True:
        randX = random.randint(30, GLOBAL.MAP_WIDTH - 30 - GLOBAL.BOX_WIDTH)
        randY = random.randint(30, GLOBAL.MAP_HEIGHT - 80 - GLOBAL.BOX_HEIGHT)
        rect = pygame.Rect(randX, randY, GLOBAL.BOX_WIDTH, GLOBAL.BOX_HEIGHT)
        box_rects = list(map(lambda b: b.getRect(), self.boxes))
        if (rect.collidelist(box_rects) < 0):
          self.boxes.append(Box(size, self.banks[size][logo], rect, self.boxDuration))
          break

  def initializeBoxes(self):
    bigBanks = ['amex', 'bmo', 'chase', 'td', 'wellsFargo']
    smallBanks = ['fido', 'tangerine', 'telstra']
    self.banks = {'B':bigBanks, 'S':smallBanks}
    self.boxes = []
    # i.e spawn {boxSpawnRate} boxes every {boxSpawnFrequency} seconds
    self.boxSpawnRate = 1
    self.boxSpawnFrequency = 2000
    self.boxSpawnEvent = pygame.USEREVENT + 1
    self.bigBoxChance = 0.2
    self.smallBoxChance = 0.8
    self.boxDuration = 5000

    #self.boxes.append(Box('B', 'bmo', (40, 40, BOX_WIDTH, BOX_HEIGHT)))
    pygame.time.set_timer(self.boxSpawnEvent, self.boxSpawnFrequency)

  def updateDisplay(self):
    pygame.draw.rect(self.display.gameDisplay, (0, 0, 0), (0, 0, GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))
    self.display.drawBoxes(self.boxes)
    self.display.drawDocuments(self.docs)
    #pygame.draw.rect(self.display.gameDisplay, (0, 0, 255), self.player.getRect())
    self.display.drawDog(self.player)
    collectedDocs = 'Fetched docs:%d'% self.player.getCollectedDocs()
    self.display.drawWord(collectedDocs, 160, 20, [(255, 255, 0), (0, 0, 255)])
    self.display.drawHp(self.hp, self.hp.health) # we going to have some function to decrease the health
    #homeBot draw
    self.display.drawHomeBot(self.homeBot)
    #health bar draw
    self.hp.updateHealth(GLOBAL.NORMAL_DECREASING_RATE)
    pygame.display.update()

  def __del__(self):
    pygame.quit()

game = Game()
while game.keepPlaying:
  game.updateBoxes()
  game.updateDocuments()

  game.updateDisplay()
  
  game.handleEvents()

  game.clock.tick(30)

quit()
