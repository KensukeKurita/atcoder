import itertools

# 街の数と道路の情報を設定
N, M = map(int, input().split())
roads = []
for _ in range(M):
    a, b, c = [int(x) for x in input().split()]
    roads.append((a, b, c))

# すべての街の順列を生成
cities = list(range(1, N + 1))
print(cities)



# 最大値を初期化
max_distance = 0

# 各順列に対して通る道路の長さの和を計算
for jj in range(1, N+1):
    permutations = itertools.combinations(cities, jj)
    for perm in permutations:
        print(perm)
        distance = 0
        for i in range(N - 1):
            for A, B, C in roads:
                if (perm[i] == A and perm[i + 1] == B) or (perm[i] == B and perm[i + 1] == A):
                    distance += C
        max_distance = max(max_distance, distance)

# 結果を出力
print(max_distance)
