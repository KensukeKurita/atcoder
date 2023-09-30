
N = int(input())
S = []

t = 0
unique = set()
for _ in range(N):
    S = input()
    rev_S = S[::-1]
    if (S not in unique) and (rev_S not in unique):
        unique.add(S)
        unique.add(rev_S)
        t += 1
print(t)

