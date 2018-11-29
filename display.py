import pygame

class Display:
  def __init__(self, pygame, playerWidth, playerHeight, mapWidth, mapHeight, boxWidth, boxHeight):
    self.border = (0, 108, 800, 415)
    self.dogImages = []
    self.dogIndex = 0
    self.dogFace = 0

    leftImages = []
    rightImages = []
    attackImages = []
    self.bigBanks = {}
    self.smallBanks = {}

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

    # box assets:
    amex = pygame.image.load('assets/bigBank/amex.png')
    amex = pygame.transform.scale(amex, (boxWidth, boxHeight))
    bmo = pygame.image.load('assets/bigBank/bmo.png')
    bmo = pygame.transform.scale(bmo, (boxWidth, boxHeight))
    chase = pygame.image.load('assets/bigBank/chase.png')
    chase = pygame.transform.scale(chase, (boxWidth, boxHeight))
    td = pygame.image.load('assets/bigBank/td.png')
    td = pygame.transform.scale(td, (boxWidth, boxHeight))
    wellsFargo = pygame.image.load('assets/bigBank/wellsFargo.png')
    wellsFargo = pygame.transform.scale(wellsFargo, (boxWidth, boxHeight))
    self.bigBanks = {"amex":amex, "bmo":bmo, "chase":chase, "td":td, "wellsFargo":wellsFargo}
    
    fido = pygame.image.load('assets/smallBank/fido.png')
    fido = pygame.transform.scale(fido, (boxWidth, boxHeight))
    tangerine = pygame.image.load('assets/smallBank/tangerine.png')
    tangerine = pygame.transform.scale(tangerine, (boxWidth, boxHeight))
    telstra = pygame.image.load('assets/smallBank/telstra.png')
    telstra = pygame.transform.scale(telstra, (boxWidth, boxHeight))
    self.smallBanks = {"fido":fido, "tangerine":tangerine, "telstra":telstra}
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

    self.gameDisplay = pygame.display.set_mode((mapWidth, mapHeight))

  def drawBoxes(self, boxes):
    for b in boxes:
      self.gameDisplay.blit(self.bigBanks[b.getLogo()], b.getRect())

  def drawDog(self, dog):
    if (self.dogIndex == 19):
      self.dogIndex = 0

    if (dog.getMoveLeft()):
      self.dogFace = 0
    elif (dog.getMoveRight()):
      self.dogFace = 1

    if (dog.getMoveLeft() or dog.getMoveRight() or dog.getMoveUp() or dog.getMoveDown()):
      self.dogIndex += 1
    dogImage = self.dogImages[self.dogFace][self.dogIndex//10]
    dog.getRect().clamp_ip(self.border)
    self.gameDisplay.blit(dogImage, dog.getRect())
    

