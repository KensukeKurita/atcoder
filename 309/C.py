
def main():

    N, K = map(int, input().split())

    med = []
    total = 0
    for _ in range(N):
        tmp = input().split()
        med.append((int(tmp[0]), int(tmp[1])))
        total += int(tmp[1])

    med.sort(key=lambda x: (x[0], x[1]))

    if total <= K:
        print(1)
        return
    
    for a, b in med:
        total -= b
        if total <= K:
            print(a+1)
            return

main()
