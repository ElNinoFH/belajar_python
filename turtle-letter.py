from turtle import *

getscreen()

shape("triangle")

bgcolor("white")

speed("slowest")

pensize(5)

fillcolor("cyan")

begin_fill()
for i in range(1):

    pendown()
    showturtle()

    forward(220)

    left(90)
    forward(300)

    left(90)
    forward(280)

    left(90)
    forward(300)

    left(90)
    forward(60)

end_fill()

hideturtle()
penup()
left(90)
forward(50)
pendown()
showturtle()

forward(200)

right(140)
forward(250)

left(140)
forward(200)

hideturtle()
penup()

done()