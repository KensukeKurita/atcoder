N = 1048576

A = [-1] * N

Q = int(input())
for i in range(Q):
    t, x = map(int, input().split())
    if t == 2:
        print(A[x % N])
        continue

    h = x
    while True:
        if A[h % N] != -1:
            h += 1
        else:
            A[h % N] = x
            break
