
N = int(input())

list_p = [int(a) for a in input().split()]
d_p = {}
for i in range(N):
	d_p[str(list_p[i])] = i + 1

list_re = []
for i in range(N):
	list_re.append(d_p[str(i+1)])
print(*list_re)
