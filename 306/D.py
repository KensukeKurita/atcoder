N = int(input())

G_DP = {} # good
G_DP["0"] = 0
B_DP = {} # bad
B_DP["0"] = 0

for i in range(1, N+1):
    x, y = map(int, input().split())

    if x == 0:
        G_DP[str(i)] = max(max(B_DP[str(i-1)], G_DP[str(i-1)]) + y, G_DP[str(i-1)])
        B_DP[str(i)] = B_DP[str(i-1)] #下げてもらう
    else:
        G_DP[str(i)] = G_DP[str(i-1)] # 下げてもらう
        B_DP[str(i)] = max(G_DP[str(i-1)] + y, B_DP[str(i-1)])

print(max(G_DP[str(N)], B_DP[str(N)]))