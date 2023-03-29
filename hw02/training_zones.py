def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))
    max_HR = 208 - 0.7*(age)
    HR_reserve = max_HR - restHR

    print(f"Your heart rate reserve is: {HR_reserve} bpm")
    print(f"Here is a breakdown of your training zones: ")

    K = [0.5, 0.6, 0.7, 0.8, 0.93, 1.0]

    for i in range(len(K)-1):
        zone_low = restHR + HR_reserve * K[i]
        zone_high = (restHR + HR_reserve * K[i+1]) -0.01
        if i == len(K)-2:
            zone_high = (restHR + HR_reserve * K[i+1]) 
        print(f"Zone {i+1}: {round(zone_low, 2)} to {round(zone_high, 2)} bpm")

main()