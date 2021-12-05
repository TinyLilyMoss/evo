import pygame
import sys
import random

pygame.init()
print("pygame has been booted")

## the pygame parts are only here because eventually this will render things
## maybe it can change color based on how close your get

screen = pygame.display.set_mode((100, 100))

pygame.display.set_caption('new version')
clock = pygame.time.Clock()

WORLDSPVALUE = (random.randint(0, 10))
WORLDSTRVALUE = (random.randint(0, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    speed = (random.randint(0, 10))
    stre = (random.randint(0, 10))

    print (speed, stre, WORLDSPVALUE, WORLDSTRVALUE)

    if speed + stre < WORLDSPVALUE + WORLDSTRVALUE:
        print("lame guy")
    if speed + stre > WORLDSPVALUE + WORLDSTRVALUE:
        print("awesome guy")
        break
    if speed + stre == WORLDSPVALUE + WORLDSTRVALUE:
        print("satisfactory guy")
        break

    pygame.display.update()
    clock.tick(1)

print ("congrats on making a cool guy!")