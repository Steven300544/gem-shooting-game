import pygame
from time import sleep
from random import randint
from sys import exit
from pygame.locals import *
pygame.init()
#         R    G    B
white = (255, 255, 255)
gray  = (180, 180, 180)
black =  (0,   0,   0)
green = (56,  140, 56)
red   = (255,  0,   0)
blue  =  (0,   0,  255)
screenWidth = 1000
screenHeight = 1000
ammoLeft = 20
ballsLeft = 0
stage = 1
coins = 0
startOver = False
singleShotMode= True
gun = ""
gunsBought = []
level = 1
ballsInfo = {}
a = {}
defaltStyle = None
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('gameicon.png'))
pygame.display.set_caption("gem shooting game")
screen = pygame.display.set_mode((screenWidth, screenHeight))
font_1 = pygame.font.Font(defaltStyle, 30)
font_2 = pygame.font.Font(defaltStyle, 75)
font_3 = pygame.font.Font(defaltStyle, 37)
ammoText = font_1.render("Ammo left: " + str(ammoLeft), True, black)
levelText = font_1.render("level " + str(level), True, black)
startScreenText = font_1.render("Press P to start level " + str(level), True, black)
winText = font_2.render("You passed level " + str(level) + " with " + str(ammoLeft) + " ammo left!", True, green)
loseText = font_2.render("out of ammo", True, red)
loadingText = font_1.render("Loading...", True, white)
loadingTextRect = loadingText.get_rect()
loadingTextRect.center = (screenWidth / 2, screenHeight / 2)
screen.blit(loadingText, (440, 475))
pygame.display.update()
def terminate():
    pygame.quit()
    exit()
def startScreen():
    global screen, clock, startScreenText, gray, font_1, stage, singleShotMode
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    terminate()
                if event.key == K_p:
                    if gun != "":
                        return
                if event.key == K_s:
                    shop()
                if event.key == K_w:
                    wepons()
                if event.key == K_c:
                    cheatCode = input("Enter cheat code here: ")
                    code = None
                    if cheatCode.isdigit():
                        code = int(cheatCode)
                        if (code > 0) and (code > stage):
                                stage = code
                        elif (code > 0) and (code < stage):
                          print("Do you really want to go back?")
                    elif cheatCode == "Heavy ammo mode":
                        if singleShotMode == True:
                            singleShotMode = False
                        else:
                            print("Heavy ammo mode already activted")
        startScreenText = font_2.render("Press P to start level " + str(level), True, black)
        startScreenTextRect = startScreenText.get_rect()
        startScreenTextRect.center = (screenWidth / 2, screenHeight * 0.382)
        screen.fill(gray)
        screen.blit(startScreenText, startScreenTextRect)        
        clock.tick(30)
        pygame.display.update()
def shop():
    global coins, font_1, font_2, font_3, singleShotMode, ammoLeft
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_b or event.key == K_s:
                    return
                if event.key == K_1:
                    if coins >= 5:
                        coins -=5
                        ammoLeft += 1
        shopScreenText = font_2.render("Shop", True, black)
        shopScreenTextRect = shopScreenText.get_rect()
        shopScreenTextRect.center = (screenWidth / 2, screenHeight * 0.1)
        coinsScreenText = font_1.render("You have " + str(coins) + " coins", True, black)
        coinsScreenTextRect = coinsScreenText.get_rect()
        coinsScreenTextRect.center = (screenWidth / 2, screenHeight * 0.15)
        item_2ScreenText = font_3.render("1 - Extra Ammo - Gives you extra ammo - 5 coins per ammo", True, black)
        item_2ScreenTextRect = item_2ScreenText.get_rect()
        item_2ScreenTextRect.center = (screenWidth / 2, screenHeight * 0.2)
        clock.tick(30)
        screen.fill(gray)
        screen.blit(shopScreenText, shopScreenTextRect)
        screen.blit(coinsScreenText, coinsScreenTextRect)
        screen.blit(item_2ScreenText, item_2ScreenTextRect)
        pygame.display.update()
