import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill('white')

pygame.draw.circle(screen, 'yellow', (200, 200), 100)
pygame.draw.polygon(screen, 'black', ((110, 110), (105, 115), (175, 165), (180, 160), (110, 110)))
pygame.draw.polygon(screen, 'black', ((220, 160), (223, 167), (291, 140), (288, 133), (220, 160)))
pygame.draw.rect(screen, 'black', (150, 250, 100, 20))
pygame.draw.circle(screen, 'red', (240, 175), 15)
pygame.draw.circle(screen, 'black', (240, 175), 8)
pygame.draw.circle(screen, 'red', (160, 175), 17)
pygame.draw.circle(screen, 'black', (160, 175), 8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
