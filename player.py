class Player:
  def __init__(self, width, height, speed, direction):
    self.__width = width
    self.__height = height
    self.__speed = speed
    
    self.__directionX = 0  # 0 = left, 1 = right
    self.__directionY = 0  # 0 = up, 1 = down

    self.__rect = (width, height)

    self.__moveLeft = False
    self.__moveRight = False
    self.__moveUp = False
    self.__moveDown = False

  def setWidth(self, value):
    self.__width = value

  def getWidth(self):
    return self.__width

  def setHeight(self, value):
    self.__height = value

  def getHeight(self):
    return self.__height

  def setSpeed(self, value):
    self.__speed = value

  def getSpeed(self):
    return self.__speed

  def setDirectionX(self, value):
    self.__directionX = value

  def setDirectionY(self, value):
    self.__directionY = value

  def getDirectionX(self):
    return self.__directionX

  def getDirectionY(self):
    return self.__directionY

  def setRect(self, value):
    self.__rect = value

  def getRect(self):
    return self.__rect
  
  def setMoveLeft(self, value):
    self.__moveLeft = value

  def setMoveRight(self, value):
    self.__moveRight = value

  def setMoveUp(self, value):
    self.__moveUp = value

  def setMoveDown(self, value):
    self.__moveDown = value
  
  def getMoveLeft(self):
    return self.__moveLeft

  def getMoveRight(self):
    return self.__moveRight

  def getMoveUp(self):
    return self.__moveUp

  def getMoveDown(self):
    return self.__moveDown

  def moveX(self, dir):
    x_change = dir * self.__speed
    self.__rect.move_ip(x_change, 0)

  def moveY(self, dir):
    y_change = dir * self.__speed
    self.__rect.move_ip(0, y_change)

  