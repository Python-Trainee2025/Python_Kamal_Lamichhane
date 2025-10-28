num = int(input("Enter a number: "))

if num < 2:
    print(f'{num} is not a prime number')
else:
    flag = False
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number')
            flag = True
            break
    else:
        print(f'{num} is a prime number')