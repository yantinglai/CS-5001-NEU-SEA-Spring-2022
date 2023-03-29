""" CS5001: Enter an odd or even number, output a diamond shape by YANTING LAI """

height = int(input("Please enter an odd or even number: "))
h = height

# When the iput is an odd number:
if h % 2 != 0:
    for i in range(1,h+1):
        i = i - (h//2 +1)
        if i <0:
            i = -i
        print(" "*i + "*"*(h-i*2)+ " "*i)

# When the input is an even number:
if h % 2 == 0:
    for i in range(1,h+1):
        if i <= (h//2):
            i = i - (h//2)
            i = -i
            print(" "*i + "*"*(h -2*i -1)+" "*i)
        if i > (h//2):
            i -=1
            i = i-(h//2)
            print(" "*i + "*"*(h -2*i -1)+" "*i)