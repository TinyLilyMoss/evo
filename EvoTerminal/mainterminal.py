## coming soon - [~] UI, [V] enviornment custimization, [] generations, [] more variables for evolving
## [] and a less data oriented form of displaying the outcome of events
## data oriented outcomes will be toggleable in the finished UI build 

## imports 

import pygame
import sys
import random

pygame.init()

## print command to avoid using in blocks

def MSG():
    print ("_________________________________________________")
    print ("variable comparison")
    print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)
    print (foodneed, FOOD)
    print (animal, animalRNG)
    print ("_________________________________________________")
    print (f"the amount of creatures that are in your enviornment is {animal}")
    print ("_________________________________________________")

## print command to avoid using in blocks

def MSG2():
    print ("_________________________________________________")
    print ("variable comparison")
    print (x, y, WORLDSPVALUE, WORLDSTRVALUE)
    print (foodneed, FOOD)
    print (animal, animalRNG)
    print ("_________________________________________________")
    print (f"the amount of creatures that are in your enviornment is {animal}")
    print ("_________________________________________________")

## line print command to make the UI more readable 

def line():
    print("_________________________________________________________________________________________")

## all enviornmental values

CREATURESDEAD = 0 ## for later 
x = []
y = []
animal = 0 
line()

## number of creatures allowed in the enviormnet is set here 

animalRNG = int(input("""please enter the number of creatures allowed in your enviornment 
between 0-100 you want to allow in your enviornment! type 999 for a random value! - """))
if animalRNG == 999:
    animalRNG = (random.randint(0, 100))

line()

## value of speed in the enviornment 

WORLDSPVALUE = int(input("""please enter the value of speed in your enviornment
between 0-10! type 999 for a random value! - """))
if WORLDSPVALUE == 999:
    WORLDSPVALUE = (random.randint(0, 10))

line()

## value of strength in the enviorment

WORLDSTRVALUE = int(input("""please enter the value of strength in your enviornment
between 0-10! type 999 for a random value! - """))
if WORLDSTRVALUE == 999:
    WORLDSTRVALUE = (random.randint(0, 10))

line()

## amount of food in the enviorment 

FOOD = int(input("""please enter the amount of food in your enviornment
between 0-10! type 999 for a random value! - """))
if FOOD == 999:
    FOOD = (random.randint(0, 10))

line()

## allowing or disallowing user input mid code

constant = int(input("""if you would like to generate creatures with no pauses for user 
input, type one, zero to stop for user input! - """))

line()

## tick speed when not given a variable from the user

guy = 1

## user input for TPS 

if constant == 1: 
    guy = int(input("please type the ticks per second at which you want to generate creatures - "))

line()

## value for updating to the next generation 

win = 0

clock = pygame.time.Clock()

while True:

    ## sets the random values for the creature to evolve with 

    speed = (random.randint(0, 10))
    stre = (random.randint(0, 10))
    foodneed = (random.randint(0, 10))

    ## overpopulation 

    if animal > animalRNG:
        print ("the enviornment is overpopulated, two of your creatures have died!")
        animal -= 2
    
## RNG birth

    while win == 0:

        ## sets the birth creatures values

        speed = (random.randint(0, 10))
        stre = (random.randint(0, 10))
        foodneed = (stre/ 2) + (speed / 2)

        ## prints data values for studying/troubleshootiing

        MSG()

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
                        win += 1
                        print ("moving on")
                        line()

            elif stre  == WORLDSTRVALUE:
                print("satisfactory guy (SP)")

                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                    
                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
                    win += 1
                    print ("moving on")
                    line()

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
                            win += 1
                            print ("moving on")
                            line()

                elif stre  == WORLDSTRVALUE:
                    print("satisfactory guy (SP)")

                    if foodneed < FOOD: 
                        print ("your creature has died of starvation")

                    elif foodneed >= FOOD:
                        print ("Congrats! you creature has lived")
                        animal += 1  
                        win += 1
                        print ("moving on")
                        line()

## user input/tickspeed

        if constant == 1: 
            clock.tick(int(guy))

        if constant == 0:
            type = input("""
_________________________________________________
press enter to create another creature""")
            clock.tick(int(guy))

## generation decent

    while win >= 1:

        ## sets the decent creatures values

        x = speed
        x += (random.randint(-1, win))
        y = stre
        y += (random.randint(-1, win))
        if win > 5:
            win -= 2
        
        ## data values for decent creatures

        MSG2()
        
        if y < WORLDSTRVALUE:
            print("creature has died (STR)")

        elif y > WORLDSTRVALUE:
            print("awesome guy (STR)")

            if x < WORLDSTRVALUE:
                print("creature has died (SP)")
                
            elif x > WORLDSPVALUE:
                    print("awesome guy (SP) ")

                    if foodneed < FOOD: 
                        print ("your creature has died of starvation")

                    elif foodneed >= FOOD:
                        print ("Congrats! you creature has lived")
                        animal += 1
                        win += 1

            elif y  == WORLDSTRVALUE:
                print("satisfactory guy (SP)")

                if foodneed < FOOD: 
                    print ("your creature has died of starvation")

                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1

        elif y == WORLDSTRVALUE:
            print("satisfactory guy (STR)")

            if x < WORLDSTRVALUE:
                print("creature has died (SP)")

            elif x > WORLDSPVALUE:
                    print("awesome guy (SP) ")

                    if foodneed < FOOD: 
                        print ("your creature has died of starvation")

                    elif foodneed >= FOOD:
                        print ("Congrats! you creature has lived")
                        animal += 1
                        win += 1

            elif y == WORLDSTRVALUE:
                print("satisfactory guy (SP)")

                if foodneed < FOOD: 
                    print ("your creature has died of starvation")

                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
        
## user input/tickspeed

        if constant == 1: 
            clock.tick(int(guy))

        if constant == 0:
            type = input("""
_________________________________________________
press enter to create another creature""")
            clock.tick(int(guy))
                    