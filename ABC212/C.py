N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

a = 0
b = 0
ans = abs(A[a] - B[b])
while a < N and b < M:
    ans = min(ans, abs(A[a] - B[b]))
    if A[a] < B[b]:
        a+=1
    else:
        b+=1
print(ans)