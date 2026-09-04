

if (__name__ == "__main__"):
    print("Welcome to the calculator app here are the rules:"  \
    "\n 1.Choose operation(VALID INPUTS: +,-,*,/,// "  \
    "\n 2.Write down two numbers to perform the operation on." \
    "\n 3.Use 'q' to quit the app")

    actions = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b
    }

    user_input = None
    number_input_1 = None
    number_input_2 = None
    result = None


    while user_input != "q":
        print("\n\n\nEnter one of the valid choices for operation:\n")
        try:
            user_input = input("Your input:")
            if user_input != 'q' and user_input not in actions.keys():
                raise ValueError("Make sure you are entering the correct values!")
        except ValueError as e:
            print(f"\n\n\nError message: {e}")
            continue
        except:
            print(f"\n\n\n[Unknown Error] Please try again!\nError message: {e}")
            continue
       
        if user_input == 'q':
            print("+------------------------------+\n| Thank you for using the app! |\n+------------------------------+")
            break
        else:
            try:
                number_input_1 = float(input("Enter the first number: "))
                number_input_2 = float(input("Enter the second number: "))
            except ValueError as e:
                print(f"\n\n\nError! Please make sure to input numbers!\nError message: {e}")
                continue
            except:
                        print("\n\n\n[Unknown Error] Please try again!")
                        continue
        try:
            result = actions[user_input](number_input_1 , number_input_2)
        except ZeroDivisionError as e:
            print(f"\n\n\nError! Please make sure to not divide by zero!\nError message: {e}")
            continue
        print(f"\n\n----------- RESULT: {result} -----------\n\n\n")

