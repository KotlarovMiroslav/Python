# #Задача 5
# def factorial(n):
#     if(n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Enter a whole number to be factorized: "))
# print(f"Factorial of {n}: {factorial(n)}")

#Задача 6

def checkBrackets(text):
    openedBrackets = 0
    for char in text:
        if char == "(":
            openedBrackets += 1
        elif char == ")":
            openedBrackets -= 1

    if(openedBrackets == 0):
        return True
    else:
        return False

if(checkBrackets("((()))")):
    print("The brackets are correctly clossed!")
else:
    print("The brackets are incorrectly closed!")