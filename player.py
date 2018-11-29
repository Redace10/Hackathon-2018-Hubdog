class Player:
  def __init__(self, width, height, speed, direction):
    self.__width = width
    self.__height = height
    self.__speed = speed
    
    self.__directionX = 0  # 0 = left, 1 = right
    self.__directionY = 0  # 0 = up, 1 = down

    self.__attack = False
    self.__attcounter = 0
    self.__rect = None

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
    self._rect = value

  def getRect(self):
    return self._rect

  def attack(self, border):
    self._attack = True
    self._attcounter += 1
    self._speed = 10
    movement = (self._direction * 2) - 1
    self.move_x(movement, border)
    if (self._attcounter > 10):
      self._speed = 5
      self._attcounter = 0
      self._attack = False

  def getAttack(self):
    return self.__attack

  def moveX(self, dir, border):
    x_change = dir * self._speed
    self._rect.move_ip(x_change, 0)
    self._rect.clamp_ip(border)

  def moveY(self, dir, border):
    y_change = dir * self._speed
    self._rect.move_ip(0, y_change)
    self._rect.clamp_ip(border)

  