
N = int(input())
S = []
for i in range(N):
    S.append(input())
X, Y = map(str, input().split())

if S[int(X)-1] == Y:
    print("Yes")
else:
    print("No")