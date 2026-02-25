import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((255, 255, 0))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 2)

circle(screen, (255, 255, 255), (130, 140), 25)
circle(screen, (0, 0, 0), (130, 140), 25, 2)

circle(screen, (0, 0, 0), (130, 140), 10)

circle(screen, (255, 255, 255), (270, 140), 20)
circle(screen, (0, 0, 0), (270, 140), 20, 2)

circle(screen, (0, 0, 0), (270, 140), 8)

line(screen, (0, 0, 0), (100, 80), (160, 120), 5)  # Левая бровь
line(screen, (0, 0, 0), (300, 80), (240, 120), 5)  # Правая бровь


ellipse(screen, (255, 0, 0), (140, 230, 120, 40))
ellipse(screen, (0, 0, 0), (140, 230, 120, 40), 2)


rect(screen, (255, 255, 255), (170, 235, 15, 25))
rect(screen, (255, 255, 255), (215, 235, 15, 25))


pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()