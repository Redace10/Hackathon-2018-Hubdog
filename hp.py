import pygame
import time
import GLOBAL
class Hp:
    #initialize some color rgb
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)

    def __init__(self, hp):
        self.health = hp

    def updateHealth(self, value):
        # here we need to figure out a logic of how 
        # HP bar decreases over time
        self.health = self.health - value
    
    def setGameDisplay(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def healthBarMain(self, playerHealth):
        if playerHealth > GLOBAL.MAP_WIDTH * 0.70:
            playerHealthColor = self.green
        elif playerHealth > GLOBAL.MAP_WIDTH * 0.45:
            playerHealthColor = self.yellow
        elif playerHealth > GLOBAL.MAP_WIDTH * 0.21:
            playerHealthColor = self.orange
        else:
            playerHealthColor = self.red
        pygame.draw.rect(self.gameDisplay, self.black, (47, GLOBAL.MAP_HEIGHT - 65, GLOBAL.MAP_WIDTH * 0.92, 37))
        pygame.draw.rect(self.gameDisplay, self.white, (52, GLOBAL.MAP_HEIGHT - 61, GLOBAL.MAP_WIDTH * 0.92, 29))
        if playerHealth > 0:
            pygame.draw.rect(self.gameDisplay, playerHealthColor, (54, GLOBAL.MAP_HEIGHT - 59, playerHealth, 25))