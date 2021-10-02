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
    """
    pygame.draw.rect(surface, color, rect)
    x = rect[0] + starting_x
    while x <= rect[0] + rect[2]:
        dx = random.randint(-max_offset, max_offset)
        pygame.draw.line(surface, 'black', (x + dx, rect[1]), (x + dx, rect[1] + rect[3]))
        x += step


def draw_ellipses(surface: pygame.Surface, color: pygame.Color, rects, width=0):
    """
    вспомогательная функция, рисует несколько эллипсов по массиву rects
    :param: rects: tuple или list, содержащий прямоугольники pygame.Rect, в которые надо вписать эллипсы
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


def draw_dog_body(surface: pygame.Surface, color: pygame.Color, rect1: pygame.Rect, rect2: pygame.Rect):
    draw_ellipses(surface, color, (rect1, rect2))


def draw_dog_forward_leg(surface: pygame.Surface, color: pygame.Color,
                         top: tuple[int, int], height: int, facing_left=True):
    """
    :param top: координаты верхней центральной точки верхнего эллипса
    :param height: высота всей ноги
    """
#    draw_ellipses(surface, color, (rect1, rect2))
    width = height//2
    width1 = 3*width//4  # ширина верхнего эллипса
    pygame.draw.ellipse(surface, color, (top[0] - width1//2, top[1], width1, 7*height//8))
    if facing_left is True:
        pygame.draw.ellipse(surface, color, (top[0] - 5*width//8, top[1] + 5*height//6, 7*width//8, height//6))
    else:
        pygame.draw.ellipse(surface, color, (top[0] - width//4, top[1] + 5*height//6, 7*width//8, height//6))


def draw_dog_back_leg(surface: pygame.Surface, color: pygame.Color,
                         top: tuple[int, int], height: int, facing_left=True):
    """
    :param top: координаты верхней центральной точки верхнего круга
    :param height: высота всей ноги
    """
    width = height//2
    width2 = width//5
    width3 = 2*width//3
    pygame.draw.circle(surface, color, (top[0], top[1] + height//5), height//5)
    if facing_left is True:
        pygame.draw.ellipse(surface, color, (top[0] + width//4, top[1] + height//5, width2, 5*height//8))
        pygame.draw.ellipse(surface, color, (top[0] - width//5, top[1] + 3*height//4, width3, height//6))
    else:
        pygame.draw.ellipse(surface, color, (top[0] - width // 4 - width2, top[1] + height // 5, width2, 5 * height // 8))
        pygame.draw.ellipse(surface, color, (top[0] - 7*width//15, top[1] + 3*height//4, width3, height//6))


def draw_dog(surface: pygame.Surface, color: pygame.Color, left_top: tuple[int, int],
             width: int, facing_left=True,):
    """
    рисует собаку как в примере
    :param left_top: координаты левого верхнего угла изображения (x, y)
    :param width: ширина изображения (высота вычисляется соответственно)
    :param facing_left: True - собака смотрит налево, False - направо. По умолчанию True
    """
    height = int(2/3 * width)
    if facing_left is True:
        draw_dog_forward_leg(surface, color, (left_top[0] + width//3, left_top[1] + height//2),
                             5*height//12, facing_left=True)
        draw_dog_forward_leg(surface, color, (left_top[0] + 3*width//18, left_top[1] + 5*height//14),
                             5*height//12, facing_left=True)
        draw_dog_back_leg(surface, color,
                          (left_top[0] + 4*width//5, left_top[1] + height//4), height//2, facing_left=True)
        draw_dog_back_leg(surface, color,
                          (left_top[0] + 2*width//3, left_top[1] + height//9), height//2, facing_left=True)
        draw_dog_body(surface, color,
                      (left_top[0] + width//10, left_top[1] + width//9, 7*width//12, 2*height//5),
                      (left_top[0] + 5*width//12, left_top[1] + width//10, 7*width//18, height//4))
        draw_dog_head(surface, color, (left_top[0] + width//5, left_top[1] + width//7), 2*width//7)
    else:
        draw_dog_forward_leg(surface, color, (left_top[0] + 2*width//3, left_top[1] + height//2),
                             5*height//12, facing_left=False)
        draw_dog_forward_leg(surface, color, (left_top[0] + 15*width//18, left_top[1] + 5*height//14),
                             5*height//12, facing_left=False)
        draw_dog_back_leg(surface, color,
                          (left_top[0] + 1*width//5, left_top[1] + height//4), height//2, facing_left=False)
        draw_dog_back_leg(surface, color,
                          (left_top[0] + 1*width//3, left_top[1] + height//9), height//2, facing_left=False)
        draw_dog_body(surface, color,
                      (left_top[0] + (width - width//10 - 7*width//12), left_top[1] + width//9, 7*width//12, 2*height//5),
                      (left_top[0] + (width - 5*width//12 - 7*width//18), left_top[1] + width//10, 7*width//18, height//4))
        draw_dog_head(surface, color, (left_top[0] + width - width // 5, left_top[1] + width // 7), 2 * width // 7)


# main начинается здесь
FPS = 30
screen = pygame.display.set_mode((600, 600))

pygame.draw.rect(screen, 'lightblue', (0, 0, 600, 300))  # небо
pygame.draw.rect(screen, 'lightgreen', (0, 350, 600, 250))  # трава
draw_fence(screen, 'yellow', (0, 100, 600, 250), 10, 30, 3)
draw_dog(screen, (108, 103, 83), (50, 360), 250, facing_left=True)
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
