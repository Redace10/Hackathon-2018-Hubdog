class HomeBot:
    def __init__(self):
        self.__curDoc = 0 # documents that have been collected

    def setGameDisplay(self, gameDisplay):
        self.gameDisplay = gameDisplay
    
    def getDocNum(self):
        return self.__curDoc
    
    def inTakeDoc(self, numOfDoc):
        self.__curDoc += numOfDoc
    
