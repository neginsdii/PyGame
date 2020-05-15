import pygame

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

def player(x,y):
    screen.blit(playerImg, (x,y))

def checkBound(x,y):
    if x<0:
        playerX=0
    if x>800+63:
        playerX=800-63

#Game Loop
running =True
while running:
    screen.fill((40,50,107))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                playerVelX-=0.3
            if event.key== pygame.K_RIGHT:
                playerVelX+=0.3
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerVelX=0
                
    playerX+=playerVelX
    checkBound(playerX,playerY)
    player(playerX,playerY)
    pygame.display.update()