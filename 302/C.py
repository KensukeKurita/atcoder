import itertools

def check(l) -> bool:

    for i in range(1, N, 1):
        # 完全一致はダメ
        if l[i-1] == l[i] :
            return False
        
        count = 0
        for j in range(M):
            if l[i-1][j] != l[i][j]:
                count += 1
        if count > 1:
            return False

    return True

N, M = map(int, input().split())
list_S = []
for _ in range(N):
    list_S.append(input())

for a in itertools.permutations(list_S, N):
    # 1つでも列があれば良い
    if check(a):
        print("Yes")
        break
else:
    print("No")