# coding : utf-8
import sys 
import copy 

def main():

    dp = [0] * (W+1) 
    # 初期化 
    for j in range(W+1):
        if Goods[0][0] <= j:
            dp[j] = Goods[0][1]

    for w, v in Goods[1:]:
        old_dp = copy.deepcopy(dp)
        for j in range(0, W+1):
            # i+1番目の荷物を入れられる場合は、
            # 「j-w[i] → j となって、価値がv[i]加算される」場合と、もとのjとで比較をする
            if w <= j:
                dp[j] = max(old_dp[j - w] + v, old_dp[j])
            else:
                pass
    print(dp[-1])


if __name__ == "__main__":
    input = sys.stdin.readline
    N, W = map(int, input().split())
    Goods = [[int(i) for i in input().split()] for _ in range(N)]
    main()