import pygame
import sys
import random

## experimenting with making the code cleaner

def balls():
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