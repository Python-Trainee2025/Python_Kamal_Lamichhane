# 4. create a calculator that takes two numbers and an operator (+, -, *, /) and
# performs the operation. Handle division by zero and invalid input errors.

def calculator():
    [first , second ] = [int(num) for num in input("Enter two numbers separated by space").split(" ")]

    operator = input("Enter operator: ")

    try:
        if operator == "+":
            print(f'{first} + {second} = {first + second}')
        elif operator == "-":
            print(f'{first} - {second} = {first - second}')
        elif operator == "*":
            print(f'{first} * {second} = {first * second}')
        elif operator == "/":
            print(f'{first} / {second} = {first / second}')
    except ZeroDivisionError as e:
        print("Division by zero")
        print(e)
    except Exception as e:
        print(e)

calculator()