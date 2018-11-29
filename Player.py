class Player:
  def __init__(self, width, height, speed, direction):
    self._width = width
    self._height = height
    self._speed = speed
    self._direction = 0 # 0 = left, 1 = right
    self._attack = False
    self._attcounter = 0
    self._rect = None

  def set_width(self, value):
    self._width = value

  def get_width(self):
    return self._width

  def set_height(self, value):
    self._height = value

  def get_height(self):
    return self._height

  def set_speed(self, value):
    self._speed = value

  def get_speed(self):
    return self._speed

  def set_direction(self, value):
    self._direction = value

  def get_direction(self):
    return self._direction

  def set_rect(self, value):
    self._rect = value

  def get_rect(self):
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

  def get_attack(self):
    return self._attack

  def move_x(self, dir, border):
    x_change = dir * self._speed
    self._rect.move_ip(x_change, 0)
    self._rect.clamp_ip(border)

  def move_y(self, dir, border):
    y_change = dir * self._speed
    self._rect.move_ip(0, y_change)
    self._rect.clamp_ip(border)

  