
N, X = map(int, input().split())
A = [int(a) for a in input().split()]

knwon = set()
count = 0
know = False
while (not know):
    count += 1
    knwon.add(X)
    X = A[X-1]
    if X in knwon:
        break

print(count)
