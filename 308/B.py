
N, M = map(int, input().split())

C = input().split()
D = input().split()
P = [int(x) for x in input().split()]

price_dict = {}
for i, d in enumerate(D):
    price_dict[d] = P[i+1]

total = 0
for eat in C:
    if eat not in price_dict.keys():
        total += P[0]
    else:
        total += price_dict[eat]


print(total)

