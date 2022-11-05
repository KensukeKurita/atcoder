N, M = map(int, input().split())
City = {}
for i in range(1, N+1):
    City[str(i)] = set()

for M in range(M):
    a, b = map(int, input().split())

    City[str(a)].add(b)
    City[str(b)].add(a)

for i in range(1, N+1):
    print("{}".format(len(City[str(i)])), end=" ")
    print(*sorted(City[str(i)]))
