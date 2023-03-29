
class Stone:
    """A Stone class"""

    def __init__(self, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.d = 50  # diameter

    def display(self):
        """
        Draw a stone object with different color
        """
        STROKE = 0
        STROKE_WEIGHT = 5
        stroke(STROKE)
        strokeWeight(STROKE_WEIGHT)
        fill(self.color)
        ellipse(self.pos_x, self.pos_y, self.d, self.d)
