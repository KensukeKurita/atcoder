N = int(input())
A = [int(x) for x in input().split()]


for i in range(N):
    print(sum(A[7*i : 7*i+7]), end=" ")