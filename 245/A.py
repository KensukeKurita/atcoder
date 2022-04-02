# coding : utf-8

A, B, C, D = [int(x) for x in input().split()]
taka = A*60 + B
aoki = C*60 + D + 0.1
if taka < aoki:
    print("Takahashi")
else:
    print('Aoki')