from dot import Dot


class Streak():
    """A class of streak"""
    def __init__(self, x, y, lenrate=5):
        self.x = x
        self.y = y
        self.streak_length = 50
        self.limit = 10
        self.streak = [
            Dot(self.x, self.y) for _ in range(self.streak_length)
        ]
        self.lengthen_rate = lenrate

    def lengthen(self):
        for i in range(self.lengthen_rate):
            self.streak.insert(len(self.streak)-1,
                               Dot(self.streak[0].x, self.streak[0].y))
            self.streak_length = len(self.streak)

    def shorten(self):
        if self.streak_length < self.limit:
            return
        else:
            for i in range(self.lengthen_rate):
                self.streak.pop()
        self.streak_length = len(self.streak)

    def update(self, x, y):
        self.streak[0].x = x
        self.streak[0].y = y
        self.streak[0].bright = 1.0

        for i in range(self.streak_length - 1, 0, -1):
            self.streak[i].x = self.streak[i-1].x  # replace Xn to Xn-1..
            self.streak[i].y = self.streak[i-1].y  # replace Yn to Yn-1..
            self.streak[i].bright = 1.0 - (i*1.0 / (self.streak_length - 1))

        self.display()

    def display(self):
        for dot in self.streak:
            dot.display()

# shouldn't type chinese in the doc, otherwise the doc cannot be open
