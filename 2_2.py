side = 30
import turtle as tt
tt.color ('blue')
tt.width (2)
a = 2**0.5
list1 = [(-90, side, 0), (135, a*side, 1), (-135, 2*side, 1)]
list0 = [(0, side, 1), (-90, 2*side, 1), (-90, side, 1), (-90, 2*side, 1)]
list4 = [(-90, side, 1), (90, side, 1), (90, side, 1),(180, 2*side, 1)]
list7 = [(0, side, 1), (-135, a*side, 1), (45, side, 1)]
i = 0
for lst in [list1, list4, list1, list7, list0, list0]:
    for tup in lst:
        if (tup [2] == 0):
            tt.penup()
        tt.left (tup [0])
        tt.forward (tup [1])
        if (tup [2] == 0):
            tt.pendown()
    i += 1
    tt.penup()
    tt.goto(i*50, 0)
    tt.pendown()
    tt.seth (0)
