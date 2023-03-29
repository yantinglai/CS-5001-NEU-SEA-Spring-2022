import random

print("Welcome to the DMV (estimated wait time is 3 hours)")
full_name = input("Please enter your first, middle, and last name: ")
date_of_birth = input("Enter date of birth (MM/DD/YY): ")

name_break = full_name.rfind(' ')
first_and_middle = full_name[:name_break]
last = full_name[name_break+1:]

date_break = date_of_birth.rfind('/')
month_and_day = date_of_birth[:date_break]
year = date_of_birth[date_break:]  # 这行代码没有用到

def cmv(): 
      str1 = ""
      for i in range(7):
        temp = str(random.randint(0,9))
        str1 +=temp 
      return str1 

# expire_year = date_of_birth.split()

print("Washington Driver License")
print("DL ", cmv())
print("LN", last)  # split 名字的知识点: 使用 rfind，去看tony的代码 -- 问题解决
print("FN", first_and_middle) 
print("DOB", date_of_birth)
print(f"EXP {month_and_day}/21")  # print()    # 替换 string 的知识点  -- 怎么把 /66替换成 /21???

# rfind()
# replace string -- [:6] 取第六个 date_of_birth[:6]
# generate random number and put them in string