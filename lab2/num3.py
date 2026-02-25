import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 800))

# фон
screen.fill((255, 255, 255))

# тело
ellipse(screen, (100, 150, 255), (50, 600, 300, 400))

# голова
circle(screen, (255, 220, 180), (200, 480), 150)

# глаза
circle(screen, (255, 255, 255), (150, 430), 15)
circle(screen, (255, 255, 255), (250, 430), 15)
circle(screen, (0, 0, 0), (150, 430), 7)
circle(screen, (0, 0, 0), (250, 430), 7)

# улыбка
polygon(screen, (255, 0, 0), [(140, 510), (260, 510), (200, 530)])

# левая рука
line(screen, (255, 220, 180), (90, 675), (30, 480), 8)
line(screen, (255, 220, 180), (30, 220), (30, 480), 8)

# правая рука
line(screen, (255, 220, 180), (300, 675), (370, 480), 8)
line(screen, (255, 220, 180), (370, 220), (370, 480), 8)


# тело
ellipse(screen, (75, 150, 57), (550, 600, 300, 400))

# голова
circle(screen, (105, 55, 0), (700, 480), 150)

# глаза
circle(screen, (255, 255, 255), (650, 430), 15)
circle(screen, (255, 255, 255), (750, 430), 15)
circle(screen, (0, 0, 0), (650, 430), 7)
circle(screen, (0, 0, 0), (750, 430), 7)

# улыбка
polygon(screen, (255, 255, 255), [(640, 510), (760, 510), (700, 530)])

# левая рука
line(screen, (105, 55, 0), (590, 675), (530, 480), 8)
line(screen, (105, 55, 0), (530, 220), (530, 480), 8)

# правая рука
line(screen, (105, 55, 0), (800, 675), (870, 480), 8)
line(screen, (105, 55, 0), (870, 220), (870, 480), 8)


poster_x = 0
poster_y = 150
poster_width = 900

# Сам плакат
rect(screen, (255, 255, 200), (poster_x, poster_y, poster_width, 120))
rect(screen, (0, 0, 0), (poster_x, poster_y, poster_width, 120), 4)


# Надпись на плакате
font = pygame.font.Font(None, 48)
text = font.render("PYTHON is AMAZING!", True, (255, 0, 0))
text_rect = text.get_rect(center=(poster_x + poster_width//2, poster_y + 60))
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