print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("enter the values: ")
    user_input = input()
    user_input = user_input.split(",")
    print(user_input)
    float_user_input = list(map(float, user_input))
    print(float_user_input)
    return float_user_input

def calc_average_temperature(final_user_inputs):
    total = sum(final_user_inputs)
    average = total/len(final_user_inputs)
    print(average)
    return average

def calc_min_max_temperature(final_user_inputs):
    min_temp = min(final_user_inputs)
    max_temp = max(final_user_inputs)

    print([int(min_temp), int(max_temp)])
    return [int(min_temp), int(max_temp)]

def calc_median_temperature(final_user_inputs):
    sorted_temperatures = sorted(final_user_inputs)
    amtOfNumbers = len(sorted_temperatures)
    if amtOfNumbers % 2 == 0:
        evenNum1 = sorted_temperatures[amtOfNumbers // 2 - 1]
        evenNum2 = sorted_temperatures[amtOfNumbers // 2]
        median = (evenNum1 + evenNum2) / 2
    else:
        median = sorted_temperatures[amtOfNumbers // 2]
    print(median)
    return median

if __name__ == "__main__":
    display_main_menu()
    final_user_inputs = get_user_input()
    calc_average_temperature(final_user_inputs)
    calc_min_max_temperature(final_user_inputs)
    calc_median_temperature(final_user_inputs)
