import GLOBAL
import pygame
class HomeBot:
    def __init__(self):
        self.__curDoc = 0 # documents that have been collected

    def setGameDisplay(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.homeBotIcon = pygame.image.load('assets/homeBot.png')
        self.homeBotIcon = pygame.transform.scale(self.homeBotIcon, (100, 200))
        self.playerRect = self.homeBotIcon.get_rect(center=(25, GLOBAL.MAP_HEIGHT*0.85))
        self.gameDisplay.blit(self.homeBotIcon, self.playerRect)
    
    def getRect(self):
        return self.playerRect
    
    def getDocNum(self):
        return self.__curDoc
    
    def inTakeDoc(self, numOfDoc):
        self.__curDoc += numOfDoc
    
