# Q1:Temperature difference 
high = input("Please enter the highest temperature value predicted for the 10 day forcast: ")
low = input("Please enter the lowest temperature value predicted for the 10 day forcast: ")
diff = float(high) - float(low)
print(f"The temperature difference in degree celcius value is {diff}")
# Q2:Calculate the average 
num1 = float(input('Enter 1st temperature value at noon: '))
num2 = float(input('Enter 2nd temperature value at noon: '))
num3 = float(input('Enter 3rd temperature value at noon: '))
num4 = float(input('Enter 4th temperature value at noon: '))
num5 = float(input('Enter 5th temperature value at noon: '))
num6 = float(input('Enter 6th temperature value at noon: '))
num7 = float(input('Enter 7th temperature value at noon: '))
num8 = float(input('Enter 8th temperature value at noon: '))
num9 = float(input('Enter 9th temperature value at noon: '))
num10 = float(input('Enter 10th temperature value at noon: '))

avg =  (num1 + num2 + num3 + num4 + num5 
        + num6 + num7 + num8 + num9 + num10) / 10

print(f"The average temperature value predicted at noon predicted for the 10 day forecast is {avg}")

# Q3: Fahrenheit converted to Celsius
tempt = float(input("Enter the highest temperature value for the 10 day forecast in Fahrenheit: "))
celsius = (tempt - 32 )*5/9 
print(f"The highest temerature in celcius is {celsius}")

# 总结：
# 1. input语句总是字符串窜：input("") 输入的value总是string，如果要变成value，需要使用 float()或者int() function
# 2. print语句用f-：print后面不要再打等号！如果要打印字符串，需要加f，即 print(f"") 
# 3. string转成float：如果输出的字符串语句里面要加value的话，使用{}进行连接，如：print(f"Python is {value}%")

