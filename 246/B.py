import math

A, B = map(int, input().split())
len = math.sqrt(A**2 + B**2)
print("{} {}".format(A/len, B/len))
