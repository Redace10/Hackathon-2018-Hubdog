import os

class Leaderboard:
  def __init__(self):
    self.__score = 49
    self.__username = "Hamzah"
    self.__filename = "leaderboard.txt"
    self.__listScores = []
    self.__maxList = 10
    self.__readLeaderboard = False

  def setScore(self, value):
    self.__score = value

  def getScore(self):
    return self.__score

  def setUsername(self, name):
    self.__username = name

  def getUsername(self):
    return self.__username

  def setReadLeaderboard(self, value):
    self.__readLeaderboard = value

  def getReadLeaderboard(self):
    return self.__readLeaderboard

  def getScoreList(self):
    return self.__listScores

  def getMaxList(self):
    return self.__maxList

  def updateLeaderboard(self):
    self.readScore()
    if (len(self.__listScores) > 0):
      highScore = self.__listScores[-1]["score"]
    else:
      highScore = 0

    return (self.__score > highScore or len(self.__listScores) < self.__maxList)

  def readScore(self):
    if not os.path.exists(self.__filename):
      file = open(self.__filename, 'a+')
    else:
      file = open(self.__filename, 'r+')
    lines = file.readlines()
    file.close()

    self.__listScores = []
    for line in lines:
      name, score = line.split(",")
      score = int(score)
      self.__listScores.append({"name": name, "score": score})

  def insertScore(self):
    os.remove(self.__filename)
    file = open(self.__filename, 'a+')
    enteredScore = False
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
    self.updateLeaderboard()

# score = Score()
# score.updateLeaderboard()

