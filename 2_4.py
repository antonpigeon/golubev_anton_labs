import turtle as tt
tt.shape ('circle')
tt.turtlesize (0.1, 0.1)
eps = 0.01 #точность касания
g = 9.81 #m/c^2
v0x = 15 #m/c
v0y = 30 #m/c
dt = 0.1 #сек
x, y = -300, 0
vy = v0y

tt.goto (300, 0)
tt.goto (-300, 0)
while (x < 300):
    x += v0x * dt
    vy -= g * dt
    y += vy * dt
    tt.goto (x, y)
    if (y <= eps):
        vy = - 9 * vy/ 10
        if (abs (vy) < 1):
            break
