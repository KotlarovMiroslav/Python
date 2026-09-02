

if (__name__ == "__main__"):
    print("Welcome to the calculator app here are the rules:"  \
    "\n 1.Choose operation(VALID INPUTS: +,-,*,/,// "  \
    "\n 2.Write down two numbers to perform the operation on." \
    "\n 3.Use 'q' to quit the app")
    user_input = None
    number_input_1 = None
    number_input_2 = None
    result = None
    while user_input != "q":
        print("\n\n\nEnter one of the valid choices for operation:\n")
        user_input = input("Your input:")
        if user_input == 'q':
            print("+------------------------------+\n| Thank you for using the app! |\n+------------------------------+")
            break
        else:
            number_input_1 = float(input("Enter the first number: "))
            number_input_2 = float(input("Enter the second number: "))

        # try except blocks can be inplemented here 
        # but the topic for them has not been covered

        if user_input == '+':
            result = number_input_1 + number_input_2
        elif user_input == '-':
            result = number_input_1 - number_input_2
        elif user_input == '*':
            result = number_input_1 * number_input_2
        elif user_input == '/':
            if number_input_2 == 0:
                print("\n\n\n+---------------------------------------+\n| Undefined result for dividing by zero |\n+---------------------------------------+")
                continue
            else:
                result = number_input_1 / number_input_2
        elif user_input == '//':
            if number_input_2 == 0:
                print("\n\n\n+---------------------------------------+\n| Undefined result for dividing by zero |\n+---------------------------------------+")
                continue
            else:
                result = number_input_1 // number_input_2
        else:
            print("\n\n\n\nInvalid operation, please enter a valid operation as mentioned in the rules.\n\n\n\n")
            continue
        print(f"\n\n----------- RESULT: {result} -----------\n\n\n")

