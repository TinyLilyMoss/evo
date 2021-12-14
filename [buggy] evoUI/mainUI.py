## coming soon - [~] UI, [V] enviornment custimization, [] generations, [] more variables for evolving
## [] and a less data oriented form of displaying the outcome of events
## data oriented outcomes will be toggleable in the finished UI

import pygame
import sys
import random

## adding pygame shit for the UI, the UI wont be especially functional until later builds

pygame.init()
screen = pygame.display.set_mode((500, 500))

## allows you to swap between modes

termUI = int(input("type 1 for the terminal build, and 0 for the UI build!"))

## clock ticking 

clock = pygame.time.Clock()

## all enviornmental values



if termUI == 1:
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
    guy = 1
    if constant == 1: 
        guy = int(input("please type the ticks per second at which you want to generate creatures - "))
    print("_________________________________________________________________________________________")

if termUI == 0:
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
    


white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render("enviornmental" , True, white)
textset = font.render("settings", True, white)
food = font.render("food amount" , True, white)
food2 = font.render(str(FOOD) , True, white)
ncreature = font.render("overpopulation" , True, white)
ncreature2 = font.render(str(animalRNG) , True, white)

## infinite loop for UI 

while termUI == 0: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    green = pygame.Surface((300, 500))
    green.fill((10, 100, 10))
    screen.blit(green, (0, 0))
    
    linebottom = pygame.Surface((200, 3))
    linebottom.fill((255, 255, 255))
    screen.blit(linebottom, (300, 90))

    lineside = pygame.Surface((3, 500))
    lineside.fill((255, 255, 255))
    screen.blit(lineside, (300, 0))

    screen.blit(text, (330, 30))
    screen.blit(textset, (350, 50))

    screen.blit(food, (330, 100))
    screen.blit(food2, (330, 130))

    screen.blit(ncreature, (330, 160))
    screen.blit(ncreature2, (330, 190))

    pygame.display.update()
    clock.tick(60)

while termUI == 1:

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
