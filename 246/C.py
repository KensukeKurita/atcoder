
N, K, X = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort(reverse=True)
B = []
for a in A:
    a_mod = a % X
    # 残りのクーポンの額と最適に使える商品の価格を比較。
    if (a-a_mod) >= K*X:
        a_new = a - K*X
        K = 0
    else:
        # a-a_mod < K*X の時
        # クーポンの方が多い場合は、0円になる手前で止める。
        a_new = a_mod
        K = K - (a-a_mod)//X
    B.append(a_new)

B.sort()

print(sum(B[0:len(B)-K]))