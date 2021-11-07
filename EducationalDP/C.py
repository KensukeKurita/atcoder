import numpy as np

def main():
    N = int(input())

    a, b, c = [], [], []
    for i in range(N):
        aa, bb, cc = map(int, input().split())
        a.append(aa)
        b.append(bb)
        c.append(cc)

    dp = np.full((N, 2), 0, dtype=int)


if __name__ == '__main__':
    main()