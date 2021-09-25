import turtle as tt
import math
tt.shape ('turtle')
tt.speed (11)

def arc (r, arclength, right = True):
    angle = 2
    for i in range (int (arclength / angle)):
        tt.forward (r * math.sin (angle * math.pi / 180))
        if right == True:
            tt.right (angle)
        else:
            tt.left (angle)

r1, r2 = 50, 10
n = 5
tt.penup()
tt.goto (-200, 0)
tt.pendown()
tt.seth (90)
for i in range (n - 1):
    arc (r1, 180)
    arc (r2, 180)
arc (r1, 180)

