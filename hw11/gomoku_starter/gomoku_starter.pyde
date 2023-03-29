"""CS5001 Gomoku Game by YANTING LAI"""
ROWS = 3
COLS = 3
grid = [[0 for i in range(ROWS)] for j in range(COLS)]
WIDTH = 300  # small board use 300 * 300
HEIGHT = 300
SPACING = WIDTH / ROWS
white_flag = True


def setup():
    """Set up the canvas"""
    size(WIDTH, HEIGHT)
    global flag
    flag = 1


def drawBoard():
    """Draw a Gomoku board"""
    background(155, 122, 31)  # 0: dark  250: white
    stroke(0)  # stroke color of the board line
    strokeWeight(5)  # stroke thickness of the line
    x = (WIDTH / ROWS) // 2
    y = (HEIGHT / COLS) // 2
    while x < HEIGHT:
        line(x, y, x, HEIGHT - y)  # the relations bt x and Width & Height
        x = x + SPACING

    x = (WIDTH / ROWS) // 2
    y = (HEIGHT / COLS) // 2
    while y < WIDTH:
        line(x, y, WIDTH - x, y)
        y = y + SPACING


def clickStone():
    """Put the black or white stone when mouse click"""
    global row, col, white_flag
    flag = 1
    row = mouseY // SPACING
    col = mouseX // SPACING
    print(row, col)
    if grid[row][col] == 0:
        white_flag = not white_flag
        flag = 1
    elif grid[row][col] != 0: # avoid clicking same dot and change color
        flag = 0
        white_flag = white_flag

    if flag == 1:
        if white_flag:
            grid[row][col] = 1
        else:
            grid[row][col] = 2


def mousePressed():
    """When mouse click, a stone will be drawn and the action repeats"""
    white_flag = True
    clickStone()
    redraw()


def drawStone():
    """Define the position to draw the stone"""
    SPACING = WIDTH / ROWS
    D = SPACING - 10
    H = 0.5
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1 and flag == 1:
                fill(255)
                ellipse((j+H)*SPACING, (i+H)*SPACING, D, D)
            elif grid[i][j] == 2 and flag == 1:
                fill(0)
                ellipse((j+H)*SPACING, (i+H)*SPACING, D, D)


def endGame(): 
    """Judge the result of the game"""
    count = 0
    white = 0
    black = 0
    SPACING = 120
    TEXT_SIZE = 40

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                white += 1
                count += 1
            elif grid[i][j] == 2:
                black += 1
                count += 1

    if count == ROWS * COLS:
        if white > black:
            fill(131, 250, 146)
            textSize(TEXT_SIZE)
            text("WHITE WINS!", WIDTH / 2 - SPACING, HEIGHT / 2)
        elif white < black:
            fill(131, 250, 146)
            textSize(TEXT_SIZE)
            text("BLACK WINS!", WIDTH / 2 - SPACING, HEIGHT / 2)
        if white == black:
            fill(131, 250, 146)
            textSize(TEXT_SIZE)
            text("IT'S A TIE!", WIDTH / 2 - SPACING, HEIGHT / 2)


def draw():
    drawBoard()
    drawStone()
    endGame()
