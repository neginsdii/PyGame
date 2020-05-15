import pygame
import random

pygame.init()

screen= pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load("transport.png")
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load("spaceship.png")
playerX= 370
playerY =480
playerVelX=0
playerVely=0

#Enemy
enemyImg=pygame.image.load("alien.png")
enemyX= random.randint(0,736)
enemyY =random.randint(0,350)
enemyVelX=0.3
enemyVely=0.5


def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))



#Game Loop
running =True
while running:
    screen.fill((40,50,107))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                playerVelX-=0.4
            if event.key== pygame.K_RIGHT:
                playerVelX+=0.4
            if event.key==pygame.K_ESCAPE:
                running=False
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerVelX=0
                
    playerX+=playerVelX
    if playerX<0:
        playerX=0
    if playerX>737:
        playerX=737

    enemyX+=enemyVelX

    if enemyX<0:
        enemyVelX=0.3
        enemyY+=enemyVely
    elif enemyX>737:
        enemyVelX=-0.3  
        enemyY+=enemyVely

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()