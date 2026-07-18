# Exercise 1: Greeting
# Write a program that asks the user for their name and prints a greeting in the format: "Hello, <name>!"

def greeting():
    userName = input("What is your name? ").strip().title()

    print(f'Hello, {userName}')

# greeting()



# Exercise 2: Calculator
# Write a program that asks the user for two numbers and an operation (+, -, *, /), then prints the result.

def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)

# calculator(float(input("Enter first number: ")), float(input("Enter second number: ")), input("Enter operator (+, -, *, /): "))



# Exercise 3: Addition Function
# Create a function add(x, y) that returns the sum of x and y.
# Then call it and print the result.

def add(x, y):
    return x + y

# print(add(5, 3))


# Exercise 4: Square of a Number
# Write a function square(n) that returns n * n.
# Ask the user for a number, call the function, and print the result.

def square(num):
    return num ** 2

# print(square(float(input("Enter number "))))


# Exercise 5: Number Check
# Ask the user for a number.
# Print whether the number is positive, negative, or zero.

def defineNumber(num):
    if num > 0:
        state = "positive"
    elif num < 0:
        state = "negative"
    elif num == 0:
        state = "0"

    return f"Number is {state}"

# print(defineNumber(float(input("Enter number "))))

# Exercise 6: Even or Odd
# Ask the user for a number.
# Print whether it is even or odd.

def isOdd(num):
    if num % 2 == 0:
        state = 'even'
    elif num % 2 == 1:
        state = 'odd'

    return f'Number is {state}'
        
# print(isOdd(float(input("Enter number "))))


# Exercise 7: Converting a String to a Number
# Ask the user for two numbers.
# Print their sum.
# Compare the result with the behavior of using raw input values without conversion.

def convertStrToInt(num1, num2):
    return [f"With convertion {int(num1) + int(num2)}", f"Without convertion {num1 + num2}"]

# print(convertStrToInt(input("Enter first number "), input("Enter second number ")))


# Exercise 8: Formatted Output
# Ask the user for a number, compute its square, and print the result.

def formSquare(num):
    return num ** 2

# print(square(float(input("Enter number "))))


# Exercise 9: Strings and Formatting
# Ask the user for their name.
# Remove extra whitespace and format the name correctly.
# Then print: "Hello, <Name>!"

def greetUser(name):
    return f"Hello, {name.strip().title()}"

print(greetUser(input("What is your name? ")))



# Exercise 10: Mini Project
# Create a console-based personal calculator.
# The program should:
# 1. ask for the user's name;
# 2. print a greeting;
# 3. let the user choose an operation (+, -, *, /);
# 4. ask for two numbers;
# 5. perform the calculation;
# 6. print the result.


def personalCalculator():
    result = None

    name = input("What is your name ").strip().title()
    print(f'Hello, {name}')

    operator = input("Choose operator to calculate ")
    num1 = float(input("enter first number "))
    num2 = float(input("enter second number "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        return
    
    print(f'Result is {result}')

# personalCalculator()