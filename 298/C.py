import bisect

def get_query(text):
    
    if text[0] == "1":
        q = text.split()
        return q[0], int(q[1]), int(q[2])
    elif text[0] == "2":
        q = text.split()
        return q[0], int(q[1])
    else:
        q = text.split()
        return q[0], int(q[1])


N = int(input())
Q = int(input())

hako = {}
for n in range(1, N+1):
    hako[str(n)] = []

card = {}

for _ in range(Q):
    query = get_query(input())
    if query[0] == "1":
        bisect.insort(hako[str(query[2])], query[1])
        
        if str(query[1]) in card.keys():
            card[str(query[1])].add(query[2])
        else:
            card[str(query[1])] = set()
            card[str(query[1])].add(query[2])

    elif query[0] == "2":
        print(*hako[str(query[1])])
    else:
        print(*card[str(query[1])])

"""
5
8
1 1 4
1 2 4
1 1 1
2 4
1 1 4
2 4
3 1
3 2

"""