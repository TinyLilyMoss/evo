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
animal = 0 
animalRNG = (random.randint(0, 10))

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

    msg = f"the amount of creatures that are in your enviornment is {animal}"
    print ("_________________________________________________")
    print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)
    print ("/")
    print (msg)
    print ("/")
    ## the actual evolution part of the code

    if animal > animalRNG:
        print ("the enviornment is overpopulated, two of your creatures have died!")
        animal -= 2

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
                    print ("Congrats! you creature has lived")
                    animal += 1
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            if foodneed >= FOOD:
                print ("Congrats! you creature has lived")
                animal += 1
    elif stre  == WORLDSTRVALUE:
        print("satisfactory guy (STR)")
        if speed < WORLDSTRVALUE:
            print("lame guy (SP)")
        elif speed > WORLDSPVALUE:
                print("awesome guy (SP) ")
                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                if foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            if foodneed >= FOOD:
                print ("Congrats! you creature has lived")
                animal += 1

    pygame.display.update()
    clock.tick(1)