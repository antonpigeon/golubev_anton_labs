import turtle as tt
import math
tt.shape ('turtle')
tt.speed (30)

def circle (r, right = True):
    angle = 2
    for i in range (int (360 / angle)):
        tt.forward (r * math.sin (angle * math.pi / 180))
        if right == True:
            tt.right (angle)
        else:
            tt.left (angle)

n = 4
r = 25
for i in range (n):
    circle (r, True)
    circle (r, False)
    tt.right (180 / n)
