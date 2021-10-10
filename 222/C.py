
N, M = map(int, input().split())
A = []
for i in range(2*N):
    A.append(input())

num_v = {}
for i in range(2*N):
    num_v[str(i)] = 0

rank = sorted(num_v.items(), key=lambda x: x[1], reverse=True)

for round_ in range(M):
    for n in range(1, N+1):
        a = rank[2*n-1-1][0]
        a_t = A[int(a)][round_]
        b = rank[2*n-1][0]
        b_t = A[int(b)][round_]

        # aが勝つ
        if a_t == "G" and b_t == "C":
            num_v[a] += 1
        elif a_t == "C" and b_t == "P":
            num_v[a] += 1
        elif a_t == "P" and b_t == "G":
            num_v[a] += 1
        # b が勝つ
        elif b_t == "G" and a_t == "C":
            num_v[b] += 1
        elif b_t == "C" and a_t == "P":
            num_v[b] += 1
        elif b_t == "P" and a_t == "G":
            num_v[b] += 1

    rank = sorted(num_v.items(), key=lambda x:x[1], reverse=True)


for i in range(2*N):
    print(str(int(rank[i][0])+1))