import math
def main():
        
    x1,y1 = eval(input("Please enter coordinates of Point1(using commas)"))
    x2,y2 = eval(input("Please enter coordinates of Point2(using commas)"))

    print(f"The distance between {x1,y1} and {x2,y2} is { math.sqrt((x2-x1)**2 +(y2-y1)**2)}")

main()

# 另外一种写法
