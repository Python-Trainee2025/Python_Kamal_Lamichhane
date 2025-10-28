num = int(input("Enter a number: "))

if num < 2:
    print(f'{num} is not a prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break

    print(f'{num} is a prime number')