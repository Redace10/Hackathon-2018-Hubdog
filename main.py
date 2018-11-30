import pygame
import os
import random
# import numpy as np

from display import Display
from player import Player
from box import Box
from leaderboard import Leaderboard

WIDTH = 1000
HEIGHT = 800

BOX_WIDTH = 60
BOX_HEIGHT = 60
BOX_DIST = 10
CHEQUE_WIDTH = 30
CHEQUE_HEIGHT = 15
DOC_WIDTH = 20
DOC_HEIGHT = 40
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 120

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    # pygame.mixer.music.load("The Marching Pirate Spy.mp3")
    # pygame.mixer.music.play(-1, 0)

    # initialize display
    self.display = Display(pygame, PLAYER_WIDTH, PLAYER_HEIGHT, WIDTH, HEIGHT, BOX_WIDTH, BOX_HEIGHT)

    self.initializeBoxes()
    self.docs = []

    # initialize player
    self.player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, 5, 0)
    self.player.setRect(self.display.dogImages[0][0].get_rect())
    self.leaderboard = Leaderboard()

    self.clock = pygame.time.Clock()
    self.keepPlaying = True

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.keepPlaying = False

      # if event.type == self.boxSpawnEvent:
      #   self.spawnBox()

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
        self.docs += b.openBox()

  def updateDocuments(self):
    for d in self.docs:
      if d.getSpread() == True:
        d.spread()
      elif self.player.getRect().colliderect(d.getRect()):
        self.docs.remove(d)

  # def spawnBox(self):
  #   for i in range(self.boxSpawnRate):
  #     size = np.random.choice(['B', 'S'], 1, replace=False, p=[self.bigBoxChance, self.smallBoxChance])[0]
  #     logo = random.randint(0, len(self.banks[size]) - 1)
  #     while True:
  #       randX = random.randint(10, WIDTH - 10 - BOX_WIDTH)
  #       randY = random.randint(10, HEIGHT - 10 - BOX_HEIGHT)
  #       rect = pygame.Rect(randX, randY, BOX_WIDTH, BOX_HEIGHT)
  #       box_rects = list(map(lambda b: b.getRect(), self.boxes))
  #       if (rect.collidelist(box_rects) < 0):
  #         self.boxes.append(Box(size, self.banks[size][logo], rect, self.boxDuration))
  #         break

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
    pygame.draw.rect(self.display.gameDisplay, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
    # self.display.drawBoxes(self.boxes)
    # self.display.drawDocuments(self.docs)
    # pygame.draw.rect(self.display.gameDisplay, (0, 0, 255), self.player.getRect())
    # self.display.drawDog(self.player)
    self.display.showLeaderboard(self.leaderboard)
    pygame.display.update()

  def __del__(self):
    pygame.quit()

game = Game()
while game.keepPlaying:
  # game.updateBoxes()
  # game.updateDocuments()

  game.updateDisplay()
  
  game.handleEvents()
  
  game.clock.tick(30)
  

quit()
