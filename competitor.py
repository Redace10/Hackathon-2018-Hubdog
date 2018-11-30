class Competitor:
  def __init__(self, logo, rect):
    self.__logo = logo
    self.__rect = rect

  def getRect(self):
    return self.__rect