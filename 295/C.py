N = int(input())
A = [int(a) for a in input().split()]

count = 0
pool = set()
for a in A:
    if a not in pool:
        pool.add(a)
    else:
        pool.remove(a)
        count += 1
print(count)
