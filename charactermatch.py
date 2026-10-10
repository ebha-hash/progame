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

pygame.display.update()

pos = None

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 0, 0), (pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        if pos is not None:
            
            if (pos[1] < 300 and pos[1] < 700) or (pos[1] < 500 and pos[1] < 300) or (pos[1] < 700 and pos[1] < 500):
                colour = (0, 210, 0)
            else:
                colour = (210, 0, 0)    
            pygame.draw.line(screen, colour, (pos), (pos2), 5)
            pygame.draw.circle(screen, colour, (pos2), 20, 0)
        pygame.display.update()
        pos = None
        #screen.fill((255, 255, 255))


