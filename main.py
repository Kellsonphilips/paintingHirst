import turtle
# import colorgram
from turtle import Turtle, Screen
import random

# extracting colors from a picture

# rgb_colors = []
# colors = colorgram.extract("SpotPainting04.jpeg", 12)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

turtle.colormode(255)

color_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105)]

paintMaster = Turtle()
paintMaster.hideturtle()
paintMaster.speed(0)


def move():
    paintMaster.setheading(225)
    paintMaster.penup()
    paintMaster.forward(350)
    paintMaster.setheading(0)


move()
num_of_moves = 100
# draw_complete = False


for dots in range(1, num_of_moves + 1):
    paintMaster.dot(25)
    paintMaster.penup()
    paintMaster.forward(50)
    paintMaster.color(random.choice(color_list))

    if dots % 10 == 0:
        paintMaster.setheading(90)
        paintMaster.penup()
        paintMaster.forward(50)
        paintMaster.setheading(180)
        paintMaster.penup()
        paintMaster.forward(500)
        paintMaster.setheading(0)


screen = Screen()
screen.exitonclick()
