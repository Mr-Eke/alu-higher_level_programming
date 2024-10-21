#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit, using absolute value for negative numbers
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit  # Preserve negative sign for negative numbers

if last_digit < 6 and last_digit != 0:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
elif last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
else:
    print(f'Last digit of {number} is {last_digit} and is 0')
