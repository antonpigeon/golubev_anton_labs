import turtle as tt
import math
tt.shape ('turtle')
tt.speed (11)

def circle (r, right = True):
    angle = 2
    for i in range (int (360 / angle)):
        tt.forward (r * math.sin (angle * math.pi / 180))
        if right == True:
            tt.right (angle)
        else:
            tt.left (angle)

n = 8
r = 40
tt.left (90)
for i in range (n):
    circle (r, True)
    circle (r, False)
    r += 15
