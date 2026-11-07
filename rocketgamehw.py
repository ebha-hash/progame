import pygame
import os
import time
import random

pygame.init()

WIDTH, HEIGHT = 700, 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

i1 = os.path.join("images", "rocket.png")
i2 = os.path.join("images", "bg.png")
i3 = os.path.join("images", "asteroid.png")
i4 = os.path.join("images", "star.png")

rocket = pygame.image.load(i1)
space = pygame.image.load(i2)
ast = pygame.image.load(i3)
star = pygame.image.load(i4)

rocketw, rocketh = rocket.get_size()
astw, asth = ast.get_size()
starw, starh = star.get_size()

rocketx = 250
rockety = 450

astx = random.randint(0, 600)
asty = -50

starx = random.randint(0, 650)
stary = -100

keys = [False, False, False, False]

while rockety < 900:
    screen.blit(space, (0, 0))
    screen.blit(rocket, (rocketx, rockety))
    screen.blit(ast,(astx, asty))
    screen.blit(star,(starx, stary))

    pygame.display.update()

    asty += 5
    stary += 2

    if asty > HEIGHT:
        asty - 100
        astx = random.randint(0, 600)

    if stary > HEIGHT:
        stary - 100
        starx = random.randint(0,650)

    rocketrect = pygame.Rect(rocketx,rockety,rocketw,rocketh)
    astrect = pygame.Rect(astx, asty, astw, asth)
    starrect = pygame.Rect(starx, stary, starw, starh)

    if rocketrect.colliderect(astrect):
        tunning = False
    if rocketrect.colliderect(starrect):
        rockety -= 75

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
            if event.key == pygame.K_LEFT:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] = False
            if event.key == pygame.K_LEFT:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        if rockety > 0:
            rockety -= 5
    elif keys[1]:
        if rockety < 495:
            rockety += 5
    elif keys[2]:
        if rocketx > 0:
            rocketx -= 5
    elif keys[3]:
        if rocketx < 690:
            rocketx += 5

    rockety += 3
    time.sleep(0.05)
