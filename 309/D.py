from collections import deque

# 頂点sからスタートする幅優先探索
def BFS(s):
    dist = {}
    q = deque()
    q.append(s)
    dist[str(s)] = 0
    while q:
        now = q.popleft()
        if str(now) not in graph.keys():
            graph[str(now)] = []
        for nxt in graph[str(now)]:
            if str(nxt) not in dist.keys():
                dist[str(nxt)] = dist[str(now)] + 1
                q.append(nxt)
    return dist


N1, N2, M = [int(x) for x in input().split()]

graph = {}
for i in range(M):
    a, b = map(int, input().split())
    if str(a) not in graph.keys():
        graph[str(a)] = []
    graph[str(a)].append(b)

    if str(b) not in graph.keys():
        graph[str(b)] = []
    graph[str(b)].append(a)

# print(graph)
# print(BFS(str(1)))
# print(BFS(str(N1+N2)))
print(max(BFS(str(1)).values()) + max(BFS(str(N1+N2)).values()) + 1)