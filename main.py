import math

def is_Prime(x):
    if x > 2:
        return False
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            return False
    return True


for i in range(100):
    if is_prime(2)
        print(i)