def wepons():
    global coins, font_1, font_2, font_3, singleShotMode, ammoLeft, gun, gunsBought
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_b or event.key == K_w:
                    return
                if event.key == K_1:
                    if "SV 98" in gunsBought:
                        gun = "SV 98"
                        singleShotMode = False
                    elif coins >= 150:
                        coins -= 150
                        gunsBought.append("SV 98")
                        gun = "SV 98"
                        singleShotMode = False
                if event.key == K_2:
                    if "Pisto" in gunsBought:
                        gun = "Pisto"
                        singleShotMode = True
                    else:
                        gunsBought.append("Pisto")
                        gun = "Pisto"
                        singleShotMode = True
        weponsScreenText = font_2.render("weapons", True, black)
        weponsScreenTextRect = weponsScreenText.get_rect()
        weponsScreenTextRect.center = (screenWidth / 2, screenHeight * 0.1)
        coinsScreenText = font_1.render("You have " + str(coins) + " coins", True, black)
        coinsScreenTextRect = coinsScreenText.get_rect()
        coinsScreenTextRect.center = (screenWidth / 2, screenHeight * 0.15)
        if gun == "SV 98":
            item_1ScreenText = font_3.render("1- SV 98 - SV 98 can shoot mutiple gems down at once - eqqiped", True, black)
        elif "SV 98" in gunsBought:
            item_1ScreenText = font_3.render("1 - SV 98 - SV 98 can shoot mutiple gems down at once - bought", True, black)
        else:
            item_1ScreenText = font_3.render("1 - SV 98 - SV 98 can shoot mutiple gems down at once - 150 coins", True, black)
        item_1ScreenTextRect = item_1ScreenText.get_rect()
        item_1ScreenTextRect.center = (screenWidth / 2, screenHeight * 0.2)
        if gun == "Pisto":
            item_2ScreenText = font_3.render("2 - pisto - weakest gun. can only shoot down one gem- eqqiped", True, black)
        elif "Pisto" in gunsBought:
            item_2ScreenText = font_3.render("2 - pisto - weakest gun. can only shoot down one gem- bought", True, black)
        else:
            item_2ScreenText = font_3.render("2 - pisto - weakist gun. can only shoot down one gem- free", True, black)
        item_2ScreenTextRect = item_2ScreenText.get_rect()
        item_2ScreenTextRect.center = (screenWidth / 2, screenHeight * 0.275)
        clock.tick(30)
        screen.fill(gray)
        screen.blit(weponsScreenText, weponsScreenTextRect)
        screen.blit(coinsScreenText, coinsScreenTextRect)
        screen.blit(item_1ScreenText, item_1ScreenTextRect)
        screen.blit(item_2ScreenText, item_2ScreenTextRect)
        pygame.display.update()
sleep(5)
while True:
    startScreen()
    for q in range(1, 7 + 1):
        ballsLeft += 1
        newBallImage = pygame.image.load("gem%s.png" % q)
        newBallImageRect = newBallImage.get_rect()
        newBallImageRect = newBallImageRect.move(randint(0,900), randint(0, 900))
        ballsInfo[newBallImage] = [newBallImageRect, [randint(level * 2 * stage, level * 3 * stage), randint(level * 3, level * 5)]]
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
                            if ballsLeft == 0:
                                coins += ammoLeft * 5
                                ammoText = font_1.render("Ammo left: " + str(ammoLeft),  True, black)
                                winText = font_2.render("You passed level " + str(level) + " with " + str(ammoLeft) + " ammo left!", True, green)
                                winTextRect = winText.get_rect()
                                winTextRect.center = (screenWidth / 2, screenHeight * 0.382)
                                screen.fill(gray)
                                for key in ballsInfo:
                                    screen.blit(key, ballsInfo[key][0])
                                screen.blit(levelText, (20, 20))
                                screen.blit(ammoText, (20, 40))
                                screen.blit(winText, winTextRect)
                                clock.tick(30)
                                pygame.display.update()
                                sleep(10)
                                if level == 6:
                                    stage += 1
                                    level = 1
                                    ammoLeft = 20
                                else:
                                    ammoLeft += 14
                                    level += 1
                            elif singleShotMode == True:
                                break
                else:
                    ammoText = font_1.render("Ammo left: " + str(ammoLeft),  True, black)
                    loseText = font_2.render("You failed level " + str(level), True, red)
                    loseTextRect = loseText.get_rect()
                    loseTextRect.center = (screenWidth / 2, screenHeight * 0.382)
                    screen.fill(gray)
                    for key in ballsInfo:
                        screen.blit(key, ballsInfo[key][0])
                    screen.blit(levelText, (20, 20))
                    screen.blit(ammoText, (20, 40))
                    screen.blit(loseText, loseTextRect)
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
