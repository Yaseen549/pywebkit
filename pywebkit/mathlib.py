# Simple Math Libraries

def add(*nums):
    number = 0
    for num in nums:
        number += num
    return number


def sub(*nums):
    number = 0
    for num in nums:
        number -= num
    return number


def multiply(*nums):
    number = 1
    for num in nums:
        number *= num
    return number


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def powerof(num1, num2):
    return num1**num2


def div2num(dividend, divisor):
    return dividend/divisor


def sqrt(num):
    return num ** 0.5


def curt(num):
    return num ** (1/3)
