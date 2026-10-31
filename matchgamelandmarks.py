import pygame
import os

pygame.init()

WIDTH, HEIGHT = 750, 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((125, 0, 0))

pygame.display.set_caption("Match the Following - Landmarks")

pygame.display.update()

i1 = os.path.join("images", "eiftow.png")
i2 = os.path.join("images", "colo.png")
i3 = os.path.join("images", "statoflib.png")
i4 = os.path.join("images", "france.png")
i5 = os.path.join("images", "italy.png")
i6 = os.path.join("images", "us.png")

eiftow = pygame.image.load(i1)
colo = pygame.image.load(i2)
statoflib = pygame.image.load(i3)
france = pygame.image.load(i4)
italy = pygame.image.load(i5)
us = pygame.image.load(i6)

screen.blit(eiftow, (200, 250))
screen.blit(colo, (200, 450))
screen.blit(statoflib, (200, 650))
screen.blit(italy, (500, 250))
screen.blit(us, (500, 450))
screen.blit(france, (500, 650))

eiftowR = pygame.Rect(200, 250, 100, 50)
coloR = pygame.Rect(200, 450, 100, 50)
statoflibR = pygame.Rect(200, 650, 100, 50)
italyR = pygame.Rect(500, 250, 50, 50)
usR = pygame.Rect(500, 450, 50, 50)
franceR = pygame.Rect(500, 650, 50, 50)

images = [(eiftowR, franceR), (coloR, italyR), (usR, statoflibR)]

startpos = None
endpos = None
dragging = False

pygame.display.update()

pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
           pos = event.pos
           for i,w in images:
               if i.collidepoint(pos):
                   startpos = i.center
                   dragging = True
                   break
        pygame.display.update()       
        '''pos2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 0, 0), (pos2), 20, 0)
        if pos == None:
            pos = pos2
        else:

            if (pos[1] <= 300 and pos2[1] <= 700) or (pos[1] <= 500 and pos2[1] <= 300) or (pos[1] <= 700 and pos2[1] <= 500):
                colour = (0, 210, 0)
            else:
                colour = (210, 0, 0)
            pygame.draw.line(screen, colour, (pos), (pos2), 5)
        pygame.display.update()
        #screen.fill((255, 255, 255))'''
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and dragging:
            endpos = event.pos
            correct = False
            for i,w in images:
                if i.collidepoint(startpos):
                    if w.collidepoint(endpos):
                        correct = True
                        break

            if correct:
                colour = (0, 210, 0)
            else:
                colour = (210, 0, 0)

            pygame.draw.line(screen, colour, startpos, endpos, 5)

            pygame.display.update()

            dragging = False
            startpos = None
            endpos = None