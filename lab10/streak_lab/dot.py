class Dot():
    def __init__(self, x, y, bright=0):
        self.x = x
        self.y = y
        self.size = 10
        self.bright = bright

    def display(self):
        dot_fill = (0, 1, 0, self.bright)
        fill(*dot_fill)
        noStroke()
        ellipse(self.x,
                self.y,
                self.size,
                self.size)
