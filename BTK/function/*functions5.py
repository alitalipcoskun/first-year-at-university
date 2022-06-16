import math
import time

def calculate_time(func):
    def wrapper(*argc, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*argc, **kwargs)
        finish = time.time()
        print("Function took "+ str(finish-start)+ " time.")
    return wrapper
@calculate_time
def powering(a,b):
    print(math.pow(a,b))
@calculate_time
def factorisation(num):
    print(math.factorial(num))

powering(3,4)
factorisation(4)