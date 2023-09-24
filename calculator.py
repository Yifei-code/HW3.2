# add
import math

def add(x,y):
    result = x + y
    return f"{x} + {y} = {result}"

def subtract(x,y):
    result = x - y
    return f"{x} - {y} = {result}"

def multiply(x,y):
    result = x * y
    return f"{x} * {y} = {result}"

def divide(x,y):
    if y == 0:
        return f"{x} / {y} = NaN"
    else:
        result = x / y
        return f"{x} / {y} = {result}"

def exponent(x,y):
    result = math.pow(x,y)
    return f"{x} ^ {y} = {result}"



def main():
    print(add())
    print(subtract())
    print(multiply())
    print(divide())
    print(exponent())