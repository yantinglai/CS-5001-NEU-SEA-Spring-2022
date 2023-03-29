"""A function to draw the circle"""
r = int(input("Enter the radius for this circle: "))
def draw_circle():
    """A function to draw the circle"""
    diameter = 2*r
    for i in range(diameter+1):
        for j in range(diameter+1):
            point1 = i - r
            point2 = j - r

            if point1*point1 + point2*point2 <= r*r +1:
                print("o", end ="")
            else:
                print(" ", end = "")

        print()

draw_circle()
