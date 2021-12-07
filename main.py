## coming soon - UI, enviornment custimization, generations, and more variables for evolving
## and a less data oriented form of displaying the outcome of events
## data oriented outcomes will be toggleable in the finished UI

import pygame
import sys
import random

pygame.init()
print("pygame has been booted")

## the pygame parts are only here because eventually this will render things
## maybe it can change color based on how close your get

screen = pygame.display.set_mode((100, 100))

rngSTR = 0 ## this will be used later on for a UI to set up an enviornment for the creature 
rngSPE = 0
rngFOOD = 0

pygame.display.set_caption('new version')
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 10)

WORLDSPVALUE = (random.randint(0, 10))
WORLDSTRVALUE = (random.randint(0, 10))
FOOD = (random.randint(0, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    ## sets the random values for the creature to evolve with 

    speed = (random.randint(0, 10))
    stre = (random.randint(0, 10))
    foodneed = (random.randint(0, 10))

    print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)

    ## the actual evolution part of the code

    if stre < WORLDSTRVALUE:
        print("lame guy (STR)")
    elif stre > WORLDSTRVALUE:
        print("awesome guy (STR)")
        if speed < WORLDSTRVALUE:
            print("lame guy (SP)")
        elif speed > WORLDSPVALUE:
                print("awesome guy (SP) ")
                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                if foodneed >= FOOD:
                    break
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            if foodneed >= FOOD:
                break
    elif stre  == WORLDSTRVALUE:
        print("satisfactory guy (STR)")
        if speed < WORLDSTRVALUE:
            print("lame guy (SP)")
        elif speed > WORLDSPVALUE:
                print("awesome guy (SP) ")
                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                if foodneed >= FOOD:
                    break
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            if foodneed >= FOOD:
                break

    pygame.display.update()
    clock.tick(1)

## prints when the creature is satisfactory :) 

print ("your creature has past all tests!")
print ("congrats on making a cool guy!")