import random

MIN_RANGE = -100
MAX_RANGE = 100

def absolute_difference(a,b):
    result = abs(a-b)
    return result
    
    
def main():
    random_a = random.randint(MIN_RANGE, MAX_RANGE)
    random_b = random.randint(MIN_RANGE, MAX_RANGE)
    
    result = absolute_difference(random_a, random_b)
    print(f"a={random_a}, b={random_b}, absolute difference={result}")

if __name__ == '__main__':
    main()