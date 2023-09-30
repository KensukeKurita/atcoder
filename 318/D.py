from itertools import combinations

def find_max_edge_sum(N, D):
    # 入力から辺の重みを2次元配列に変換
    edge_weights = [[0] * N for _ in range(N)]
    k = 0
    for i in range(N):
        for j in range(i + 1, N):
            edge_weights[i][j] = D[k]
            k += 1
    return edge_weights

def get_dp_even(N, D):
    score = 0

    # DP
    # dp[選んだノード]

    DP = {}
    DP["0"] = {tuple(range(N)): 0}
    for i in range(1, N//2+1):
        DP[str(i)] = {}
        for state in DP[str(i-1)].keys():
            for tmp in combinations(state, 2):
                new_state = list(state)
                new_state.remove(tmp[0])
                new_state.remove(tmp[1])

                DP[str(i)][tuple(new_state)] = DP[str(i-1)][state] + D[tmp[0]][tmp[1]]

    return score    
   

# 入力の例
N = int(input())
tmp_D = []
for _ in range(N-1):
    tmp = [int(x) for x in input().split()]
    tmp_D.extend(tmp)
D = find_max_edge_sum(N, tmp_D)

if N % 2 == 0:
    get_dp_even(N, D)
