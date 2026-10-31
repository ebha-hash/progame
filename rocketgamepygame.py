import pygame
import os
import time

pygame.init()

WIDTH, HEIGHT = 700, 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

i1 = os.path.join("images", "rocket.png")
i2 = os.path.join("images", "bg.png")

rocket = pygame.image.load(i1)
space = pygame.image.load(i2)

rocketx = 250
rockety = 450

keys = [False, False, False, False]

while rockety < 900:
    screen.blit(space, (0, 0))
    screen.blit(rocket, (rocketx, rockety))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
            if event.key == pygame.K_LEFT:
                keys[2] == True
            if event.key == pygame.K_RIGHT:
                keys[3] == True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] == False
            if event.key == pygame.K_LEFT:
                keys[2] == False
            if event.key == pygame.K_RIGHT:
                keys[3] == False

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
