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


def draw_ellipses(surface: pygame.Surface, color: pygame.Color, rects, width=0):
    """
    вспомогательная функция, рисует несколько эллипсов
    """
    for rect in rects:
        pygame.draw.ellipse(surface, color, rect, width=width)


# dog functions
def draw_dog_head(surface: pygame.Surface, color: pygame.Color, middle: tuple[int, int], side: int):
    """
    рисует голову собаки. middle - координаты ценра головы, side - длина стороны квадрата
    """
    # квадрат
    pygame.draw.rect(surface, color, (middle[0] - side//2, middle[1] - side//2, side, side))
    pygame.draw.rect(surface, 'black', (middle[0] - side // 2, middle[1] - side // 2, side, side), width = 2)
    # левое ухо
    pygame.draw.circle(surface, color, (middle[0] - side//2, middle[1] - side//3), side//8)
    pygame.draw.circle(surface, 'black', (middle[0] - side//2, middle[1] - side//3), side//8, width=1)
    # правое ухо
    pygame.draw.circle(surface, color, (middle[0] + side//2, middle[1] - side//3), side//8)
    pygame.draw.circle(surface, 'black', (middle[0] + side//2, middle[1] - side//3), side//8, width=1)
    # левый глаз
    pygame.draw.ellipse(surface, 'white', (middle[0] - side//3, middle[1] - side//10, side//5, side//10))
    pygame.draw.ellipse(surface, 'black', (middle[0] - side//3, middle[1] - side//10, side//5, side//10), width=1)
    pygame.draw.circle(surface, 'black', (middle[0] - side//3 + side//10, middle[1] - side//20), side//20)
    # правый глаз
    pygame.draw.ellipse(surface, 'white', (middle[0] + 2*side//15, middle[1] - side//10, side//5, side//10))
    pygame.draw.ellipse(surface, 'black', (middle[0] + 2*side//15, middle[1] - side//10, side//5, side//10), width=1)
    pygame.draw.circle(surface, 'black', (middle[0] + 7*side//30, middle[1] - side//20), side//20)
    # рот
    pygame.draw.arc(surface, 'black', (middle[0] - side//3, middle[1] + side//4, 2*side//3, side//2), 0.3, 2.9)
    # левый зуб
    pygame.draw.polygon(surface, 'white', ((middle[0] - 7*side//30, middle[1] + side//5),
                                           (middle[0] - 6*side//30, middle[1] + 2.75*side//10),
                                           (middle[0] - 8*side//30, middle[1] + 3.25*side//10),
                                           (middle[0] - 7*side//30, middle[1] + side//5)))
    pygame.draw.aalines(surface, 'black', False, ((middle[0] - 7 * side // 30, middle[1] + side // 5),
                                                  (middle[0] - 6 * side // 30, middle[1] + 2.75 * side // 10),
                                                  (middle[0] - 8 * side // 30, middle[1] + 3.25 * side // 10),
                                                  (middle[0] - 7 * side // 30, middle[1] + side // 5)))
    # правый зуб
    pygame.draw.polygon(surface, 'white', ((middle[0] + 7 * side // 30, middle[1] + side // 5),
                                           (middle[0] + 6 * side // 30, middle[1] + 2.75 * side // 10),
                                           (middle[0] + 8 * side // 30, middle[1] + 3.25 * side // 10),
                                           (middle[0] + 7 * side // 30, middle[1] + side // 5)))
    pygame.draw.aalines(surface, 'black', False, ((middle[0] + 7 * side // 30, middle[1] + side // 5),
                                                  (middle[0] + 6 * side // 30, middle[1] + 2.9 * side // 10),
                                                  (middle[0] + 8 * side // 30, middle[1] + 3.25 * side // 10),
                                                  (middle[0] + 7 * side // 30, middle[1] + side // 5)))
def draw_dog_body(surface: pygame.Surface, color: pygame.Color, rect1: pygame.Rect, rect2 :pygame.Rect):
    draw_ellipses(surface, color, (rect1, rect2))
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
    :param facing_left: True - собака смотрит налево, False - направо. По умолчанию True
    """
    height = int(2/3 * width)
    pygame.draw.rect(screen, 'grey', (left_top[0], left_top[1], width, height))
    if facing_left is True:
        draw_dog_body(surface, color,
                      (left_top[0] + width//10, left_top[1] + width//9, 7*width//12, height//2),
                      (left_top[0] + 5*width//12, left_top[1] + width//10, 7*width//18, height//4))
        draw_dog_head(surface, color, (left_top[0] + width//5, left_top[1] + width//7), 2*width//7)
    else:
        draw_dog_body(surface, color,
                      (left_top[0] + (width - width//10 - 7*width//12), left_top[1] + width//9, 7*width//12, height//2),
                      (left_top[0] + (width - 5*width//12 - 7*width//18), left_top[1] + width//10, 7*width//18, height//4))
        draw_dog_head(surface, color, (left_top[0] + width - width // 5, left_top[1] + width // 7), 2 * width // 7)

FPS = 30
screen = pygame.display.set_mode((600, 600))

pygame.draw.rect(screen, 'lightblue', (0, 0, 600, 300))  # небо
pygame.draw.rect(screen, 'lightgreen', (0, 300, 600, 300))  # трава
draw_fence(screen, 'yellow', (50, 100, 400, 200), 10, 20, 5)
draw_dog(screen, (108, 103, 83), (100, 300), 400, facing_left=True)
#draw_dog(screen, (108, 103, 83), (100, 300), 400, facing_left=False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
