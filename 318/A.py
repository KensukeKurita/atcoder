N, M, P = [int(x) for x in input().split()]

count = 0
for i in range(1, N+1):
    if i == M or (i-M) % P == 0:
        count += 1

print(count)