import pygame
import os

from Player import Player

# sets basic game features
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# plays background song repeatedly
pygame.mixer.music.load("The Marching Pirate Spy.mp3")
pygame.mixer.music.play(-1, 0)

# initialize player
player = Player(135, 115, 5, 0)

dog_images = []
left_images = []
right_images = []
attack_images = []

left1 = pygame.image.load('moving/good/left1.png')
left2 = pygame.image.load('moving/good/left2.png')
left1 = pygame.transform.scale(left1, (player.get_width(), player.get_height()))
left2 = pygame.transform.scale(left2, (player.get_width(), player.get_height()))

right1 = pygame.image.load('moving/good/right1.png')
right2 = pygame.image.load('moving/good/right2.png')
right1 = pygame.transform.scale(right1, (player.get_width(), player.get_height()))
right2 = pygame.transform.scale(right2, (player.get_width(), player.get_height()))

attack1 = pygame.image.load('attack/attack1.png')
attack2 = pygame.image.load('attack/attack1.png')
attack1 = pygame.transform.scale(attack1, (player.get_width(), player.get_height()))
attack2 = pygame.transform.scale(attack2, (player.get_width(), player.get_height()))

map = pygame.image.load('boss battle.png')

left_images.append(left1)
left_images.append(left2)
right_images.append(right1)
right_images.append(right2)
attack_images.append(attack1)
attack_images.append(attack2)

dog_images.append(left_images)
dog_images.append(right_images)
dog_images.append(attack_images)

face = 0
index = 0
dog = dog_images[index]

x_Display = 800
y_Display = 600
gameDisplay = pygame.display.set_mode((x_Display, y_Display))
game_border = (0, 108, 800, 415)

# dog movements and body
movement_speed = 5
x_change = 0
y_change = 0
player.set_rect(dog[0].get_rect())

# beginning game features
keepPlaying = True
clock = pygame.time.Clock()

# variables for which side the dog is facing
moveUp = moveDown = moveRight = moveLeft = False
attack = False

while keepPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepPlaying = False

        if event.type == pygame.KEYDOWN and player.get_attack() == False:
            if event.key == pygame.K_LEFT:
                player.set_direction(0)
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                player.set_direction(1)
                moveRight = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True
            if event.key == pygame.K_SPACE:
                player.attack(game_border)
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False

  # Walking animation
    if (index == 19):
        index = 0
    else:
        if (moveLeft or moveRight or moveUp or moveDown):
            index += 1

    # Player movement
    if (moveRight and player.get_attack() == False):
      player.move_x(1, game_border)
    if (moveLeft and player.get_attack() == False):
      player.move_x(-1, game_border)
    if (moveUp):
      player.move_y(-1, game_border)
    if (moveDown):
      player.move_y(1, game_border)
    
    # draw map
    gameDisplay.blit(map, (0, 0))
    # draw player
    if (player.get_attack()):
        player.attack(game_border)
        face = 2
        dog = dog_images[face][index//10]
        gameDisplay.blit(dog, (player.get_rect().x, player.get_rect().y-30))
    else:
        face = player.get_direction()
        dog = dog_images[face][index//10]
        gameDisplay.blit(dog, player.get_rect())

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
