from random import randint
import pygame
import pygame.freetype
import json

pygame.init()

# Размер окна
x_pixels = 500
y_pixels = 500
# Размер места под счёт
total_box_x = 100
total_box_y = 50

FPS = 30
screen = pygame.display.set_mode((x_pixels, y_pixels))
popping_speed = 3
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
        self.points_cost = 1
        self.is_popping = False
        self.stopped_popping = False
        self.x = randint(total_box_x, x_pixels - x_pixels // 10)
        self.y = randint(total_box_y, y_pixels - y_pixels // 10)
        self.r = randint(20, 30)
        self.popping_r = self.r
        self.max_pop_r = self.r * 2.5
        self.x_speed = randint(-3, 3)
        self.y_speed = randint(-3, 3)
        self.color = COLORS[randint(0, len(COLORS) - 1)]
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)

    def contains_point(self, x: int, y: int):
        return (self.x - x) ** 2 + (self.y - y) ** 2 <= self.r ** 2

    def blackout(self):
        pygame.draw.circle(self.surface, (0, 0, 0), (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def bounce(self):
        if self.x + self.r >= x_pixels or self.x - self.r <= 0:
            self.x_speed *= -1
        if self.y + self.r >= y_pixels or self.y - self.r <= 0:
            self.y_speed *= -1

    def advance_popping(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.popping_r)
        self.popping_r += popping_speed
        if self.popping_r >= self.max_pop_r:
            self.stopped_popping = True

    def update(self):
        if self.is_popping is False:
            self.bounce()
            self.move()
        else:
            self.advance_popping()


class Square:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.points_cost = 3
        self.is_popping = False
        self.stopped_popping = False
        self.x = randint(total_box_x, x_pixels - x_pixels // 10)
        self.y = randint(total_box_y, y_pixels - y_pixels // 10)
        self.side = randint(20, 30)
        self.popping_side = self.side
        self.max_pop_side = self.side * 2.5
        self.ticks_since_tp = 0
        self.color = COLORS[randint(0, len(COLORS) - 1)]
        pygame.draw.rect(surface, self.color, (self.x - self.side//2, self.y - self.side//2,
                                               self.side, self.side))

    def contains_point(self, x: int, y: int):
        return (self.x - self.side//2 <= x <= self.x + self.side//2 and
                self.y - self.side//2 <= y <= self.y + self.side//2)

    def blackout(self):
        pygame.draw.rect(surface, BLACK, (self.x - self.side // 2, self.y - self.side // 2,
                                          self.side, self.side))

    def move(self):
        if self.ticks_since_tp == 30:
            self.ticks_since_tp = 0
            self.x = randint(total_box_x, x_pixels - x_pixels // 10)
            self.y = randint(total_box_y, y_pixels - y_pixels // 10)
        else:
            self.ticks_since_tp += 1
        pygame.draw.rect(self.surface, self.color, (self.x - self.side // 2, self.y - self.side // 2,
                                                    self.side, self.side))

    def advance_popping(self):
        pygame.draw.rect(self.surface, self.color, (self.x - self.popping_side // 2, self.y - self.popping_side // 2,
                                                    self.popping_side, self.popping_side))
        self.popping_side += popping_speed
        if self.popping_side >= self.max_pop_side:
            self.stopped_popping = True

    def update(self):
        if self.is_popping is False:
            self.move()
        else:
            self.advance_popping()


pygame.display.update()
clock = pygame.time.Clock()


dt = {}


to_exit = False
while not to_exit:
    targets = []
    total = 0
    ticks_since_append = 0
    player_name = ""
    finished = False
    while not finished:
        pygame.display.update()
        clock.tick(FPS)
        my_font.render_to(screen, (x_pixels//3, y_pixels//3), "введите имя:", (255, 0, 0))
        my_font.render_to(screen, (x_pixels//3, y_pixels//3), "введите имя:", (255, 0, 0))
        pygame.draw.rect(screen, BLACK, (x_pixels//3, y_pixels//3 + 20, x_pixels, y_pixels))
        my_font.render_to(screen, (x_pixels//3, y_pixels//3 + 20), player_name, (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finished = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += pygame.key.name(event.key)

    finished = False

    while not finished:
        clock.tick(FPS)
        if ticks_since_append == 30:
            targets.append(Ball(screen) if randint(0, 1) == 1 else Square(screen))
            ticks_since_append = 0
        ticks_since_append += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for target in targets[::-1]:
                    if (target.contains_point(*event.pos) is True
                            and target.is_popping is False):
                        target.is_popping = True
                        total += target.points_cost
                        break  # Чтобы убирать только 1 цель за раз
        screen.fill((0, 0, 0))
        for target in targets:
            target.update()
            if target.stopped_popping is True:
                targets.remove(target)

        # Обновление текста
        pygame.draw.rect(screen, BLACK, (0, 0, total_box_x, total_box_y))
        my_font.render_to(screen, (5, 10), "total: " + str(total), (255, 0, 0))

        pygame.display.update()

    dt[player_name] = total
    with open('scores.json', 'w') as f:
        json.dump(dt, f)


pygame.quit()
