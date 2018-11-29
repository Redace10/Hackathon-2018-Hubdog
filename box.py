# from document import Doc

class Box:
  def __init__(self, size, logo, rect):
    self.__size = size
    self.__logo = logo
    self.__rect = rect
    self.__docs = []
    self.__open = False
    self.generate_docs()

  def getSize(self):
    return self.__size

  def getLogo(self):
    return self.__logo

  def getRect(self):
    return self.__rect

  def isOpen(self):
    return self.__open

  def generate_docs(self):
    self.__doc = [1, 2, 3, 4]

  def boxOpen(self):
    for i in len(self.__docs):
      j = 0 # self.__doc[i].spread(i, len(self.__docs))
    self.__open = True
    return self.__docs