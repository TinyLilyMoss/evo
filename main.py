## DAMN BITCH, IMPORT THOSE MODULES ',:|

import pygame
import sys
import random

## bots up pygame... and then tells you that its been booted... 

pygame.init()
print("pygame has been booted")

## variables to get data on the RNG, don't put these in the while loop, it just resets them

a = 0
b = 0
c = 0

## sets the display size

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Evolution base') ## captions the window 
clock = pygame.time.Clock() ## ???

while True:

    ## allows you to quit the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    ## the random number generator, it works by the power of magic and pure hormones

    x = (random.randint(0, 1))
    y = (random.randint(0, 1))
    la1 = y
    la2 = x

    ## this just decide who wins, or whether or not its a draw

    if la1 < la2:
        print("la2 has won!")
        win = 1
        a += 1
    if la1 > la2:
        print("la1 has won")
        win = 0
        b += 1
    if la1 == la2:
        print("must have been a draw")
        win = 2
        c += 1
    print(a, b, c) ## prints the win to loss ratio, mostly just to test how random the RNG is? 

    ## renders certain things based on who wins, 

    if win == 1:
        color = pygame.image.load("assets/CATEJAM.png") ## lol 
        screen.blit(color, (0, 0))
    if win == 0:
        color = pygame.Surface((1000, 1000))
        color.fill((0, 0, 255))
        screen.blit(color, (0, 0))
    if win == 2:
        color = pygame.Surface((1000, 1000))
        color.fill((0, 255, 0))
        screen.blit(color, (0, 0))
    pygame.display.update() # updates the display (it does this because I asked nicely)
    clock.tick(1) ## tps, change this to slow down or speed up the RNG process
