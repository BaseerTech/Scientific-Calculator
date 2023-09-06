#Creating a Scientific Calculator

import numpy as np

class Scientific_Calculator:
    def addition(self):
        user_value_1 = float(input("Enter the first number: "))
        user_value_2 = float(input("Enter the second number: "))
        print(f"Result: {user_value_1 + user_value_2}")

    def subtraction(self):
        user_value_1 = float(input("Enter the first number: "))
        user_value_2 = float(input("Enter the second number: "))
        print(f"Result: {user_value_1 - user_value_2}")

    def multiplication(self):
        user_value_1 = float(input("Enter the first number: "))
        user_value_2 = float(input("Enter the second number: "))
        print(f"Result: {user_value_1 * user_value_2}")

    def division(self):
        user_value_1 = float(input("Enter the first number: "))
        user_value_2 = float(input("Enter the second number: "))
        print(f"Result: {user_value_1 / user_value_2}")
    def trignometric_calc(self):
        user_input = input("Select one:\n1)Sin\n2)Cos\n3)Tan\nEnter: ").capitalize()
        #user_input = user_input.capitalize()
        user_value = float(input("Enter the value: "))

        if user_input == 'Sin':
            value = np.sin(user_value)
            print(f"Answer: {value}")
        elif user_input == 'Cos':
            value = np.cos(user_value)
            print(f"Answer: {value}")
        elif user_input == 'Tan':
            value = np.tan(user_value)
            print(f"Answer: {value}")
        else:
            print("Invalid choice selected!!!!")

    def geometric_calc(self):
        user_input = input("Select one:\n1)Mean\n2)Median\n3)Standard Deviation\nEnter: ").lower()
        # user_input = user_input.capitalize()
        total_values = int(input("Enter the number of values you want to insert:\n"))
        values_list = []
        for _ in range (total_values):
            user_value = float(input("Enter the value: "))
            values_list.append(user_value)

        if user_input == 'mean':
            value = np.mean(values_list)
            print(f"Answer: {value}")
        elif user_input == 'median':
            value = np.median(values_list)
            print(f"Answer: {value}")
        elif user_input == 'standard deviation':
            value = np.std(values_list)
            print(f"Answer: {value}")
        else:
            print("Invalid choice selected!!!!")

b = Scientific_Calculator()
quit_option = 'y'
while(quit_option == 'y'):
    user_input = input("What operation you would like to perform:\n1)Addition\n2)Subtraction\n"
          "3)Multiplication\n4)Division\n5)Trignometric\n6)Geometric\nInput:").capitalize()
    #user_input = user_input.capitalize()
    if user_input == 'Addition':
        b.addition()
    elif user_input == 'Trignometric':
        b.trignometric_calc()
    elif user_input == 'Geometric':
        b.geometric_calc()
    else:
        print("Invalid")
    quit_option = input("Do you want to continue? y/n: ")