import turtle
import random

def draw_shape(forward, angle, length):
    ninja.penup()
    ninja.forward(forward)
    for x in range(200):
        ninja.right(angle)
        ninja.pendown()
        ninja.forward(length)


ninja = turtle.Turtle()

ninja.speed(0)
ninja.shape('turtle')
ninja.shapesize(1, 1)

for i in range(10):
    draw_shape(random.randint(50, 200), random.randint(0, 180), random.randint(50, 200))

turtle.done()
