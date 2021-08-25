# coding : utf-8

def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(int(input()))

    before = 101
    count = 0
    for i in range(N):
        big = max(d)
        if big < before:
            count += 1
            before = big
        d.remove(big)

    print(count)

if __name__=="__main__":
    main()
