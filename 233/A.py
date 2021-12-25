import math

X, Y = map(int, input().split())
a = (Y - X) / 10.0

if a <= 0:
    print(0)
else:
    print(math.ceil(a))