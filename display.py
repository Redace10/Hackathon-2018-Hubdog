import pygame

CHEQUE_WIDTH = 30
CHEQUE_HEIGHT = 15
DOC_WIDTH = 20
DOC_HEIGHT = 40

class Display:
  def __init__(self, pygame, playerWidth, playerHeight, mapWidth, mapHeight, boxWidth, boxHeight):
    self.border = (0, 10, mapWidth, mapHeight - 50)
    self.dogImages = []
    self.dogIndex = 0
    self.dogFace = 0

    leftImages = []
    rightImages = []
    bigBanks = {}
    smallBanks = {}

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
    bigBanks = {'amex':amex, 'bmo':bmo, 'chase':chase, 'td':td, 'wellsFargo':wellsFargo}
    
    fido = pygame.image.load('assets/smallBank/fido.png')
    fido = pygame.transform.scale(fido, (boxWidth, boxHeight))
    tangerine = pygame.image.load('assets/smallBank/tangerine.png')
    tangerine = pygame.transform.scale(tangerine, (boxWidth, boxHeight))
    telstra = pygame.image.load('assets/smallBank/telstra.png')
    telstra = pygame.transform.scale(telstra, (boxWidth, boxHeight))
    smallBanks = {'fido':fido, 'tangerine':tangerine, 'telstra':telstra}

    self.banks = {'B':bigBanks, 'S':smallBanks}

    # Document assets
    cheque = pygame.image.load('assets/document/cheque.png')
    cheque = pygame.transform.scale(cheque, (CHEQUE_WIDTH, CHEQUE_HEIGHT))
    invoice = pygame.image.load('assets/document/invoice.png')
    invoice = pygame.transform.scale(invoice, (DOC_WIDTH, DOC_HEIGHT))
    pdf = pygame.image.load('assets/document/pdf.png')
    pdf = pygame.transform.scale(pdf, (DOC_WIDTH, DOC_HEIGHT))

    self.documents = {'cheque':cheque, 'invoice':invoice, 'pdf':pdf}

    # map
    # self.map = pygame.image.load('assets/boss battle.png')

    leftImages.append(left1)
    leftImages.append(left2)
    rightImages.append(right1)
    rightImages.append(right2)

    self.dogImages.append(leftImages)
    self.dogImages.append(rightImages)
    self.dogImages.append(attack1)
    self.dogImages.append(attack2)

    self.gameDisplay = pygame.display.set_mode((mapWidth, mapHeight))

  def drawBoxes(self, boxes):
    for b in boxes:
      self.gameDisplay.blit(self.banks[b.getSize()][b.getLogo()], b.getRect())

  def drawDocuments(self, docs):
    for d in docs:
      self.gameDisplay.blit(self.documents[d.getFormat()], d.getRect())

  def drawDog(self, dog):
    # self.gameDisplay.blit(self.map, (0, 0))
    if (self.dogIndex == 19):
      self.dogIndex = 0

    if (dog.getMoveLeft()):
      self.dogFace = 0
    elif (dog.getMoveRight()):
      self.dogFace = 1

    if (dog.getMoveLeft() or dog.getMoveRight() or dog.getMoveUp() or dog.getMoveDown()):
      self.dogIndex += 1
    
    dog.getRect().clamp_ip(self.border)
    if (dog.getAttack()):
      if (self.dogFace == 0):
        dogImage = self.dogImages[2]
      elif(self.dogFace == 1):
        dogImage = self.dogImages[3]
      dog.attack(self.dogFace)
      self.gameDisplay.blit(dogImage, (dog.getRect().x, dog.getRect().y))
    else:
      dogImage = self.dogImages[self.dogFace][self.dogIndex//10]
      self.gameDisplay.blit(dogImage, dog.getRect())

    def drawDisplay(self, pygame):
      pygame.draw.rect(self.gameDisplay, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
      self.drawBoxes(game.boxes)
      self.drawDocuments(game.docs)
      pygame.draw.rect(self.gameDisplay, (0, 0, 255), game.player.getRect())
      self.drawDog(game.player)
      pygame.display.update()
    

