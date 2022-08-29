import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
pnt = Turtle()
pnt.speed("fastest")
pnt.penup()
pnt.hideturtle()

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
         (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
         (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79),
         (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177),
         (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

pnt.setheading(225)
pnt.forward(250)
pnt.setheading(0)

no_of_spots = 100

for i in range(1, no_of_spots + 1):
    pnt.dot(20, random.choice(colors))
    pnt.forward(50)

    if i % 10 == 0:
        pnt.left(90)
        pnt.forward(50)
        pnt.left(90)
        pnt.forward(500)
        pnt.left(180)


screen = Screen()
screen.exitonclick()