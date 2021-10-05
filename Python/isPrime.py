import math

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, sqrt(num) + 1):
        if num % i == 0:
            return False

    return True

print(is_prime(3))
