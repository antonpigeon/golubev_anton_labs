import turtle as tt
import math
tt.shape ('turtle')
tt.speed (5)

def n_shape (n, side):
    tt.seth (180 - (90 * (n - 2) / n))
    for _ in range (n):
        tt.forward (side)
        tt.left (360 / n)
    tt.seth (0)

#n_shape (3, 80)
r = 30
for n in range (3, 13):
    tt.penup()
    tt.goto (r, 0)
    tt.pendown()
    side = 2 * r * math.sin(math.pi / n)
    n_shape (n, side)
    r += 20
