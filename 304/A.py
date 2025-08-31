N = int(input())

name = []
age = []
for _ in range(N):
    a = input().split()
    name.append(a[0])
    age.append(int(a[1]))

idx = age.index(min(age))

for i in range(idx, N):
    print(name[i])
for i in range(0, idx):
    print(name[i])