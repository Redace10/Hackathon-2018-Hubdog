class Document:
  def __init__(self, format, rect):
    self.__format = format
    self.__rect = rect
    self.__spread = False
    self.__spreadCounter = 0
    self.__endTime = 0
    self.__targeted = False

  def getTargeted(self):
    return self.__targeted

  def setTargeted(self, value):
    self.__targeted = value

  def getSpread(self):
    return self.__spread

  def getFormat(self):
    return self.__format

  def getRect(self):
    return self.__rect

  def setDuration(self, currentTime, duration):
    self.__endTime = currentTime + duration

  def shouldHide(self, currentTime):
    if currentTime >= self.__endTime:
      return True
    return False

  def spread(self, dir=None, total=None):
    self.__spread = True
    speed = 5
    self.__spreadCounter += 1*speed
    if dir != None:
      self.__dir = dir
    if total != None:
      self.__total = total
    shift = self.get_shift()
    self.__rect.move_ip(shift[0]*speed, shift[1]*speed)
    if (self.__spreadCounter > 90):
      self.__spreadCounter = 0
      self.__spread = False

  def get_shift(self):
    if self.__dir == 1 and self.__total != 4:
      return [0, -1]
    if self.__dir == 1 and self.__total == 4:
      return [-1, -1]
    if self.__dir == 2 and self.__total == 2:
      return [0, 1]
    if self.__dir == 2 and self.__total >= 3:
      return [1, 1]
    if self.__dir == 3 and self.__total >= 3:
      return [-1, 1]
    if self.__dir == 4 and self.__total >= 4:
      return [1, -1]
    if (self.__dir == 5 and self.__total == 5):
      return [-1, -1]
    return [0, 0]
