import turtle as tt
import math
tt.shape ('turtle')
tt.speed (1)

def move (x, y):
    tt.penup()
    tt.goto (x, y)
    tt.pendown()

def star (n):
    angle = (180 - (360 / n)) * 2
    l = 150
    #tt.left (180)
    for i in range (n):
        tt.forward (l)
        tt.left (angle)

move (-100, 0)
star (5)
move (100, 0)
star (11)
