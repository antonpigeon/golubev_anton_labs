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

# dog functions
def draw_dog_head(surface: pygame.Surface, color: pygame.Color, middle: tuple[int, int], side: int):
    pygame.draw.rect(surface, color, (middle[0] - side//2, middle[1] - side//2, side, side))

    pygame.draw.circle(surface, color, (middle[0] - side//2, middle[1] - side//3), side//8)
    pygame.draw.circle(surface, 'black', (middle[0] - side//2, middle[1] - side//3), side//8, width=1)

    pygame.draw.circle(surface, color, (middle[0] + side//2, middle[1] - side//3), side//8)
    pygame.draw.circle(surface, 'black', (middle[0] + side//2, middle[1] - side//3), side//8, width=1)
def draw_dog_body():
    return
def draw_dog_forward_leg():
    return
def draw_dog_back_leg():
    return
def draw_dog(surface: pygame.Surface, color: pygame.Color, left_top: tuple[int, int],
             width: int, facing_left=True, ):
    """
    рисует собаку как в примере
    :param left_top: координаты левого верхнего угла изображения (x, y)
    :param width: ширина изображения (высота вычисляется соответственно)
    :param surface: окно, в котором рисовать
    :param color: цвет забора
    :param facing_left: True - собака смотрит налево, False - направо. По умолчанию True
    :return: None
    """
    height = int(2/3 * width)
    pygame.draw.rect(screen, 'grey', (left_top[0], left_top[1], width, height))
    draw_dog_head(surface, color, (left_top[0] + width//5, left_top[1] + width//7), 2*width//7)

FPS = 30
screen = pygame.display.set_mode((600, 600))

pygame.draw.rect(screen, 'lightblue', (0, 0, 600, 300))  # небо
pygame.draw.rect(screen, 'lightgreen', (0, 300, 600, 300))  # трава
draw_fence(screen, 'yellow', (50, 100, 400, 200), 10, 20, 5)
draw_dog(screen, 'blue', (100, 400), 200)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()