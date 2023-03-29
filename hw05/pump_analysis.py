""" CS5001: Pump Data Analysis By YANTING LAI """


def main():
    """
    Read short_data.txt
    str -> str
    """
    file_name = input("Please enter the file name: ")

    try:
        with open("pump_data\\" + file_name, 'r', encoding="utf-8") as file:
            # list[str] -> ['0\n', '0\n',...'1\n', '0\n', '0\n', '0']
            str_list = file.readlines()
            int_list = [int(i.strip())
                        for i in str_list]  # list[str] -> list[int]
    except FileNotFoundError as _:
        print("Unable to open {file_name}")
        return

    # Calculate the total cover of time in mins, hours, and days
    mins = len(int_list)
    hrs = mins / 60
    days = round((hrs/24), 3)

    # Calculate the valid runtime of the Pump
    valid_time = 0  # calculate how many minutes it actually runs
    total_valid = 0  # calculate the actual watt used
    min_five_gallon = -1
    min_hundred_gallon = -1
    for index, num in enumerate(int_list):
        if num > 1:
            valid_time += 1
            total_valid += num
        if min_five_gallon == -1 and 2 * valid_time >= 5:
            min_five_gallon = index + 1
        if min_hundred_gallon == -1 and 2 * valid_time >= 100:
            min_hundred_gallon = index + 1
            break

    print(f"Data covers a total of {hrs} hours")
    print(f"(That's {days} days)\n")
    print(
        f"Pump was running for {valid_time} minutes"
        + "producing {valid_time*2} gallons")
    print(f"(That's {float(valid_time*2*24)} gallons per day) \n")
    print(f"Pump required a total of {total_valid} watt minutes of power")
    print(f"That's {round((total_valid/60000),3)} kwh \n")
    print(f"It took {min_five_gallon} minutes of data to reach 5 gallons")
    print(
        f"It took {min_hundred_gallon} minutes of data to reach 100 gallons\n")


main()


def extra_credit():
    """
    Read pump_data.txt, calculate pump start, end, and actual runtime
    str -> int
    """
    file_name = input("Please enter the file name: ")

    try:
        with open("pump_data\\" + file_name, 'r', encoding="utf-8") as file:
            # list[str] -> ['0\n', '0\n',...'1\n', '0\n', '0\n', '0']
            str_list = file.readlines()
            int_list = [int(i.strip())
                        for i in str_list]  # list[str] -> list[int]
    except FileNotFoundError as _:
        print("Unable to open {file_name}")
        return

    print("Information on water softener recharges:")

    run_time = 0
    start_time = 0
    end_time = 0

    for index, number in enumerate(int_list):
        if number > 500:
            run_time += 1
        elif run_time >= 120:
            end_time = index
            start_time = end_time - run_time + 1
            print(f"{run_time} minutes run started at {start_time}")
            run_time = 0
            start_time = 0
            end_time = 0
        else:
            run_time = 0


extra_credit()


# 我犯过的错误：
# 1. input 语句打成了print 语句  2. 没有把short_data.txt创建在 hw05的文档下面
# list.strip() 的写法是错的 -- list cannot be stripped
# 如何打印在多少分钟 reach 5 - 10 gallons?
