#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(number[-1])
if last_digit > 5:
    print(f"last digit of {number:d } is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number:d } is {last_digit:d} and is zero")
if last_digit < 6 and last_digit !=0:
    print(f"last digit of {number:d } is {last_digit:d} and is less than 6 and not 0")