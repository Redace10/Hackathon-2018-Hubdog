import os

class Score:
  def __init__(self):
    self.__score = 10
    self.__username = "Hamzah"
    self.__filename = "hamzahZia"
    self.__listScores = []
    self.__maxList = 10

  def setScore(self, value):
    self.__score = value

  def getScore(self):
    return self.__score

  def setUsername(self, name):
    self.__username = name

  def getUsername(self):
    return self.__username

  def enterUsername(self):
    print("we need to implement this")

  def updateLeaderboard(self):
    self.readScore()
    if (len(self.__listScores) > 0):
      highScore = self.__listScores[-1]["score"]
    else:
      highScore = 0

    if (self.__score > highScore or len(self.__listScores) < self.__maxList):
      self.enterUsername()
      if (len(self.__listScores) == self.__maxList):
        del self.__listScores[-1]
      self.insertScore()

    self.showTop10()

  def readScore(self):
    file = open(self.__filename, 'r+')
    lines = file.readlines()
    file.close()

    for line in lines:
      name, score = line.split(",")
      score = int(score)
      self.__listScores.append({"name": name, "score": score})

  def insertScore(self):
    os.remove(self.__filename)
    file = open(self.__filename, 'a+')
    enteredScore = False
    print(self.__listScores)
    for item in self.__listScores:
      name = item["name"]
      score = item["score"]
      if (self.__score > score and not enteredScore):
        file.write(self.__username+","+ str(self.__score) + "\n")
        enteredScore = True
      file.write(name+","+ str(score) + "\n")

    if (not enteredScore):
      file.write(self.__username+","+ str(self.__score) + "\n")
    file.close()

  def showTop10(self):
    print("aaaa")

score = Score()
score.updateLeaderboard()

