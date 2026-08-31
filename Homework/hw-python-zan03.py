

if (__name__ == "__main__"):
    print("Welcome to the calculator app here are the rules:"  \
    "\n 1.Choose operation(VALID INPUTS: +,-,*,/,// "  \
    "\n 2.Write down two numbers to perform the operation on." \
    "\n 3.Use 'q' to quit the app")
    user_input = None
    result = None
    while(user_input != "q"):
        print("\n\n\nEnter one of the valid choices for operation:\n")
        user_input = input("Your input:")
        print() 

        # try except blocks can be inplemented here 
        # but the topic for them has not been covered

        if(user_input == '+'):
            user_input = float(input("Enter the first number: "))
            result = 0
            result += user_input
            user_input = float(input("Enter the second number: "))
            result += user_input
        elif(user_input == '-'):
            user_input = float(input("Enter the first number: "))
            result = 0
            result -= user_input
            user_input = float(input("Enter the second number: "))
            result -= user_input
        elif(user_input == '*'):
            user_input = float(input("Enter the first number: "))
            result = 1
            result *= user_input
            user_input = float(input("Enter the second number: "))
            result *= user_input
        elif(user_input == '/'):
            user_input = float(input("Enter the first number: "))
            result = 1
            result *= user_input
            user_input = float(input("Enter the second number: "))
            if (user_input == 0):
                print("\n\n\n")
                print("+---------------------------------------+")
                print("| Undefined result for dividing by zero |")
                print("+---------------------------------------+")
                continue
            else:
                result /= user_input     
        elif(user_input == '//'):
            user_input = float(input("Enter the first number: "))
            result = 1
            result *= user_input
            user_input = float(input("Enter the second number: "))
            if (user_input == 0):
                print("\n\n\n")
                print("+---------------------------------------+")
                print("| Undefined result for dividing by zero |")
                print("+---------------------------------------+")
                continue
            else:
                result //= user_input
        elif(user_input == 'q'):
            print("+------------------------------+")
            print("| Thank you for using the app! |")
            print("+------------------------------+")
            continue
        else:
            print("\n\n\n\nInvalid operation, please enter a valid operation as mentioned in the rules.\n\n\n\n")
            continue
        print(f"\n\n----------- RESULT: {result} -----------\n\n\n")

