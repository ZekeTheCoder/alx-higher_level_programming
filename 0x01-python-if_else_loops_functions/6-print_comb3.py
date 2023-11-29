#!/usr/bin/python3
number = 0
while number <= 89:
    if number % 10 == 0:
        number += 1 + number // 10
    if number == 89:
        print("{:02d}".format(number))
    else:
        print("{:02d}".format(number), end=", ")
    number += 1
