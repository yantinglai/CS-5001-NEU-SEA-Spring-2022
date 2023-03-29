import random

print("Welcome to the Guessing Game!")
user_guess = int(input("I picked a number between 1 and 50. Try and guess! \n"))
random_number = random.randint(1,50)
tries = 0

print("You guessed", user_guess)

while (user_guess != random_number):
    diff = abs(user_guess - random_number)
    tries +=1
    if (diff == 1):
        user_guess = int(input("Your guess is scalding hot \n"))
        
    elif(diff == 2):
        user_guess = int(input("Your guess is extremely warm \n"))
        
    elif(diff == 3):
        user_guess =int(input("Your guess is very warm \n"))
        
    elif(diff >= 4 and diff <= 5):
        user_guess = int(input("Your guess is warm \n"))

    elif(diff >=6 and diff <= 8):
        user_guess = int(input("Your guess is cold \n"))
      
    elif(diff >=9 and diff <=13):
        user_guess = int(input("Your guess is very cold \n"))

    elif(diff >=14 and diff <= 20):
        user_guess = int(input("Your guess is extremely cold \n"))
        
    elif(diff > 20):
        user_guess = int(input("Your guess is icy freezing miserably cold \n"))
        

print(f"Congratulations. You figured it out in {tries} tries.")
        
        

# while loop的作用：就是当你的语句没有达到 while 一开始的结果的时候，它就会不停的去找
# 换行的语句：\n
# generate a random number between 1 and 50：random.randint(1,50)
