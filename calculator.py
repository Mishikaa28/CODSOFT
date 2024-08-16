import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Logarithm")


while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            if choice in ('6', '7'):
                num1 = float(input("Enter number: "))
                if choice == '6':
                    print(f"Square Root of {num1} = {sqrt(num1)}")
                elif choice == '7':
                    base = float(input("Enter base (default is 10): ") or 10)
                    print(f"Logarithm of {num1} with base {base} = {logarithm(num1, base)}")
        
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print("Invalid Input")
