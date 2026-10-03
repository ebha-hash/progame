import pygame
import os

pygame.init()

WIDTH, HEIGHT = 900, 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((125, 0, 0))

pygame.display.set_caption("Match the Following")

pygame.display.update()

i1 = os.path.join("images", "ludo.png")
i2 = os.path.join("images", "subwaysurfers.png")
i3 = os.path.join("images", "candycrush.jpg")
i4 = os.path.join("images", "templerun.png")

ludo = pygame.image.load(i1)
subwsurf = pygame.image.load(i2)
candycrush = pygame.image.load(i3)
templerun = pygame.image.load(i4)

screen.blit(ludo, (250, 200))
screen.blit(subwsurf, (250, 400))
screen.blit(candycrush, (250, 600))
screen.blit(templerun, (250, 800))

font=pygame.font.SysFont("Arial", 36)

text1 = font.render("Ludo", True, (0, 0, 200))
text2 = font.render("Subway Surfers", True, (0, 0, 200))
text3 = font.render("Candy Crush", True, (0, 0, 200))
text4 = font.render("Temple Run", True, (0, 0, 200))

screen.blit(text3, (500, 200))
screen.blit(text1, (500, 400))
screen.blit(text4, (500, 600))
screen.blit(text2, (500, 800))

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 0, 0), (pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0, 0, 0), (pos), (pos2), 5)
        pygame.draw.circle(screen, (0, 0, 0), (pos2), 20, 0)
        pygame.display.update()

