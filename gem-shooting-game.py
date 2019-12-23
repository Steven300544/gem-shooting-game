import pygame
from time import sleep
from random import randint
from sys import exit
from pygame.locals import *
pygame.init()
#         R    G    B
white = (255, 255, 255)
gray  = (125, 125, 125)
black =  (0,   0,   0)
green = (50,  250, 125)
red   = (255,  0,   0)
blue  =  (0,   0,  255)
screenWidth = 1000
screenHeight = 1000
ammoLeft = 20
ballsLeft = 0
startOver = False
level = 1
ballsInfo = {}
a = {}
defaltStyle = None
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('/home/pi/python_games/gameicon.png'))
pygame.display.set_caption("gem shooting game")
screen = pygame.display.set_mode((screenWidth, screenHeight))
font_1 = pygame.font.Font(defaltStyle, 30)
font_2 = pygame.font.Font(defaltStyle, 75)
ammoText = font_1.render("Ammo left: " + str(ammoLeft), True, black)
levelText = font_1.render("level " + str(level), True, black)
startScreenText = font_1.render("Press P to start level " + str(level), True, black)
winText = font_2.render("You passed level " + str(level) + " with " + str(ammoLeft) + " ammo left!", True, green)
loseText = font_2.render("out of ammo", True, red)
loadingText = font_1.render("Loading...", True, white)
screen.blit(loadingText, (440, 475))
pygame.display.update()
def terminate():
    pygame.quit()
    exit()
def startScreen():
    global screen, clock, startScreenText, gray, font_1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    terminate()
                if event.key == K_p:
                    print("DDD")
                    return
##                if event.key == K_c:
##                    code = input("Enter cheat code here: ")
##                    for cheatCodeNumber in range(2, 6):
##                        if code = cheatCodeList[cheatCodeNumber]:
##                            level = cheatCodeNumber
        startScreenText = font_2.render("Press P to start level " + str(level), True, black)
        screen.fill(gray)
        screen.blit(startScreenText, (250, 250))        
        clock.tick(30)
        pygame.display.update()
sleep(5)
while True:
    startScreen()
    for q in range(1, 8):
        ballsLeft += 1
##      change the path of the files on the line below to your computer's path of the files
        newBallImage = pygame.image.load("/home/pi/python_games/gem%s.png" % q)
        newBallImageRect = newBallImage.get_rect()
        newBallImageRect = newBallImageRect.move(randint(0,900), randint(0, 900))
        ballsInfo[newBallImage] = [newBallImageRect, [randint(level * 3, level * 5), randint(10, 15)]]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                if ammoLeft != 0:
                    ammoLeft -= 1
                    for ball in ballsInfo:
                        if ballsInfo[ball][0].collidepoint(pygame.mouse.get_pos()):
                            a = dict(ballsInfo)
                            del a[ball]
                            ballsInfo = dict(a)
                            ballsLeft -= 1
                            print("del ball")
                            if ballsLeft == 0:
                                ammoText = font_1.render("Ammo left: " + str(ammoLeft),  True, black)
                                winText = font_2.render("You passed level " + str(level) + " with " + str(ammoLeft) + " ammo left!", True, green)
                                screen.fill(gray)
                                for key in ballsInfo:
                                    screen.blit(key, ballsInfo[key][0])
                                screen.blit(levelText, (20, 20))
                                screen.blit(ammoText, (20, 40))
                                screen.blit(winText, (50, 250))
                                clock.tick(30)
                                pygame.display.update()
                                sleep(10)
                                if level == 6:
                                    level = 1
                                    ammoLeft = 20
                                else:
                                    ammoLeft += 14
                                    level += 1
                else:
                    ammoText = font_1.render("Ammo left: " + str(ammoLeft),  True, black)
                    loseText = font_2.render("You failed level " + str(level), True, red)
                    screen.fill(gray)
                    for key in ballsInfo:
                        screen.blit(key, ballsInfo[key][0])
                    screen.blit(levelText, (20, 20))
                    screen.blit(ammoText, (20, 40))
                    screen.blit(loseText, (275, 250))
                    clock.tick(30)
                    pygame.display.update()
                    sleep(10)
                    level = 1
                    ballsInfo = {}
                    startOver = True
        for key in ballsInfo:
            newBallImageRect2 = ballsInfo[key][0]
            newBallImageRect2 = newBallImageRect2.move(ballsInfo[key][1])
            ballsInfo[key][0] = newBallImageRect2
            if ballsInfo[key][0].left < 0 or ballsInfo[key][0].right > screenWidth:
                ballsInfo[key][1][0] = -ballsInfo[key][1][0]
            if ballsInfo[key][0].top < 0 or ballsInfo[key][0].bottom > screenHeight:
                ballsInfo[key][1][1] = -ballsInfo[key][1][1]
        if ballsLeft == 0:
            break
        elif startOver == True:
            startOver = False
            ballsLeft = 0
            ammoLeft = 20
            break
        levelText = font_1.render("level " + str(level), True, black)
        ammoText = font_1.render("Ammo left: " + str(ammoLeft),  True, black)
        screen.fill(gray)
        for key in ballsInfo:
            screen.blit(key, ballsInfo[key][0])
        screen.blit(levelText, (20, 20))
        screen.blit(ammoText, (20, 40))
        clock.tick(30)
        pygame.display.update()