#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:13:07 2022

@author: darmoment
"""

import sys 
import pygame
import pygame.locals
import pygame.sprite 
import random
from random import randrange
        
#Froggy Sprite
class Froggy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.image = pygame.transform.rotate(FROG, -90)
        self.rect = pygame.Rect(30, 270, 40, 40)
        
    def draw(self):
        surface.blit(self.image, self.rect)
        
    #Changes the direction of the frog when it moves (style)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_LEFT] or keys[pygame.locals.K_a]:
            self.image = pygame.transform.rotate(FROG, 90)
        elif keys[pygame.locals.K_RIGHT] or keys[pygame.locals.K_d]:
            self.image = pygame.transform.rotate(FROG, -90)
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
            self.image = pygame.transform.rotate(FROG, 0)
        elif keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
            self.image = pygame.transform.rotate(FROG, -180)
        elif self.rect.x > 646 and self.rect.y < 80:
            self.rect.x = 645

#Car sprites (Row One, Two, Three)
class CarOne(pygame.sprite.Sprite):
    
    def __init__(self, yposition):
        super().__init__()
        
        self.image = random.choice([BLUE, GREEN, RED])
        self.rect = pygame.Rect(100, yposition, 60, 80)
        self.ydir = 4 #sets the speed
    
    def draw(self):
        surface.blit(self.image, self.rect)
    
    #Moves the car down the page and resets the car back to top when it leaves the screen
    def update(self):
        if self.rect.top > 580:
            self.rect = self.image.get_rect(center = (130,0))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)
            
class CarTwo(pygame.sprite.Sprite):
    
    def __init__(self, yposition):
        super().__init__()
        
        self.image = random.choice([BLUE, GREEN, RED])
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center = (210,yposition))
        self.ydir = -2
        
    def draw(self):
        surface.blit(self.image, self.rect)
        
     #Moves the car up the page and resets the car back to bottom when it leaves the screen
    def update(self):
        if self.rect.bottom < 0:
            self.rect = self.image.get_rect(center = (210,580))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)
            
class CarThree(pygame.sprite.Sprite):
    
    def __init__(self, yposition):
        super().__init__()
        
        self.image = random.choice([BLUE, GREEN, RED])
        self.rect = self.image.get_rect(center = (290, yposition))
        self.ydir = 6
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Moves the car down the page and resets the car back to top when it leaves the screen    
    def update(self):
        if self.rect.top > 580:
            self.rect = self.image.get_rect(center = (290,0))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)
            
#LogSprites (Row One, Two, Three)
class LogOne(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()
        
        self.image = LOGROW1
        self.rect = self.image.get_rect(center = (450, yposition))
        self.ydir = -2 #sets the speed
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Moves the log up the page and resets to bottom when log leaves the screen
    def update(self):
        if self.rect.bottom < 0:
            self.rect = self.image.get_rect(center = (450, 680))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)
   
class LogTwo(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()
        
        self.image = LOGROW2
        self.rect = self.image.get_rect(center = (530, yposition))
        self.ydir = 3
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Moves the log down the page and resets to top when log leaves the screen    
    def update(self):
        if self.rect.top > 580:
            self.rect = self.image.get_rect(center = (530, -45))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)
            
class LogThree(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()

        self.image = LOGROW3
        self.rect = self.image.get_rect(center = (610, yposition))
        self.ydir = -4
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Moves the log up the page and resets to bottom when log leaves the screen    
    def update(self):
        if self.rect.bottom < 0:
            self.rect = self.image.get_rect(center = (610, 713))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)

#Water sprite (for collision detection)  
class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.surf = pygame.Surface((240, 580))
        self.rect = self.surf.get_rect(center = (530, 290))
        self.surf.fill((0, 36, 119))
        
    def draw(self):
        surface.blit(self.surf, self.rect)

#Lilpyad sprites
class LilyPad(pygame.sprite.Sprite):
    
    def __init__(self, yposition):
        super().__init__()
        
        self.image = LILYPAD
        self.rect = self.image.get_rect(center = (690, yposition))
        
    def draw(self):
        surface.blit(self.image, self.rect)

#Bush sprites
class Bush(pygame.sprite.Sprite):
    def __init__(self, xposition, yposition):
        super().__init__()
        
        self.image = BUSH
        self.rect = self.image.get_rect(topleft = (xposition, yposition))
        
    def draw(self):
        surface.blit(self.image, self.rect)
        
#Coin sprites
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #randomizes coin position in spots easily accessible for the frog
        xposition = randrange(50, 410, 80)
        yposition = randrange(40, 560, 80)
        
        self.image = COIN
        self.rect = self.image.get_rect(center = (xposition, yposition))
    
    def draw(self):
        surface.blit(self.image, self.rect)

#Coin sprites on LogOne Logs
class CoinLogOne(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()
        
        self.image = COIN
        self.rect = self.image.get_rect(center = (450, yposition))
        self.ydir = -2 #sets the speed
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Gives the illusion of coin riding a log1 log  
    def update(self):
        if self.rect.bottom < 0:
            self.rect = self.image.get_rect(center = (450, 765))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)

#Coin sprites on LogTwo Logs
class CoinLogTwo(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()
        
        self.image = COIN
        self.rect = self.image.get_rect(center = (530, yposition))
        self.ydir = 3
        
    def draw(self):
        surface.blit(self.image, self.rect)

    #Gives the illusion of coin riding a log2 log
    def update(self):
        if self.rect.top > 580:
            self.rect = self.image.get_rect(center = (530, -75))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)

#Coin sprites on LogThree Logs
class CoinLogThree(pygame.sprite.Sprite):
    def __init__(self, yposition):
        super().__init__()

        self.image = COIN
        self.rect = self.image.get_rect(center = (610, yposition))
        self.ydir = -4
        
    def draw(self):
        surface.blit(self.image, self.rect)
    
    #Gives the illusion of coin riding a log3 log
    def update(self):
        if self.rect.bottom < 0:
            self.rect = self.image.get_rect(center = (610, 765))
            self.rect.move_ip(0, self.ydir)
        else:
            self.rect.move_ip(0, self.ydir)

#Live Sprites
class Lives(pygame.sprite.Sprite):
    def __init__ (self, xposition):
        super().__init__()

        self.image = FROGLIFE
        self.rect = self.image.get_rect(topleft = (xposition, 10))

    def draw(self):
        surface.blit(self.image, self.rect)

        
pygame.init()
surface = pygame.display.set_mode((740,580))
pygame.display.set_caption('Frogger')

#Load up all game images and scale/rotate them~~
#Frogg
IMAGE = pygame.image.load('images/Frogger.png').convert_alpha()
GREEN = pygame.image.load('images/GreenCar.png').convert_alpha() #CARS
BLUE = pygame.image.load('images/BlueCar.png').convert_alpha() #CARS
RED = pygame.image.load('images/RedCar.png').convert_alpha() #CARS
LOG = pygame.image.load('images/Log.png').convert_alpha() 
LILYPAD = pygame.image.load('images/LilyPad.png').convert_alpha()
BUSH = pygame.image.load('images/Bush.png')
COIN = pygame.image.load('images/Coin.png')
FROGLIFE = pygame.image.load('images/FroggerLife.png') #LIFE ICON
FROG = pygame.transform.scale(IMAGE, (40, 40))
GREEN = pygame.transform.scale(GREEN, (60, 80)) #CARS
BLUE = pygame.transform.scale(BLUE, (60, 80)) #CARS
RED = pygame.transform.scale(RED, (60, 80)) #CARS
LOG = pygame.transform.rotate(LOG, -90)
LOGROW1 = pygame.transform.scale(LOG, (60, 200)) #LOG ROW ONE
LOGROW2 = pygame.transform.scale(LOG, (60, 90)) #LOG ROW TWO
LOGROW3 = pygame.transform.scale(LOG, (60, 133)) #LOG ROW THREE
LILYPAD = pygame.transform.scale(LILYPAD, (80, 80))
LILYPAD = pygame.transform.rotate(LILYPAD, 90)
BUSH = pygame.transform.scale(BUSH, (80,80))
COIN = pygame.transform.scale(COIN, (30, 30))
FROGLIFE = pygame.transform.scale(FROGLIFE, (100, 66))
CARHORN = pygame.mixer.Sound("sounds/car-horn.mp3")
COLLECTCOIN = pygame.mixer.Sound("sounds/coin.wav")
WATERFALL = pygame.mixer.Sound("sounds/dropinwater.mp3")
COLLIDEBUSH = pygame.mixer.Sound("sounds/bushes.mp3")

#Created a whole main function to have multiple functions within and game loops
def main():

    #Creates the basic background surfaces
    grass1 = pygame.Surface((90,580))
    grass1.fill((21, 65, 39))
    concrete = pygame.Surface((240, 580))
    concrete.fill((117, 120, 123))
    grass2 = pygame.Surface((80,580))
    grass2.fill((21, 65, 39))
    grass3 = pygame.Surface((90,580))
    grass3.fill((21, 65, 39))
    
    #Calls all game items with their respective x/y position parameters
    FROGGY = Froggy()
    CAR1 = CarOne(0)
    CAR2 = CarTwo(0)
    CAR3 = CarThree(0)
    CAR11 = CarOne(-200)
    CAR21 = CarTwo(260)
    CAR31 = CarThree(-100)
    CAR32 = CarThree(310)
    LOG1 = LogOne(150)
    LOG11 = LogOne(450)
    LOG2 = LogTwo(67)
    LOG21 = LogTwo(201)
    LOG22 = LogTwo(335)
    LOG23 = LogTwo(469)
    LOG24 = LogTwo(603)
    LOG3 = LogThree(97)
    LOG31 = LogThree(291)
    LOG32 = LogThree(485)
    WATER = Water()
    LILYPAD1 = LilyPad(120)
    LILYPAD2 = LilyPad(280)
    LILYPAD3 = LilyPad(440)
    BUSH1 = Bush(646, 0)
    BUSH2 = Bush(646, -40)
    BUSH3 = Bush(646, 159)
    BUSH4 = Bush(646, 160)
    BUSH5 = Bush(646, 319)
    BUSH6 = Bush(646, 320)
    BUSH7 = Bush(646, 479)
    COIN1 = Coin()
    COIN2 = Coin()
    COIN3 = Coin()
    COIN4 = Coin()
    COIN5 = Coin()
    COIN6 = CoinLogTwo(67)
    COIN7 = CoinLogTwo(335)
    COIN8 = CoinLogThree(97)
    COIN9 = CoinLogOne(150)
    COIN10 = CoinLogOne(450)
    LIFE1 = Lives(10)
    LIFE2 = Lives(120)
    LIFE3 = Lives(230)

    #Adds sprites to respective sprite groups, coins and totalLives in list bc I'm not using a group collision for them
    coins = [COIN1, COIN2, COIN3, COIN4, COIN5, COIN6, COIN7, COIN8, COIN9, COIN10]
    totalLives = [LIFE1, LIFE2, LIFE3]
    carSprites = pygame.sprite.Group()
    carSprites.add([CAR1, CAR11, CAR2, CAR21, CAR3, CAR31, CAR32])
    logOneSprites = pygame.sprite.Group()
    logOneSprites.add([LOG1, LOG11])
    logTwoSprites = pygame.sprite.Group()
    logTwoSprites.add([LOG2, LOG21, LOG22, LOG23, LOG24])
    logThreeSprites = pygame.sprite.Group()
    logThreeSprites.add([LOG3, LOG31, LOG32])
    lilyPads = pygame.sprite.Group()
    lilyPads.add([LILYPAD1, LILYPAD2, LILYPAD3])
    bushSprites = pygame.sprite.Group()
    bushSprites.add([BUSH1, BUSH2, BUSH3, BUSH4, BUSH5, BUSH6, BUSH7])
    
    #Game variables
    coinCounter = 0
    game = False
    start = True
    lost = False
    won = False
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    FPS = 60
    CLOCK = pygame.time.Clock()
    
    #Collision function, called with every update
    def collision():
        #Detects if frog and car collides --> Pauses game (style), clears any player movements after collision, resets at the starting point
        if pygame.sprite.spritecollide(FROGGY, carSprites, False):
            pygame.mixer.Sound.play(CARHORN)
            pygame.time.delay(1000)
            pygame.event.clear(eventtype=[pygame.KEYDOWN])
            FROGGY.rect.x = 40
            FROGGY.rect.y = 290
            FROGGY.image = pygame.transform.rotate(FROG, -90)
            totalLives.remove(totalLives[len(totalLives) -1])
        #Detects if frog and log collide --> The frog takes the logs speed
        elif pygame.sprite.spritecollide(FROGGY, logOneSprites, False):
            FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
            FROGGY.rect.move_ip(0, LOG1.ydir)
        elif pygame.sprite.spritecollide(FROGGY, logTwoSprites, False):
            FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
            FROGGY.rect.move_ip(0, LOG2.ydir)
        elif pygame.sprite.spritecollide(FROGGY, logThreeSprites, False):
            FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
            FROGGY.rect.move_ip(0, LOG3.ydir)
        #Detects if frog and water collides --> Pauses game (style), clears any player movements after collision, resets at the starting point
        elif pygame.sprite.collide_rect(FROGGY, WATER):
            pygame.mixer.Sound.play(WATERFALL)
            pygame.time.delay(1000)
            pygame.event.clear(eventtype=[pygame.KEYDOWN])
            FROGGY.rect.x = 40
            FROGGY.rect.y = 290
            FROGGY.image = pygame.transform.rotate(FROG, -90)
            totalLives.remove(totalLives[len(totalLives) -1])
        #Detects if frog and bushes collides --> Pauses game (style), clears any player movements after collision, resets at the starting point
        elif pygame.sprite.spritecollide(FROGGY, bushSprites, False):
            pygame.mixer.Sound.play(COLLIDEBUSH)
            pygame.time.delay(1000)
            pygame.event.clear(eventtype=[pygame.KEYDOWN])
            FROGGY.rect.x = 40
            FROGGY.rect.y = 290
            FROGGY.image = pygame.transform.rotate(FROG, -90)
            totalLives.remove(totalLives[len(totalLives) -1])
       

    #Starting screen loop
    while start:
        surface.fill((0,0,0))
        #Paints the Initial start screen 
        gameTitle = pygame.font.Font('8-bit-hud.ttf', 38)
        gameStart = pygame.font.Font('8-bit-hud.ttf', 24)
        text1 = gameTitle.render(' FROGGER! ', True, (67, 209, 67))
        text2 = gameStart.render(' Press SPACE to ', True, (67, 209, 67))
        text3 = gameStart.render(' PLAY! ', True, (67, 209, 67))
        text1Rect = text1.get_rect()
        text2Rect = text2.get_rect()
        text3Rect = text3.get_rect()
        text1Rect.center = (370, 180)
        text2Rect.center = (370, 372)
        text3Rect.center = (370, 420)
        surface.blit(grass1, (0,0))
        surface.blit(grass3, (650,0))
        surface.blit(BUSH, (690, -40))
        surface.blit(BUSH, (690, 10))
        surface.blit(BUSH, (725, 80))
        surface.blit(BUSH, (725, 119))
        surface.blit(BUSH, (700, 145))
        surface.blit(BUSH, (725, 159))
        surface.blit(BUSH, (710, 190))
        surface.blit(BUSH, (725, 240))
        surface.blit(BUSH, (710, 295))
        surface.blit(BUSH, (710, 340))
        surface.blit(BUSH, (725, 400))
        surface.blit(BUSH, (710, 455))
        surface.blit(BUSH, (710, 510))
        FROGGY.draw()
        for bush in bushSprites:
            bush.draw()
        for lilypad in lilyPads:
            lilypad.draw()
        surface.blit(text1, text1Rect)
        surface.blit(text2, text2Rect)
        surface.blit(text3, text3Rect)
        
        
        pygame.display.update()
            
        for event in pygame.event.get():
            #If player presses space bar, end intro loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = True
                    start = False
                    break
            if event.type == pygame.locals.QUIT:
                pygame.quit() # ends pygame and closes window
                print("Thanks for playing!")
                sys.exit(0) #terminates program

    #Game Loop   
    while game:
        #pygame.mixer.Sound.play(GAMESTARTED)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                print("Thanks for playing!")
                sys.exit(0) 
            #Moves the frog and keeps frog in screen, also checks for collisions
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    FROGGY.rect.x += 80
                    FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
                    collision()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    FROGGY.rect.x -= 80
                    FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
                    collision()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    FROGGY.rect.y += 80
                    FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
                    collision()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    FROGGY.rect.y -= 80
                    FROGGY.rect.clamp_ip(pygame.Rect((30, 0), (740, 580)))
                    collision()
            #Keeps track of total live --> If lives run out, game loop starts and losing loop starts
            elif len(totalLives) < 1:
                game = False
                lost = True
            #Checks if froggy collides with lilypad --> game loop stops and winning loop starts
            elif pygame.sprite.spritecollide(FROGGY, lilyPads, False):
                game = False 
                won = True
                
            #Keeps track of the number of coins collected and removes collided coin from the game
            for c in coins:
                if (c.rect).colliderect(FROGGY) or (FROGGY.rect).colliderect(c.rect):
                    coins.remove(c)
                    pygame.mixer.Sound.play(COLLECTCOIN)
                    coinCounter += 1

        #Paints basic bakground elements
        surface.blit(grass1, (0,0))
        surface.blit(concrete, (90, 0))
        surface.blit(grass2, (330,0)) 
        surface.blit(grass3, (650,0))
        
        
        #CPaints the basic bushes at their respective positions
        surface.blit(BUSH, (690, -40))
        surface.blit(BUSH, (690, 10))
        surface.blit(BUSH, (725, 80))
        surface.blit(BUSH, (725, 119))
        surface.blit(BUSH, (700, 145))
        surface.blit(BUSH, (725, 159))
        surface.blit(BUSH, (710, 190))
        surface.blit(BUSH, (725, 240))
        surface.blit(BUSH, (710, 295))
        surface.blit(BUSH, (710, 340))
        surface.blit(BUSH, (725, 400))
        surface.blit(BUSH, (710, 455))
        surface.blit(BUSH, (710, 510))
    
        #Loops through all the given groups and updates the individual sprites
        for coin in coins:
            coin.update()
        for log1 in logOneSprites:
            log1.update()
        for log2 in logTwoSprites:
            log2.update()
        for log3 in logThreeSprites:
            log3.update()
        for car in carSprites:
            car.update()
        for bush in bushSprites:
            bush.update()
        FROGGY.update()
        
        #Checks for collision
        collision()
        
        #Loops through all the given groups and draws the individual sprites (order matters)
        WATER.draw()
        for log1 in logOneSprites:
            log1.draw()
        for log2 in logTwoSprites:
            log2.draw()
        for log3 in logThreeSprites:
            log3.draw()
        for coin in coins:
            coin.draw()
        for car in carSprites:
            car.draw()
        for lilypad in lilyPads:
            lilypad.draw()
        for bush in bushSprites:
            bush.draw()
        FROGGY.draw()
        for life in totalLives:
            life.draw()
        
        
        pygame.display.update()
        CLOCK.tick(FPS)
    
    #Losing loop
    while lost:
        #Paints losing screen
        gameLost = pygame.font.Font('8-bit-hud.ttf', 32)    
        gameRestart = pygame.font.Font('8-bit-hud.ttf', 28)
        gameRestart2 = pygame.font.Font('8-bit-hud.ttf', 28)
        text3 = gameLost.render(' YOU LOST ', True, white)
        text4 = gameRestart.render(' Press SPACE ', True, white)
        text5 = gameRestart2.render(' to play again! ', True, white)
        text3Rect = text3.get_rect()
        text4Rect = text4.get_rect()
        text5Rect = text5.get_rect()
        text3Rect.center = (370, 242)
        text4Rect.center = (370, 300)
        text5Rect.center = (370, 352)
        surface.fill(blue)
        surface.blit(text3, text3Rect)
        surface.blit(text4, text4Rect)
        surface.blit(text5, text5Rect)
        pygame.display.update()
        
        #Restarts the game or quits the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    lost = False
                    break
            if event.type == pygame.locals.QUIT:
                pygame.quit() # ends pygame and closes window
                print("Thanks for playing!")
                sys.exit(0) #terminates program
                
    #Winning loop
    while won: 
        #Paints won screen
        gameWon = pygame.font.Font('8-bit-hud.ttf', 32)    
        finalCoins = pygame.font.Font('8-bit-hud.ttf', 28)
        gameRestart1 = pygame.font.Font('8-bit-hud.ttf', 28)
        gameRestart2 = pygame.font.Font('8-bit-hud.ttf', 28)
        text1 = gameWon.render(' YOU WON! ', True, white)
        text2 = finalCoins.render(' with ' + str(coinCounter) + ' coins! ', True, white)
        text3 = gameRestart1.render(' Press SPACE ', True, white)
        text4 = gameRestart2.render(' to play again! ', True, white)
        text1Rect = text1.get_rect()
        text2Rect = text2.get_rect()
        text3Rect = text3.get_rect()
        text4Rect = text4.get_rect()
        text1Rect.center = (370, 222)
        text2Rect.center = (370, 280)
        text3Rect.center = (370, 330)
        text4Rect.center = (370, 380) 
        surface.fill(blue)
        surface.blit(text1, text1Rect)
        surface.blit(text2, text2Rect)
        surface.blit(text3, text3Rect)
        surface.blit(text4, text4Rect)
        pygame.display.update()
        
        #restarts the game or quits the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    break
            if event.type == pygame.locals.QUIT:
                pygame.quit() # ends pygame and closes window
                print("Thanks for playing!")
                sys.exit(0) #terminates program

#Calls main function to start everything
main()