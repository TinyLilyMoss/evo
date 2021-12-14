import pygame
import sys
import random

pygame.init()

animal = 0 
animalRNG = (random.randint(0, 100))
WORLDSPVALUE = (random.randint(0, 10))
WORLDSTRVALUE = (random.randint(0, 10))
FOOD = (random.randint(0, 10))
guy = 1
win = 0
CREATURESDEAD = 0
x = []
y = []
z = []
a = []
b = []
c = []

clock = pygame.time.Clock()

print ("123")
while True:

    ## prints the data in a semi readable form!
    ## overpopulation 
    
    if animal > animalRNG:
        animal -= 2  

    ## the actual evolution part of the code

    while win == 0:
        speed = (random.randint(0, 10))
        stre = (random.randint(0, 10))
        foodneed = (random.randint(0, 10))
        print ("test")
        msg = f"the amount of creatures that are in your enviornment is {animal}"
        print ("_________________________________________________")
        print ("variable comparison")
        print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)
        print (foodneed, FOOD)
        print (animal, animalRNG)
        print ("_________________________________________________")
        print (msg)
        print ("_________________________________________________")
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
            elif stre  == WORLDSTRVALUE:
                print("satisfactory guy (SP)")
                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1
                    win += 1
                    print ("moving on")
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
                elif stre  == WORLDSTRVALUE:
                    print("satisfactory guy (SP)")
                    if foodneed < FOOD: 
                        print ("your creature has died of starvation")
                    elif foodneed >= FOOD:
                        print ("Congrats! you creature has lived")
                        animal += 1  
                        win += 1
                        print ("moving on")
            clock.tick(guy)

    while win == 1:
        x = speed 
        x += (random.randint(-1, 1))
        y = stre
        y += (random.randint(-1, 1))
        msg = f"the amount of creatures that are in your enviornment is {animal}"
        print ("_________________________________________________")
        print ("variable comparison")
        print (x, y, WORLDSPVALUE, WORLDSTRVALUE)
        print (foodneed, FOOD)
        print (animal, animalRNG)
        print ("_________________________________________________")
        print (msg)
        print ("_________________________________________________")
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
            elif y == WORLDSTRVALUE:
                print("satisfactory guy (SP)")
                if foodneed < FOOD: 
                    print ("your creature has died of starvation")
                elif foodneed >= FOOD:
                    print ("Congrats! you creature has lived")
                    animal += 1  
        clock.tick(guy)
