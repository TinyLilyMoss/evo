## coming soon - [~] UI, [V] enviornment custimization, [] generations, [] more variables for evolving
## [] and a less data oriented form of displaying the outcome of events
## data oriented outcomes will be toggleable in the finished UI

import pygame
import sys
import random

pygame.init()

## the pygame parts are only here because eventually this will render things
## maybe it can change color based on how close your get

## all enviornmental values

animal = 0 
animalRNG = int(input("""please enter the number of creatures allowed in your enviornment 
between 0-100 you want to allow in your enviornment! type 999 for a random value! - """))
if animalRNG == 999:
    animalRNG = (random.randint(0, 100))
print("_________________________________________________________________________________________")
WORLDSPVALUE = int(input("""please enter the value of speed in your enviornment
between 0-10! type 999 for a random value! - """))
if WORLDSPVALUE == 999:
    WORLDSPVALUE = (random.randint(0, 10))
print("_________________________________________________________________________________________")
WORLDSTRVALUE = int(input("""please enter the value of strength in your enviornment
between 0-10! type 999 for a random value! - """))
if WORLDSTRVALUE == 999:
    WORLDSTRVALUE = (random.randint(0, 10))
print("_________________________________________________________________________________________")
FOOD = int(input("""please enter the amount of food in your enviornment
between 0-10! type 999 for a random value! - """))
if FOOD == 999:
    FOOD = (random.randint(0, 10))
print("_________________________________________________________________________________________")

constant = int(input("""if you would like to generate creatures with no pauses for user 
input, type one, zero to stop for user input! - """))
print("_________________________________________________________________________________________")
if constant == 1: 
    guy = int(input("please type the ticks per second at which you want to generate creatures - "))
print("_________________________________________________________________________________________")

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
                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            elif foodneed >= FOOD:
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
                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
        elif stre  == WORLDSTRVALUE:
            print("satisfactory guy (SP)")
            if foodneed < FOOD: 
                print ("your creature has died of starvation")
            elif foodneed >= FOOD:
                print ("Congrats! you creature has lived")
                animal += 1  

## user input to make new creature 

    if constant == 0:
        type = input("""
_________________________________________________
press enter to create another creature""")
    clock.tick(guy)
