import bisect

N, Q = map(int, input().split())
A = [int(a) for a in input().split()]
A.sort(reverse=False)

for i in range(Q):
    x = int(input())
    print(N - bisect.bisect_left(A, x))

