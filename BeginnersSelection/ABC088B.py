# coding : utf-8

def main():
    N = int(input())
    a = list(map(int, input().split()))

    alice = 0
    bob = 0
    for i in range(N):
        biggest = max(a)
        if i % 2 ==0:
            alice += biggest
        else:
            bob += biggest

        a.remove(biggest)

    print(alice - bob)

if __name__=="__main__":
    main()
