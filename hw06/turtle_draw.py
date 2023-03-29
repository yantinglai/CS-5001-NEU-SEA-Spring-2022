""" CS5001: Draw a star inscribed a circle by YANTING LAI """
import turtle
import time

START_POINT = 0
HEIGHT = 262
DISTANCE = 500
TURN_ANGLE = 72
RIGHT_TURN_ANGLE = 144
SPEED_TIME = 0
SLEEP_TIME = 3
ANKOR_NUMBER = 5

# Initialize the pen configuration: shape, speed, movement
t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.speed(SPEED_TIME)
t.penup()

# Draw a circle
def draw_circle(height):
    """
    Draw the circle
    """
    t.goto(0, -HEIGHT)
    t.color("blue")
    t.pendown()

    t.fillcolor("cyan")
    t.begin_fill()
    t.circle(HEIGHT)
    t.end_fill()
    t.penup()

# Draw a star
def draw_star(height, angle1, angle2 ):
    """
    Draw the star
    """
    t.goto(0, HEIGHT)
    t.color("red")
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(TURN_ANGLE)
    for _ in range(ANKOR_NUMBER):
        t.forward(DISTANCE)
        t.right(RIGHT_TURN_ANGLE)
    t.end_fill()
    t.penup()

draw_circle(HEIGHT)
draw_star(HEIGHT, DISTANCE, TURN_ANGLE)
time.sleep(SLEEP_TIME)

# How to improve the code? - 在最前面声明constant，传入到function call当中
# size 以及 位置的常数，可以使用 global variable，传入到function当中
# 犯的错误，把parameters直接传到了function里面了，应该传到 function call 里面！
