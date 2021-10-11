import pygame
import pygame.freetype
from random import randint
pygame.init()

# Размер окна
x_pixels = 500
y_pixels = 500
# Размер места под счёт
total_box_x = 100
total_box_y = 50

FPS = 30
screen = pygame.display.set_mode((x_pixels, y_pixels))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

my_font = pygame.freetype.SysFont('Times New Roman', 15)


class Ball:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.x = randint(total_box_x, x_pixels - x_pixels//10)
        self.y = randint(total_box_y, y_pixels - y_pixels//10)
        self.r = randint(20, 30)
        self.x_speed = randint(-3, 3)
        self.y_speed = randint(-3, 3)
        self.color = COLORS[randint(0, len(COLORS) - 1)]
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)

    def contains_point(self, x: int, y: int):
        return(self.x - x)**2 + (self.y - y)**2 <= self.r**2

    def blackout(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def bounce(self):
        if self.x + self.r >= x_pixels or self.x - self.r <= 0:
            self.x_speed *= -1
            self.x += 2*self.x_speed  # Чтобы не застревал
        if self.y + self.r >= y_pixels or self.y - self.r <= 0:
            self.y_speed *= -1
            self.y += 2*self.y_speed


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = []
total = 0
ticks_since_append = 0

while not finished:
    clock.tick(FPS)
    if ticks_since_append == 30:
        balls.append(Ball(screen))
        ticks_since_append = 0
    ticks_since_append += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls[::-1]:
                if ball.contains_point(event.pos[0], event.pos[1]) is True:
                    ball.blackout()
                    balls.remove(ball)
                    total += 1
                    break  # Чтобы убирать только 1 шар за раз
    screen.fill((0, 0, 0))
    for ball in balls:
        ball.bounce()
        ball.move()

    # Обновление текста
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, total_box_x, total_box_y))
    my_font.render_to(screen, (5, 10), "total: " + str(total), (255, 0, 0))

    pygame.display.update()
    # screen.fill(BLACK)

pygame.quit()
