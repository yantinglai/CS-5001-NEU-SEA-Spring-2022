# ControlP5 is a 3rd party library that gives us
# interface controls. We need it for the slider.
from point import Point
add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider

# Here we import the Point class definition from
# the other tab of this sketch. That file is
# and ordinary .py file stored in the same
# sketch directory.

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


def setup():
    size(430, 400)
    noStroke()
    setupSlider()


def draw():
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    """A recursive function that draws the Sierpinski triangle"""
    if recursionDepth <= 0:
        return
    # paint the first dark triangle in the middle
    mid_l_r = bottomLeft.midPoint(bottomRight)
    mid_l_t = bottomLeft.midPoint(top)
    mid_r_t = bottomRight.midPoint(top)
    fill(0)

    triangle(mid_l_r.getX(), mid_l_r.getY(),
             mid_l_t.getX(), mid_l_t.getY(),
             mid_r_t.getX(), mid_r_t.getY())
    
    # paint the bottom left dark triangle
    sierpinksi(bottomLeft, mid_l_r, mid_l_t, recursionDepth - 1)
    # paint the bottom right dark triangle
    sierpinksi(bottomRight, mid_l_r, mid_r_t, recursionDepth - 1)
    # paint the top dark triangle
    sierpinksi(top, mid_l_t, mid_r_t, recursionDepth - 1)


# The code below sets up the slider and sets a listener callback
# function to respond to the user sliding the slider.
def setupSlider():
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    global depth
    depth = event.value()
