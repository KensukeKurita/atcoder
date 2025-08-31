from collections import deque

N, M = map(int, input().split())

S = input()
C = [int(c) for c in input().split()]

colors = {str(color): deque() for color in range(1, M+1)}
for i, c in enumerate(C):
    colors[str(c)].append(S[i])

for color_deque in colors.values():
    color_deque.rotate(1)

result = []
for c in C:
    result.append(colors[str(c)].popleft())

print("".join(result))