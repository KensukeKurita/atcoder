
N = int(input())
A = [int(x) for x in input().split()]
A.sort()

im = min(A) - 1
for i in A:
    if i == im + 1:
        im = i
    else:
        print(i-1)
        break