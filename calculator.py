# Calculator-in-Python
# Building a Basic Calculator using Python

# function to add two numbers
def add(x, y):
    return x + y


# function to subtract two numbers
def subtract(x, y):
    return x - y


# function to multiply two numbers
def multiply(x, y):
    return x * y


# function to divide two numbers
def divide(x, y):
    return x / y


# Prompt the user to select option
print("Enter the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # take input from the user
    choice = input("Enter Choice(1/2/3/4): ")

    # Check if Choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break

    else:
        print("Invalid Input")
