A, B = map(int, input().split())

n = A // B
if A % B == 0:
    print(n)
else:
    print(n+1)