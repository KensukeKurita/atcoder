import math
def get_greatest_common_divisor(a, b):

    # x > y
    """
    if a > b :
        x = a
        y = b
    elif a < b :
        x = b
        y = a
    else:
        # in case a = b
        return a

    while (y):
        x, y = y, x % y

    return x
    """
    return math.gcd(a, b)



def main():
    r = math.gcd(A, math.gcd(B,C))
    print(int((A+B+C)/r -3))
    return 
    

import math
a,b,c = map(int,input().split())
g = math.gcd(math.gcd(a,b),c)
print((a+b+c)//g-3)

