import pygame
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
        self.playerIcon = pygame.image.load('assets/move/right1.png')
        self.playerRect = self.playerIcon.get_rect(center=(20, 560))

    def loseHealth(self):
        # here we need to figure out a logic of how 
        # HP bar decreases over time
        pass
        
    def gainHealth(self):
        pass
    
    def setGameDisplay(self, gameDisplay):
        self.gameDisplay = gameDisplau

    def healthBarMain(self, playerHealth):
        if playerHealth > 75:
            playerHealthColor = self.green
        elif playerHealth > 50:
            playerHealthColor = self.yellow
        elif playerHealth > 25:
            playerHealthColor = self.orange
        else:
            playerHealthColor = self.red
        self.gameDisplay.blit(self.playerIcon, self.playerRect)
        pygame.draw.rect(self.gameDisplay, self.black, (78, 544, 112, 37))
        pygame.draw.rect(self.gameDisplay, self.white, (82, 548, 104, 29))
        if playerHealth > 0:
            pygame.draw.rect(self.gameDisplay, playerHealthColor, (84, 550, playerHealth, 25))