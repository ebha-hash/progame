import pygame
import os

pygame.init()

WIDTH, HEIGHT = 900, 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((125, 0, 0))

pygame.display.set_caption("Match the Following - Characters")

pygame.display.update()

i1 = os.path.join("images", "ninja.png")
i2 = os.path.join("images", "wizard.png")
i3 = os.path.join("images", "archer.png")
i4 = os.path.join("images", "ninjasword.png")
i5 = os.path.join("images", "wand.png")
i6 = os.path.join("images", "bow.png")

ninja = pygame.image.load(i1)
wizard = pygame.image.load(i2)
archer = pygame.image.load(i3)
sword = pygame.image.load(i4)
wand = pygame.image.load(i5)
bow = pygame.image.load(i6)

screen.blit(ninja, (200, 250))
screen.blit(wizard, (200, 450))
screen.blit(archer, (200, 650))
screen.blit(wand, (500, 250))
screen.blit(bow, (500, 450))
screen.blit(sword, (500, 650))

ninjaR = pygame.Rect(200, 250, 100, 50)
wizardR = pygame.Rect(200, 450, 100, 50)
archerR = pygame.Rect(200, 650, 100, 50)
wandR = pygame.Rect(500, 250, 50, 50)
bowR = pygame.Rect(500, 450, 50, 50)
swordR = pygame.Rect(500, 650, 50, 50)

images = [(ninjaR, swordR), (wizardR, wandR), (archerR, bowR)]

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