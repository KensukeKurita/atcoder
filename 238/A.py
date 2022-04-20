
import math

n = int(input())

if n > 2*math.log2(n):
    print("Yes")
else:
    print("No")