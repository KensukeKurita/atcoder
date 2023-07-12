import heapq
Q = int(input())


fukuro = []
heapq.heapify([])
offset = 0
for _ in range(Q):
    query = input()
    if query[0] == "1":
        X = int(query.split()[1])
        heapq.heappush(fukuro, X - offset)
    elif query[0] == "2":
        X = int(query.split()[1])
        offset += X
    else:
        ans = heapq.heappop(fukuro)
        print(ans + offset)
    # print(fukuro)

"""
7
1 1
2 10
1 5
1 3
3
2 2
3

"""
