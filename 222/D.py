
N = int(input())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]

c = []
for i in range(N):
    c.append(range(a[i], b[i]+1))

print(c)