import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# фон
screen.fill((255, 255, 255))


# тело
ellipse(screen, (100, 150, 255), (100, 600, 400, 400))  # Синяя одежда

# голова
circle(screen, (255, 220, 180), (300, 480), 150)

# глаза
circle(screen, (255, 255, 255), (250, 430), 15)
circle(screen, (255, 255, 255), (350, 430), 15)
circle(screen, (0, 0, 0), (250, 430), 7)
circle(screen, (0, 0, 0), (350, 430), 7)

# улыбка
polygon(screen, (255, 0, 0), [(240, 510), (360, 510), (300, 530)])


# левая рука
line(screen, (255, 220, 180), (150, 675), (80, 480), 8)
line(screen, (255, 220, 180), (80, 220), (80, 480), 8)

# правая рука
line(screen, (255, 220, 180), (400, 675), (520, 480), 8)
line(screen, (255, 220, 180), (520, 220), (520, 480), 8)

# плакат
rect(screen, (255, 255, 200), (60, 150, 480, 120))
rect(screen, (0, 0, 0), (60, 150, 480, 120), 4)

# надпись на плакате
font = pygame.font.Font(None, 48)
text = font.render("PYTHON is AMAZING", True, (255, 0, 0))  # Красный текст
text_rect = text.get_rect(center=(300, 210))
screen.blit(text, text_rect)



pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()