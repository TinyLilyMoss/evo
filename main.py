## coming soon - UI, enviornment custimization, generations, and more variables for evolving
## and a less data oriented form of displaying the outcome of events
## data oriented outcomes will be toggleable in the finished UI

import pygame
import sys
import random

pygame.init()

## the pygame parts are only here because eventually this will render things
## maybe it can change color based on how close your get

## all enviornmental values

animal = 0 
animalRNG = (random.randint(0, 100))
WORLDSPVALUE = (random.randint(0, 10))
WORLDSTRVALUE = (random.randint(0, 10))
FOOD = (random.randint(0, 10))

clock = pygame.time.Clock()

while True:

    ## sets the random values for the creature to evolve with 

    speed = (random.randint(0, 10))
    stre = (random.randint(0, 10))
    foodneed = (random.randint(0, 10))

    ## prints the data in a semi readable form!

    msg = f"the amount of creatures that are in your enviornment is {animal}"
    print ("_________________________________________________")
    print ("variable comparison")
    print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)
    print (foodneed, FOOD)
    print (animal, animalRNG)
    print ("_________________________________________________")
    print (msg)
    print ("_________________________________________________")

    ## overpopulation 

    if animal > animalRNG:
        print ("the enviornment is overpopulated, two of your creatures have died!")
        animal -= 2
    
    ## the actual evolution part of the code

    if stre < WORLDSTRVALUE:
        print("creature has died (STR)")
    elif stre > WORLDSTRVALUE:
        print("awesome guy (STR)")
        if speed < WORLDSTRVALUE:
            print("creature has died (SP)")
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
            print("creature has died (SP)")
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

## user input to make new creature 

    type = input("""
_________________________________________________
press enter to create another creature""")
    clock.tick(50)