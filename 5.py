import turtle as tt
tt.shape('turtle')

def square (side):
    for i in range (4):
        tt.forward(side)
        tt.left(90)
        
side = 20
num_squares = 10
x = num_squares * side
while (side <= x):
    square (side)
    tt.penup()
    tt.goto (-side/2, -side/2)
    tt.pendown()
    side += 20
