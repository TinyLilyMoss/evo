print("balls")

## this is just to test github :)

import pygame
import sys
import random


pygame.init()
print("pygame has been booted")

a = 0
b = 0
c = 0

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Evolution base')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    x = (random.randint(0, 1))
    y = (random.randint(0, 1))
    la1 = y
    la2 = x
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
    print(a, b, c)

    if win == 1:
        color = pygame.Surface((1000, 1000))
        color.fill((255, 0, 0))
        screen.blit(color, (0, 0))
    if win == 0:
        color = pygame.Surface((1000, 1000))
        color.fill((0, 0, 255))
        screen.blit(color, (0, 0))
    if win == 2:
        color = pygame.Surface((1000, 1000))
        color.fill((0, 255, 0))
        screen.blit(color, (0, 0))
    pygame.display.update()
    clock.tick(1)
