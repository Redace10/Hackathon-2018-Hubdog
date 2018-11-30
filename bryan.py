import math
import GLOBAL

class Bryan:
  def __init__(self, rect):
    self.__speed = GLOBAL.BRYAN_SPEED
    self.__rect = rect
    self.__target = None

  def getRect(self):
    return self.__rect

  def selectTarget(self, docs):
    if self.__target and docs.count(self.__target) > 0:
      return True
    else:
      if len(docs) == 0:
        return False
      minDistance = GLOBAL.MAP_WIDTH
      self.__target = None
      for d in docs:        
        xSquared = (self.__rect.x - d.getRect().x) * (self.__rect.x - d.getRect().x)
        ySquared = (self.__rect.y - d.getRect().y) * (self.__rect.y - d.getRect().y)
        distance = math.sqrt(xSquared + ySquared)
        if distance <= minDistance:
          minDistance = distance
          self.__target = d
      if self.__target != None:
        return True
      else:
        return False

  def moveToTarget(self):
    if self.__target != None:
      targetRect = self.__target.getRect()
      if targetRect.center[0] < self.__rect.center[0] - self.__speed:
        xOffset = -1 * self.__speed
      elif targetRect.center[0] > self.__rect.center[0] + self.__speed:
        xOffset = 1 * self.__speed
      else: 
        xOffset = 0
      if targetRect.center[1] < self.__rect.center[1] - self.__speed:
        yOffset = -1 * self.__speed
      elif targetRect.center[1] > self.__rect.center[1] + self.__speed:
        yOffset = 1 * self.__speed
      else: 
        yOffset = 0
      self.__rect.move_ip(xOffset, yOffset)