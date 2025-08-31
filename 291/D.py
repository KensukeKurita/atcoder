
def main():

    N = int(input())


    cards = []
    for _ in range(N):
        cards.append([int(x) for x in input().split()])

    if N == 1:
        print(2)
        return

    mA_0 = 1
    mB_0 = 1
    for i in range(1, N):
        # mA_1
        if (cards[i][0] != cards[i-1][0]) and (cards[i][0] != cards[i-1][1]):
            mA_1 = mA_0 + mB_0
        elif (cards[i][0] != cards[i-1][0]):
            mA_1 = mA_0
        elif (cards[i][0] != cards[i-1][1]):
            mA_1 = mB_0
        
        if (cards[i][1] != cards[i-1][0]) and (cards[i][1] != cards[i-1][1]):
            mB_1 = mA_0 + mB_0
        elif (cards[i][1] != cards[i-1][0]):
            mB_1 = mA_0
        elif (cards[i][1] != cards[i-1][1]):
            mB_1 = mB_0
        
        mA_0 = mA_1
        mB_0 = mB_1

    print((mA_1 + mB_1) % 998244353 )

if __name__ == "__main__":
    main()
