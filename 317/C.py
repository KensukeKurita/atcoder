from collections import deque
import itertools

def compare(aaaa, bbbb):
    if aaaa >= bbbb:
        return aaaa
    else:
        return bbbb

N, M = map(int, input().split())

# 全探査してみる
roads = {}
for i in range(M):
    a, b, c = [int(x) for x in input().split()]
    roads[(a-1, b-1)] = c

# DPテーブルの初期化
# DP[今いる街i][(未踏の街)] = この状態に遷移するまでの長さの最大値
DP = {}
for i in range(N):
    DP[str(i)] = {}
    for j in range(0, N+1):
        for test in itertools.combinations(range(N), j):
            DP[str(i)][tuple(test)] = -float('inf')

# 初期条件
# 街 i をスタート地点とする。
for i in range(N):
    tmp = list(range(N))
    tmp.remove(i)
    DP[str(i)][tuple(  tmp   )] = 0

for j in range(N, -1, -1):
    for state in itertools.combinations(range(N), j):
        for now in range(N):
            # 今の街が、未踏の街なわけがない。
            if now in state:
                continue
            else:
                for next_city in range(N):
                    # 次の街は、未踏の街にふくまれている必要がある。
                    if next_city in state:
                        # now と next をつなぐ道がある場合は、
                        if tuple([min([now, next_city]), max([now, next_city])]) in roads.keys():
                            tmp = list(state)
                            tmp.remove(next_city)

                            a = DP[str(now)][tuple(state)] + roads[(min(now, next_city), max(now, next_city))]
                            b = DP[str(next_city)][tuple(sorted(tmp))]
                            DP[str(next_city)][tuple(tmp)] =  compare(a, b)
                    else:
                        continue
        print(state, [DP[str(k)][state] for k in range(N)])

max_length = -1
for j in range(0, N):
    for state in itertools.combinations(range(N), j):
        for now in range(N):
            max_length = max(max_length, DP[str(now)][tuple(state)])
print(max_length)