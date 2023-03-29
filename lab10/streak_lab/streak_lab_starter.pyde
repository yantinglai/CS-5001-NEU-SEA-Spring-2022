from streak import Streak

WIDTH = 600
HEIGHT = 600
BG_COLOR = (0.0, 0.0, 0.0)
CIRCLE_DEGS = 360
MAGENTA_BRIGHT = (1, 0, 1)
MAGENTA_DARK = (0.2, 0.0, 0.2)
BLACK = 0
RECT_POS_X = WIDTH//4
RECT_POS_Y = HEIGHT//4
CIRC_POS_X = WIDTH//2
CIRC_POS_Y = HEIGHT//2
SQUARE_SIZE = 300
CIRCLE_SIZE = 185

field = (WIDTH, HEIGHT)
radius = 180
center = (WIDTH//2, HEIGHT//2)
angle = 0
streak = Streak(
                radius * sin(radians(angle)) + center[0],
                radius * cos(radians(angle)) + center[1]
                )


def setup():
    """
    Set up the environment
    """
    size(*field)
    colorMode(RGB, 1)


def draw():
    global angle
    background(*BG_COLOR)
    fill(BLACK)
    strokeWeight(3)
    stroke(*MAGENTA_BRIGHT)
    fill(*MAGENTA_DARK)
    rect(RECT_POS_X, RECT_POS_Y, SQUARE_SIZE, SQUARE_SIZE)
    fill(BLACK)
    ellipse(CIRC_POS_X, CIRC_POS_Y, CIRCLE_SIZE, CIRCLE_SIZE)

    dot_position = (
                    radius * sin(radians(angle)) + center[0],
                    radius * cos(radians(angle)) + center[1]
                    )
    streak.update(*dot_position)

    angle += 1
    if angle > CIRCLE_DEGS - 1:
        angle = angle - CIRCLE_DEGS


def keyPressed():
    global radius
    if key == CODED:
        if keyCode == UP:
            streak.lengthen()
        if keyCode == DOWN:
            streak.shorten()
