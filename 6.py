import turtle as tt
tt.shape('turtle')

n = int (input())
side = 100
for i in range (n):
    tt.forward (side)
    tt.stamp()
    tt.goto(0, 0)
    tt.right (360 / n)
