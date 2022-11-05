
N = int(input())

S = {}
for i in range(N):
    name = input()
    if not name in S.keys():
        S[name] = 1
    else:
        S[name] += 1

SS = sorted(S.items(), key=lambda  x:x[1], reverse=True)
print(SS[0][0])