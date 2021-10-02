import pygame
import random

pygame.init()


def draw_fence(surface: pygame.Surface, color: pygame.Color, rect: pygame.Rect,
               starting_x: int, step: int, max_offset: int):
    """
    рисует забор - прямоугольник с вертикальными линиями, изображающими стык досок
    :param surface: окно, в котором рисовать
    :param color: цвет забора
    :param rect: (x левого верхнего угла, y левого верхнего угла, длина, ширина)
    :param starting_x: отступ первой вертикальной линии
    :param step: расстояние между вертикальными линиями
    :param max_offset: максимальное расстояние, на которое линия может быть случайно сдвинута
    :return: NONE
    """
    pygame.draw.rect(surface, color, rect)
    x = rect[0] + starting_x
    while x <= rect[0] + rect[2]:
        dx = random.randint(-max_offset, max_offset)
        pygame.draw.line(surface, 'black', (x + dx, rect[1]), (x + dx, rect[1] + rect[3]))
        x += step


FPS = 30
screen = pygame.display.set_mode((600, 600))

pygame.draw.rect(screen, 'lightblue', (0, 0, 600, 300))  # небо
pygame.draw.rect(screen, 'lightgreen', (0, 300, 600, 300))  # трава
draw_fence(screen, 'yellow', (0, 100, 600, 200), 10, 20, 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()