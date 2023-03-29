class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint=500):
        """Calculate the coordinate of the new midpoint and returns it"""

        new_mid_X = (otherPoint.getX() + self.getX()) / 2
        new_mid_Y = (otherPoint.getY() + self.getY()) / 2

        return Point(new_mid_X, new_mid_Y)

    # Another way to calculate the mid point
    #  newX = self.getX() + (otherPoint.getX() - self.getX()) / 2
    #  newY = self.getY() + (otherPoint.getY() - self.getY()) / 2
