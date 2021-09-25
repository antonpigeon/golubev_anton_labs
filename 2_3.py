import turtle as tt
tt.color ('blue')
tt.width (2)

f1 = open ('numbers.txt', 'r')
read = f1.readlines()
print (read)
numbers = []
for str in read:
    str = str.rstrip()
    str = str.split (' ')
    lst = []
    for i in range (0, len(str), 3):
        t = int (str [i]), int (str [i + 1]), int (str [i + 2])
        lst.append (t)
    numbers.append (lst)

for i in range (len (numbers)):
    tt.penup()
    tt.goto(i*50, 0)
    tt.pendown()
    tt.seth (0)
    for tup in numbers[i]:
        if (tup [2] == 0):
            tt.penup()
        tt.left (tup [0])
        tt.forward (tup [1])
        if (tup [2] == 0):
            tt.pendown()
f1.close()
