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
from leaderboard import Leaderboard

from vkeyboard import VKeyboardRenderer
from vkeyboard import VKeyboardLayout
from vkeyboard import VKeyboard
import vkeyboard
from homeBot import HomeBot
from competitor import Competitor
from bryan import Bryan

class Game:
  def __init__(self):
    # sets basic game features
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # plays background song repeatedly
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/backgroundMusic.wav")
    pygame.mixer.music.play(-1, 0.0)

    self.beatEnemySound = pygame.mixer.Sound('assets/sounds/beatEnemy.wav')
    self.boxBreakSound = pygame.mixer.Sound('assets/sounds/boxBreak.wav')
    self.boxAppearSound = pygame.mixer.Sound('assets/sounds/boxAppearing.wav')
    self.docCollectSound = pygame.mixer.Sound('assets/sounds/docFetched.wav')
    self.bryanSound = pygame.mixer.Sound('assets/sounds/codeReviewBryanSong.wav')
    self.playerDamageSound = pygame.mixer.Sound('assets/sounds/playerDamage.wav')
    # initialize Hp bar
    self.hp = Hp(GLOBAL.HOMEBOT_HEALTH) # the full health is 760

    # initialize Home robot
    self.homeBot = HomeBot()

    # initialize display
    self.display = Display(pygame)

    self.initializeBoxes()
    self.docs = []
    self.docDuration = 7000
    self.initializeCompetitors()

    # initialize player
    self.player = Player(GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT, GLOBAL.PLAYER_SPEED, 0)
    self.diff = 0
    self.player.setRect(self.display.dogImages[0][0].get_rect())
    self.leaderboard = Leaderboard()
    self.playerCooldownEvent = pygame.USEREVENT + 3
    self.playerBryanEvent = pygame.USEREVENT + 4
    pygame.time.set_timer(self.playerBryanEvent, GLOBAL.BRYAN_COOLDOWN)

    # initialize jotstick
    pygame.joystick.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()


    self.clock = pygame.time.Clock()
    self.keepPlaying = True
    self.bryans = []

    self.clock = pygame.time.Clock()
    self.keepPlaying = True
    self.postGame = False

    # Initializes and activates vkeyboard
    self.renderer = VKeyboardRenderer(
      # Key font.
      pygame.font.Font('assets/PressStart2P.ttf', 20),
      # Keyboard background color.
      (50, 50, 50),
      # Key background color (one per state, 0 for released, 1 for pressed).
      ((255, 255, 255), (0, 0, 0)),
      # Text color for key (one per state as for the key background).
      ((0, 0, 0), (255, 255, 255)),
      # (Optional) special key background color.
      ((255, 255, 255), (0, 0, 0)),
    )

    self.increaseDifficultyEvent = pygame.USEREVENT + 5
    pygame.time.set_timer(self.increaseDifficultyEvent, GLOBAL.INCREASE_DIFF_TIME)

    self.layout = VKeyboardLayout(VKeyboardLayout.AZERTY, allow_uppercase=False, key_size=100, allow_special_chars=False)
    self.keyboard = VKeyboard(self.display.gameDisplay, self.consumer, self.layout, renderer=self.renderer)
    self.keyboard.enable()
    self.text = ""
    self.boxAppearSound = pygame.mixer.Sound('assets/sounds/boxAppearing.wav')

  def reset(self):
    pygame.draw.rect(game.display.gameDisplay, (0, 0, 100), (0, 0, GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))

    # initialize Hp bar
    self.hp = Hp(GLOBAL.HOMEBOT_HEALTH) # the full health is 760

    # initialize Home robot
    self.homeBot = HomeBot()

    self.initializeBoxes()
    self.docs = []
    self.docDuration = 7000
    self.initializeCompetitors()

    # initialize player
    self.player = Player(GLOBAL.PLAYER_WIDTH, GLOBAL.PLAYER_HEIGHT, GLOBAL.PLAYER_SPEED, 0)
    self.player.setRect(self.display.dogImages[0][0].get_rect())
    self.leaderboard = Leaderboard()
    self.playerCooldownEvent = pygame.USEREVENT + 3
    pygame.time.set_timer(self.playerBryanEvent, GLOBAL.BRYAN_COOLDOWN)

    self.bryans = []

    self.clock = pygame.time.Clock()
    self.keepPlaying = True
    self.postGame = False

    # Initializes and activates vkeyboard
    self.renderer = VKeyboardRenderer(
      # Key font.
      pygame.font.Font('assets/PressStart2P.ttf', 20),
      # Keyboard background color.
      (50, 50, 50),
      # Key background color (one per state, 0 for released, 1 for pressed).
      ((255, 255, 255), (0, 0, 0)),
      # Text color for key (one per state as for the key background).
      ((0, 0, 0), (255, 255, 255)),
      # (Optional) special key background color.
      ((255, 255, 255), (0, 0, 0)),
    )
    self.diff = 0
    pygame.time.set_timer(self.increaseDifficultyEvent, GLOBAL.INCREASE_DIFF_TIME)


    self.layout = VKeyboardLayout(VKeyboardLayout.AZERTY, allow_uppercase=False, key_size=100, allow_special_chars=False)
    self.keyboard = VKeyboard(self.display.gameDisplay, self.consumer, self.layout, renderer=self.renderer)
    self.keyboard.enable()
    self.text = ""

  def joystickMove(self, axis1, axis0):
    if axis1 >= 0.8 or axis1 <= -0.8 or axis0 >= 0.8 or axis0 <= -0.8:
      return True
    else:
      return False
      
  def consumer(self, text):
    self.text = text

  def handleEvents(self):
    axis1 = self.joystick.get_axis( 1 )
    axis0 = self.joystick.get_axis( 0 )
    buttonA = self.joystick.get_button( 0 )
    buttonB = self.joystick.get_button( 1 )
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.keepPlaying = False
        self.postGame = False

      if event.type == self.boxSpawnEvent:
        self.spawnBox()
      if event.type == self.compSpawnEvent:
        self.spawnCompetitors()
      if event.type == self.playerCooldownEvent:
        self.player.canAttack(True)
        pygame.time.set_timer(self.playerCooldownEvent, 0)
      if event.type == self.playerBryanEvent:
        self.player.giveBryan()
        if self.player.hasPowerup():
          pygame.time.set_timer(self.playerBryanEvent, 0)
      if event.type == self.increaseDifficultyEvent:
        self.diff += 0.1

      if buttonA == 1 and self.postGame == True and self.display.showKeyboard == False:
          self.reset()
          self.leaderboard.setReadLeaderboard(False)
          vkeyboard.FINISHED = False
          self.display.inserted = False
      if buttonB == 1 and self.postGame == True and self.display.showKeyboard == False:
          self.postGame = False
      # move left -> axis0 <= -0.8
      # move right -> axis0 >= 0.8
      # move up -> axis1 <= -0.8
      # move down -> axis1 >= 0.8
      if self.joystickMove(axis1, axis0) and self.player.getAttack() == False:
        if axis0 <= -0.8 and axis1 <= -0.8:
          self.player.setMoveUp(True)
          self.player.setMoveLeft(True)
          self.player.setMoveRight(False)
          self.player.setMoveDown(False)
          GLOBAL.CURRENT_DIR = 'LEFTUP'
        elif axis0 >= 0.8 and axis1 <= -0.8:
          self.player.setMoveUp(True)
          self.player.setMoveRight(True)
          self.player.setMoveLeft(False)
          self.player.setMoveDown(False)
          GLOBAL.CURRENT_DIR = 'RIGHTUP'
        elif axis0 <= -0.8 and axis1 >= 0.8:
          self.player.setMoveLeft(True)
          self.player.setMoveDown(True)
          self.player.setMoveRight(False)
          self.player.setMoveUp(False)
          GLOBAL.CURRENT_DIR = 'LEFTDOWN'
        elif axis0 >= 0.8 and axis1 >= 0.8:
          self.player.setMoveRight(True)
          self.player.setMoveDown(True)
          self.player.setMoveLeft(False)
          self.player.setMoveUp(False)
          GLOBAL.CURRENT_DIR = 'RIGHTDOWN'
        elif axis0 <= -0.8:
          self.player.setMoveLeft(True)
          self.player.setMoveRight(False)
          self.player.setMoveUp(False)
          self.player.setMoveDown(False)
          GLOBAL.CURRENT_DIR = 'LEFT'
        elif axis0 >= 0.8:
          self.player.setMoveRight(True)
          self.player.setMoveLeft(False)
          self.player.setMoveUp(False)
          self.player.setMoveDown(False)
          GLOBAL.CURRENT_DIR = 'RIGHT'
        elif axis1 <= -0.8:
          self.player.setMoveUp(True)
          self.player.setMoveDown(False)
          self.player.setMoveLeft(False)
          self.player.setMoveRight(False)
          GLOBAL.CURRENT_DIR = 'UP'
        elif axis1 >= 0.8:
          self.player.setMoveDown(True)
          self.player.setMoveUp(False)
          self.player.setMoveLeft(False)
          self.player.setMoveRight(False)
          GLOBAL.CURRENT_DIR = 'DOWN'
      else:
        if GLOBAL.CURRENT_DIR == 'LEFTUP':
          self.player.resetMoveX()
          self.player.setMoveLeft(False)
          self.player.resetMoveY()
          self.player.setMoveUp(False)
        elif GLOBAL.CURRENT_DIR == 'RIGHTUP':
          self.player.resetMoveX()
          self.player.setMoveRight(False)
          self.player.resetMoveY()
          self.player.setMoveUp(False)
        elif GLOBAL.CURRENT_DIR == 'LEFTDOWN':
          self.player.resetMoveX()
          self.player.setMoveLeft(False)
          self.player.resetMoveY()
          self.player.setMoveDown(False)
        elif GLOBAL.CURRENT_DIR == 'RIGHTDOWN':
          self.player.resetMoveX()
          self.player.setMoveRight(False)
          self.player.resetMoveY()
          self.player.setMoveDown(False)
        elif GLOBAL.CURRENT_DIR == 'LEFT' or GLOBAL.CURRENT_DIR == 'RIGHT':
          self.player.resetMoveX()
          self.player.setMoveRight(False)
        elif GLOBAL.CURRENT_DIR == 'UP' or GLOBAL.CURRENT_DIR == 'DOWN':
          self.player.resetMoveY()
          self.player.setMoveUp(False)
        elif GLOBAL.CURRENT_DIR == None:
          self.player.resetMoveX()
          self.player.setMoveRight(False)
          self.player.setMoveLeft(False)
          self.player.setMoveUp(False)
          self.player.resetMoveY()
          self.player.setMoveDown(False)
        GLOBAL.CURRENT_DIR = None
      if buttonA == 1:
        self.player.setAttack(True)
      #if buttonA == 0:
        #self.player.setAttack(False)
      if buttonB == 1:
        if self.player.hasPowerup():
          self.initiateBryan()
          self.bryanSound.play()
          self.player.removePowerup()
          pygame.time.set_timer(self.playerBryanEvent, GLOBAL.BRYAN_COOLDOWN)
      if (self.display.showKeyboard):
        self.keyboard.on_event(event, axis1, axis0, buttonA)

    if (self.player.getMoveLeft()):
      self.player.moveX(-1)
    if (game.player.getMoveRight()):
      self.player.moveX(1)
    if (game.player.getMoveUp()):
      self.player.moveY(-1)
    if (game.player.getMoveDown()):
      self.player.moveY(1)

  def updateBoxes(self):
    for b in self.boxes:
      if b.shouldHide(pygame.time.get_ticks()):
        self.boxes.remove(b)
        self.boxBreakSound.play()
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
        self.docCollectSound.play()
      elif d.shouldHide(pygame.time.get_ticks(),
      list(map(lambda c: c.getRect(), self.comps)),
      list(map(lambda b: b.getRect(), self.bryans))):
        self.docs.remove(d),

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
      self.boxAppearSound.play()

  def initializeBoxes(self):
    bigBanks = ['amex', 'bmo', 'chase', 'td', 'wellsFargo']
    smallBanks = ['fido', 'tangerine', 'telstra']
    self.banks = {'B':bigBanks, 'S':smallBanks}
    self.boxes = []
    # i.e spawn {boxSpawnRate} boxes every {boxSpawnFrequency} seconds
    self.boxSpawnRate = 1
    self.boxSpawnFrequency = 2000
    self.boxSpawnEvent = pygame.USEREVENT + 1
    self.bigBoxChance = 0.3
    self.smallBoxChance = 0.7
    self.boxDuration = 5000

    #self.boxes.append(Box('B', 'bmo', (40, 40, BOX_WIDTH, BOX_HEIGHT)))
    pygame.time.set_timer(self.boxSpawnEvent, self.boxSpawnFrequency)

  def initializeCompetitors(self):
    self.comps = []
    self.compSpawnRate = 1
    self.compSpawnFrequency = 3000
    self.compSpawnEvent = pygame.USEREVENT + 2
    pygame.time.set_timer(self.compSpawnEvent, self.compSpawnFrequency)

  def spawnCompetitors(self):
    for i in range(self.compSpawnRate):
      loc = random.choice(GLOBAL.COMP_SPAWNS)
      rect = pygame.Rect(loc[0], loc[1], GLOBAL.COMP_WIDTH, GLOBAL.COMP_HEIGHT)
      self.comps.append(Competitor('veryfi', rect, GLOBAL.COMP_SPEED))

  def updateCompetitors(self):
    for c in self.comps:
      if c.selectTarget(self.docs, self.player):
        c.moveToTarget()
      if self.player.getAttack() and self.player.getRect().colliderect(c.getRect()):
        self.comps.remove(c)
        self.beatEnemySound.play()
      elif self.player.getRect().colliderect(c.getRect()):
        self.player.getHit()
        self.playerDamageSound.play()

  def updateHomebot(self):
    if self.player.getRect().colliderect(self.homeBot.getRect()):
      self.homeBot.inTakeDoc(self.player.getCollectedDocs())
      self.hp.updateHealth(GLOBAL.DOC_INCREASE_HEALTH * self.player.getCollectedDocs())
      self.player.emptyCollectedDocs()
    if self.hp.getHp() <= 0:
      self.postGame = True
      self.keepPlaying = False

  def initiateBryan(self):
    rect = pygame.Rect(0, 100, GLOBAL.BRYAN_WIDTH, GLOBAL.BRYAN_HEIGHT)
    self.bryans.append(Bryan(rect))

  def updateBryan(self):
    for b in self.bryans:
      if b.selectTarget(self.docs):
        b.moveToTarget()
      else:
        self.bryanSound.stop() 
        self.bryans.remove(b)
      docRects = list(map(lambda d: d.getRect(), self.docs))
      coll = b.getRect().collidelist(docRects)
      if coll >= 0:
        self.homeBot.inTakeDoc(1)
        self.hp.updateHealth(GLOBAL.DOC_INCREASE_HEALTH * 1)

  def updateDisplay(self):
    pygame.draw.rect(self.display.gameDisplay, (0, 0, 100), (0, 0, GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))
    self.display.drawBoxes(self.boxes)
    self.display.drawComps(self.comps)
    self.display.drawDocuments(self.docs)
    self.display.drawBryans(self.bryans)
    #pygame.draw.rect(self.display.gameDisplay, (0, 0, 255), self.player.getRect())
    self.display.drawDog(self.player, self.playerCooldownEvent)
    collectedDocs = 'Fetched docs:%d'% self.player.getCollectedDocs()
    self.display.drawWord(collectedDocs, 160, 20, [(255, 255, 0), (0, 0, 255)])
    self.display.drawHp(self.hp, self.hp.health) # we going to have some function to decrease the health
    #homeBot draw
    self.display.drawHomeBot(self.homeBot)
    #health bar draw
    self.hp.updateHealth(GLOBAL.NORMAL_DECREASING_RATE - self.diff)
    pygame.display.update()

  def updatePostDisplay(self):
    pygame.draw.rect(self.display.gameDisplay, (0, 0, 100), (0, 0, GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))
    self.leaderboard.setScore(int(self.homeBot.getDocNum() * 100))
    self.display.showEnterUsername(self.leaderboard, self.keyboard, self.text)

  def clear(self):
    del self.docs[:]
    del self.comps[:]
    del self.boxes[:]
    self.player.setAttack(False) 
    self.player.emptyCollectedDocs()
    pygame.time.set_timer(self.compSpawnEvent, 0)
    pygame.time.set_timer(self.boxSpawnEvent, 0)
    pygame.time.set_timer(self.playerBryanEvent, 0)
    pygame.time.set_timer(self.increaseDifficultyEvent, 0)


  def __del__(self):
    pygame.quit()

game = Game()

while game.keepPlaying or game.postGame:
  while game.keepPlaying:
    game.updateHomebot()
    game.updateCompetitors()
    game.updateBryan()
    game.updateBoxes()
    game.updateDocuments()

    game.updateDisplay()
    
    game.handleEvents()
    
    game.clock.tick(30)

  game.clear()

  while game.postGame:
    pygame.draw.rect(game.display.gameDisplay, (0, 0, 100), (0, 0, GLOBAL.MAP_WIDTH, GLOBAL.MAP_HEIGHT))
    game.updatePostDisplay()
    game.handleEvents()
    pygame.display.update()
    game.clock.tick(30)
    

quit()
