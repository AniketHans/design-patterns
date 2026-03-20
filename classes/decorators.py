import time

# Decorator for calculatng the time of execution of a function
def timer(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"{func.__name__}'s execution time is {endTime - startTime}")
        return result
    return wrapper

@timer
def add(a,b):
    return a+b

print(add(10,15))