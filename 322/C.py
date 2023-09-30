N, M = map(int, input().split())
A = [int(x) for x in input().split()]

i = 1
for a in A:
    flag = True
    while flag:
        if i <= a:
            print(a-i)
            i = i + 1
        else:
            flag = False