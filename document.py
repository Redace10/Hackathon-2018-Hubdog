class Document:
  def __init__(self, format, rect):
    self.__format = format
    self.__rect = rect
    self.__spread = False
    self.__spreadCounter = 0

  def getSpread(self):
    return self.__spread

  def getFormat(self):
    return self.__format

  def getRect(self):
    return self.__rect

  def spread(self, dir=None, total=None):
    self.__spread = True
    self.__spreadCounter += 1
    if dir != None:
      self.__dir = dir
    if total != None:
      self.__total = total
    shift = self.get_shift()
    self.__rect.move_ip(shift[0], shift[1])
    if (self.__spreadCounter > 30):
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
    return (0, 0)
