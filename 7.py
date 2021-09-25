import turtle as tt
tt.shape ('classic')

angle = 5
side = 0.01
while True:
    tt.forward (side)
    tt.left (angle)
    side += 0.01
