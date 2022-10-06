from turtle import right, left, forward, penup, pendown
from turtle import shape, exitonclick

shape('turtle')

# pootocene ctverce
for _ in range(18):
    left(20)
    for _ in range(4):
        forward(100)
        right(90)

# zvetsujici se prerusovana cara 
line_length = 10
right(90)
for i in range(1, 10):
    pendown()
    forward(line_length * i)
    penup()
    forward(line_length)

exitonclick()
