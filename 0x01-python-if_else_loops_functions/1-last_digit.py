#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = abs(number)
print("Last digit of {} is {} and is ".format(number, abs_num % 10), end="")
if abs_num % 10 > 5:
    print("greater than 5")
elif abs_num % 10 == 0:
    print("0")
else:
    print("less than 6 and not 0")
