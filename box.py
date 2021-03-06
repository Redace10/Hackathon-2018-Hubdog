from document import Document
import random
import pygame
import GLOBAL

class Box:
  def __init__(self, size, logo, rect, duration):
    self.__size = size
    self.__logo = logo
    self.__rect = rect
    self.__docs = []
    self.__open = False
    self.generate_docs()
    self.__endTime = pygame.time.get_ticks() + duration
    self.docDuration = 7000

  def getSize(self):
    return self.__size

  def getLogo(self):
    return self.__logo

  def getRect(self):
    return self.__rect

  def isOpen(self):
    return self.__open

  def generate_docs(self):
    if (self.__size == 'B'):
      numberDoc = random.randint(3, 5)
    elif (self.__size == 'S'):
      numberDoc = random.randint(1, 3)
    for d in range (numberDoc):
      format = random.choice(['cheque', 'invoice', 'pdf'])
      if (format == 'cheque'):
        rect = pygame.Rect(self.__rect.x, self.__rect.y, GLOBAL.CHEQUE_WIDTH, GLOBAL.CHEQUE_HEIGHT)
      else:
        rect = pygame.Rect(self.__rect.x, self.__rect.y, GLOBAL.DOC_WIDTH, GLOBAL.DOC_HEIGHT)
      doc = Document(format, rect)
      self.__docs.append(doc)

  def openBox(self):
    for i in range(len(self.__docs)):
      self.__docs[i].spread(i + 1, len(self.__docs))
    self.__open = True
    return self.__docs

  def shouldHide(self, currentTime):
    if currentTime >= self.__endTime or self.__open:
      return True
    return False
