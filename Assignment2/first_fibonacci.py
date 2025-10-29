# 1. Write a program that takes a number n and
# prints the first n numbers in the Fibonacci sequence.
# Use both Recursion and regular method

num = int(input('Enter a number: '))

def fibonacci_regular(num):
    if num < 2:
        return num
    first, second = 0, 1
    for i in range(num - 2):
        temp = first
        first = second
        second = temp + first
    return first + second

def fibonacci_recursive(num):
    if num < 2:
        return num
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

for i in range(num):
    # print(fibonacci_regular(i))
    print(fibonacci_recursive(i))