# coding : utf-8

N = int(input())
A = []
B = []
l_list = {}
l = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    l = l + a / b

kotae = l / 2.0

real_l = 0
l = 0
for i in range(N):
    a = A[i]
    b = B[i]
    l = l + a / b
    real_l = real_l + a

    if kotae <= l:
        # 前のステップまでのreal長さ
        lll = real_l - a
        # 今ステップの割合
        aaa = (kotae - (l - a/b)) * b
        print(aaa + real_l - a)
        break
