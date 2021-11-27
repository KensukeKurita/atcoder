N, K = map(int, input().split())
score = {}
for i in range(N):
    score[str(i+1)] = sum([int(p) for p in input().split()])

score = sorted(score.items(), key=lambda x:x[1], reverse=True)

ans = {}
for i in range(N):
    num, s = score[i]
    if s + 300 >= score[K-1][1]:
        ans[str(num)] = "Yes"
    else:
        ans[str(num)] = "No"

for i in range(N):
    print(ans[str(i+1)])
