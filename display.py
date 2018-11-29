import pygame

class Display:
  def __init__(self, pygame, playerWidth, playerHeight, mapWidth, mapHeight):
    self.dogImages = []
    leftImages = []
    rightImages = []
    attackImages = []

    left1 = pygame.image.load('assets/move/left1.png')
    left2 = pygame.image.load('assets/move/left2.png')
    left1 = pygame.transform.scale(left1, (playerWidth, playerHeight))
    left2 = pygame.transform.scale(left2, (playerWidth, playerHeight))

    right1 = pygame.image.load('assets/move/right1.png')
    right2 = pygame.image.load('assets/move/right2.png')
    right1 = pygame.transform.scale(right1, (playerWidth, playerHeight))
    right2 = pygame.transform.scale(right2, (playerWidth, playerHeight))

    attack1 = pygame.image.load('assets/attack/attackLeft.png')
    attack2 = pygame.image.load('assets/attack/attackRight.png')
    attack1 = pygame.transform.scale(attack1, (playerWidth, playerHeight))
    attack2 = pygame.transform.scale(attack2, (playerWidth, playerHeight))

    # self.map = pygame.image.load('boss battle.png')

    leftImages.append(left1)
    leftImages.append(left2)
    rightImages.append(right1)
    rightImages.append(right2)
    attackImages.append(attack1)
    attackImages.append(attack2)

    self.dogImages.append(leftImages)
    self.dogImages.append(rightImages)
    self.dogImages.append(attackImages)

    gameDisplay = pygame.display.set_mode((mapWidth, mapHeight))
