N = int(input())
data = []

for i in range(N):
    A, B = map(int, input().split())
    success_rate = float(A) / float(A + B)
    data.append((i+1, success_rate))

data.sort(key=lambda x: (-x[1], x[0]))

for i in range(N):
    print(data[i][0], end=" ")