import itertools

# 累積和を考える。
N, K = map(int, input().split())
A = [int(a) for a in input().split()]
S = [0]
S.extend(list(itertools.accumulate(A)))

result = []
for l in range(N):
    for r in range(l, N):
        result.append(S[r+1] - S[l])

print(len([x for x in result if x == K]))
