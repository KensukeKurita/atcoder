
N = int(input())
A = [int(a) for a in input().split()]

angle = [0]

for i in range(N):
    a = A[i]
    for j in range(len(angle)):
        angle[j] += a
    angle.append(0)

for j in range(len(angle)):
    angle[j] = angle[j] % 360

angle.sort()
angle.append(360)
diff = []
for i in range(1, len(angle)):
    diff.append(angle[i] - angle[i-1])

print(max(diff))