import itertools

S, K = input().split()
K = int(K)

list_s = []
for s in S:
	list_s.append(s)
list_s.sort()

all = []
ans = list(itertools.permutations(list_s))
for i in ans:
	all.append(''.join(i))
all = list(set(all))
all.sort()
print(all[K-1])