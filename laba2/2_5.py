import turtle as tt
from random import *
tt.setup (650, 650)
dots_count = 20
dots = [tt.Turtle (shape = 'circle') for i in range (dots_count)]

tt.penup()
tt.goto (-300, -300)
tt.pendown()
tt.goto (300, -300)
tt.goto (300, 300)
tt.goto (-300, 300)
tt.goto (-300, -300)
tt.hideturtle()

for dot in dots:
    dot.turtlesize (0.1, 0.1)
    dot.speed = 1
    dot.penup()
    dot.goto (randint (-200, 200), randint (-200, 200))
    dot.seth (randint(0, 355))

while (True):
    for dot in dots:
        dot.forward (10)
        x, y = dot.pos()
        hdg = dot.heading()
        if (abs (x) >= 300):
            dot.left (2 * (90 - hdg))
        elif (abs (y) >= 300):
            dot.right (2 * hdg)
