""" This is """
def extra_credit():
    """
    Extra
    """
    file_name = input("Please enter the file name: ")

    try:
        with open("pump_data\\" + file_name, 'r', encoding = "utf-8") as file: # under pump_data dir
            str_list = file.readlines() # list[str] -> ['0\n', '0\n',...'1\n', '0\n', '0\n', '0']
            int_list = [int(i.strip()) for i in str_list] # list[str] -> list[int]
    except FileNotFoundError as _:
        print("Unable to open {file_name}")
        return

    print("Information on water softener recharges:")

    run_time = 0
    start_time = 0
    end_time = 0

    for index, number in enumerate(int_list):
        if number>500:
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
