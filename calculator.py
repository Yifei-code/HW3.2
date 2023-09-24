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
    x=int(input("enter an integer values:"))
    y=int(input("enter anthor integer values: "))
    
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
    print(exponent(x,y))
    
# if __name__ == "__main__":
main()