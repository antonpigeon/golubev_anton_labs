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

def move (x, y):
    tt.penup()
    tt.goto (x, y)
    tt.pendown()
    
tt.left (90)

tt.fillcolor ('yellow')
tt.begin_fill()
arc (50, 360, False)
tt.end_fill()

move (-40, 25)
tt.fillcolor ('blue')
tt.begin_fill()
arc (10, 360)
tt.end_fill()

move (-80, 25)
tt.begin_fill()
arc (10, 360)
tt.end_fill()

move (-50, 0)
tt.color ('black')
tt.width (10)
tt.goto (-50, -20)

move (-20, -10)
tt.left (180)
tt.color ('red')
arc (30, 180)
tt.hideturtle()
