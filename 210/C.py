# codig : utf-8

def main():
    N, K = map(int, input().split())
    c = [int(a) for a in input().split()]

    e = []
    for i in range(N-K):
        s = set(c[i:i+K])
        e.append(len(s))

    if len(e) == 0:
        print(1)
    else:
        print(max(e))



main()