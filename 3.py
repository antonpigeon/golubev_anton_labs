import turtle as tt
tt.shape('turtle')
def square (side):
    for i in range (4):
        tt.forward(side)
        tt.left(90)

square(100)
tt.goto(0,0)
