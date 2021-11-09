# coding : utf-8
import sys

def main(N, W, Goods):
    # dp[品物][重さ] = 最大の価値
    # とすると、配列の次元が100*10^9となり、大変。
    # dp[品物][価値] = 最小の重さ
    # としてやるとよさそう。
    inf = 10**12
    max_v = N * 10**3
    dp = [[inf for _ in range(max_v+1)] for _ in range(N+1)]
    dp[0][0] = 0

    i = 0
    for w, v in Goods:
        for j in range(max_v+1):
            if v <= j :
                dp[i+1][j] = min(dp[i][j], dp[i][j-v]+w)
            else:
                dp[i+1][j] = dp[i][j]
                    
        i += 1

    # 価値が高い順に、重さを見て、基準をクリアしたものを出力
    for j in range(max_v, 0, -1):             
        if dp[N][j] <= W:
            print(j)
            break



if __name__ == "__main__":
    input = sys.stdin.readline
    N, W = map(int, input().split())
    Goods = [[int(i) for i in input().split()] for _ in range(N)]

    main(N, W, Goods)