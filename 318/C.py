
N, D, P = [int(x) for x in input().split()]
F = [int(x) for x in input().split()]

all_F = sum(F)
minus_price = 0
F.sort(reverse=True)

i = 0
flag = True
while flag:
    tmp = sum(F[i:(i+D)])
    if tmp > P:
        minus_price += tmp - P
        i = i + D
    else:
        flag = False

print(all_F - minus_price)

"""
チケットを使い切らない場合
5 3 10
10 5 5 3 20 


"""