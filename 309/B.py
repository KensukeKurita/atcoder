N = int(input())

A = []
for i in range(N):
    A.append(input())


# 1行目
print(A[1][0] + A[0][0:N-1])
# 2~N-1行目
for i in range(1, N-1):
    print(A[i+1][0] + A[i][1:N-1] + A[i-1][N-1])
# N行目
print(A[N-1][1:N] + A[N-2][N-1])
