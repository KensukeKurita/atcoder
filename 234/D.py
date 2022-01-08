
import bisect

N, K = map(int, input().split())
P = [int(x) for x in input().split()]

list_p = sorted(P[0:K])  # len(list_p) = K
print(list_p[-K])

for i in range(K, N):
    bisect.insort_left(list_p, P[i])
    print(list_p[-K])
