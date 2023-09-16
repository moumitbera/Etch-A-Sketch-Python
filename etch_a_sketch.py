# an program that uses -
# w: forwards
# s = backwards
# a = counter-clock 
# d = clockwise

import turtle as t

turtle = t.Turtle()
screen = t.Screen()

screen.listen()
change = 10

def move_forwards():
    turtle.fd(change)

def move_backwards():
    turtle.back(change)

def counter_clock():
    turtle.left(change)

def clock_wise():
    turtle.right(change)

def clear():
    turtle.clear()
    turtle.penup
    turtle.home()
    turtle.pendown()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()